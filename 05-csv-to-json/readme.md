# Lab 05 — Convert CSV to JSON using Copilot

### 🎯 Goal

Use **Copilot Chat (Agent Mode)** to generate Python code that reads a CSV file and outputs a JSON file.

---

## ✅ Task

1. In this folder, you have `data.csv`.
2. Create a new file `convert.py`.
3. Ask Copilot to generate a script that:

   * reads the CSV,
   * converts it to JSON,
   * saves output to a file (e.g., `output.json`).

> You should not code manually — describe what you want in natural language and let Copilot generate the code.

---

## 🔧 Prompts to use

### Generate script

```
Create a Python script that reads data.csv and converts it to JSON. Save the result to output.json. Use json and csv modules.
```

### Optional — pretty formatting

```
Modify the script to format JSON with indentation = 4.
```

### Optional — add CLI argument

```
Add support for input/output file paths passed as command-line arguments.
```

---

## ✅ Success criteria

* Script reads CSV and saves JSON.
* You generated code using prompts (no manual coding).
* Script runs without errors.

---

## 📄 Example CSV (`data.csv`)

```
id,name,role
1,Alice,Admin
2,Bob,Developer
3,Eve,Security
```

---

### Expected `output.json`

```json
[
  { "id": "1", "name": "Alice", "role": "Admin" },
  { "id": "2", "name": "Bob", "role": "Developer" },
  { "id": "3", "name": "Eve", "role": "Security" }
]
```

---
