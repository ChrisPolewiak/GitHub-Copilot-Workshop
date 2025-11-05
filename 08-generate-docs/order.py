from dataclasses import dataclass
from typing import Any, Dict, Iterable, List
import json

# Order domain objects
@dataclass
class Product:
    sku: str
    title: str
    price: float
    stock: int


class ProductCatalog:
    def __init__(self):
        self._items: Dict[str, Product] = {
            "BK-001": Product("BK-001", "Dune", 39.99, 12),
            "BK-002": Product("BK-002", "Neuromancer", 29.99, 8),
            "BK-003": Product("BK-003", "Clean Code", 59.99, 5),
        }

    def get(self, sku: str) -> Product:
        return self._items[sku]

    def has_stock(self, sku: str, qty: int) -> bool:
        p = self.get(sku)
        return p.stock >= qty

    def reserve(self, sku: str, qty: int) -> None:
        p = self.get(sku)
        if p.stock < qty:
            raise ValueError("Insufficient stock")
        p.stock -= qty


class PaymentGateway:
    def charge(self, amount: float, card_token: str) -> str:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if not card_token or not card_token.startswith("tok_"):
            raise ValueError("Invalid payment token")
        return "ch_" + card_token[4:]


class Notifier:
    def send(self, address: str, subject: str, body: str) -> None:
        print(f"[MAIL] To:{address} | {subject}\n{body}")


# Pipeline flow
class OrderService:
    def __init__(self, catalog: ProductCatalog, payments: PaymentGateway, notifier: Notifier):
        self.catalog = catalog
        self.payments = payments
        self.notifier = notifier

    def process(self, order: Dict[str, Any]) -> Dict[str, Any]:
        lines = self._normalise_lines(order.get("items", []))
        self._validate_request(order, lines)
        total = self._price_items(lines)
        self._reserve_inventory(lines)
        charge_id = self._charge_payment(total, order["payment_token"])
        self._send_notification(order, total, charge_id)
        return {"total": total, "charge_id": charge_id}

    # --- Steps in the flow ---
    def _validate_request(self, order: Dict[str, Any], lines: List[Dict[str, Any]]) -> None:
        if "customer_email" not in order or not order["customer_email"]:
            raise ValueError("Missing customer email")
        if "items" not in order or not lines:
            raise ValueError("Order must contain at least one item")
        for line in lines:
            if line["qty"] <= 0:
                raise ValueError("Quantities must be positive integers")
            if not self.catalog.has_stock(line["sku"], line["qty"]):
                raise ValueError(f"No stock for {line['sku']}")

    def _price_items(self, lines: List[Dict[str, Any]]) -> float:
        total = 0.0
        for line in lines:
            product = self.catalog.get(line["sku"])
            total += product.price * line["qty"]
        return round(total, 2)

    def _reserve_inventory(self, lines: List[Dict[str, Any]]) -> None:
        for line in lines:
            self.catalog.reserve(line["sku"], line["qty"])

    def _charge_payment(self, amount: float, token: str) -> str:
        return self.payments.charge(amount, token)

    def _send_notification(self, order: Dict[str, Any], total: float, charge_id: str) -> None:
        subject = "Order confirmation"
        body = json.dumps({"total": total, "charge_id": charge_id, "items": order["items"]}, indent=2)
        self.notifier.send(order["customer_email"], subject, body)

    @staticmethod
    def _normalise_lines(items: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Return a normalised copy of the line items with validated keys."""

        normalised: List[Dict[str, Any]] = []
        for line in items:
            if not isinstance(line, dict):
                raise TypeError("Order line items must be dictionaries")
            if "sku" not in line or not line["sku"]:
                raise ValueError("Each line item requires a SKU")
            if "qty" not in line:
                raise ValueError("Each line item requires a quantity")
            qty = line["qty"]
            if not isinstance(qty, int):
                raise TypeError("Quantities must be integers")
            normalised.append({"sku": line["sku"], "qty": qty})
        return normalised

