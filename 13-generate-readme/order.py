import time
import random
from typing import Dict, List

class OrderService:
    def __init__(self):
        self.inventory = {
            "laptop": 5,
            "mouse": 10,
            "keyboard": 7
        }

    def validate_order(self, order: Dict[str, int]) -> bool:
        """Check if requested items are in stock."""
        for item, qty in order.items():
            if item not in self.inventory or self.inventory[item] < qty:
                return False
        return True

    def reserve_items(self, order: Dict[str, int]) -> None:
        """Reserve items by reducing inventory."""
        for item, qty in order.items():
            self.inventory[item] -= qty
        print("[Inventory] Reserved items:", order)

    def process_payment(self, amount: float) -> bool:
        """Simulate payment processing."""
        print(f"[Payment] Processing payment of ${amount:.2f}...")
        time.sleep(1)
        if random.random() > 0.1:  # 90% chance of success
            print("[Payment] Payment successful ✅")
            return True
        print("[Payment] Payment failed ❌")
        return False

    def generate_invoice(self, order: Dict[str, int], amount: float) -> str:
        """Generate invoice ID."""
        invoice_id = f"INV-{random.randint(1000, 9999)}"
        print(f"[Invoice] Generated invoice {invoice_id} for ${amount:.2f}")
        return invoice_id

    def ship_order(self, order: Dict[str, int], invoice_id: str) -> str:
        """Simulate order shipment."""
        shipment_id = f"SHP-{random.randint(10000, 99999)}"
        print(f"[Shipping] Order shipped! Shipment ID: {shipment_id}")
        return shipment_id

    def process_order(self, order: Dict[str, int], price_list: Dict[str, float]) -> None:
        """Full order pipeline."""
        print("=== ORDER PIPELINE START ===")
        if not self.validate_order(order):
            print("[Error] Order validation failed.")
            return

        self.reserve_items(order)
        total = sum(price_list[item] * qty for item, qty in order.items())

        if not self.process_payment(total):
            print("[Error] Payment failed. Releasing inventory.")
            for item, qty in order.items():
                self.inventory[item] += qty
            return

        invoice = self.generate_invoice(order, total)
        shipment = self.ship_order(order, invoice)
        print(f"[Success] Order completed. Invoice: {invoice}, Shipment: {shipment}")
        print("=== ORDER PIPELINE END ===")


if __name__ == "__main__":
    service = OrderService()
    demo_order = {"laptop": 1, "mouse": 2}
    price_list = {"laptop": 1200.0, "mouse": 25.0, "keyboard": 45.0}

    service.process_order(demo_order, price_list)
