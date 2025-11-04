# GitHub Copilot Workshop

A hands-on workshop designed to teach developers how to effectively use **GitHub Copilot** and **Copilot Chat** to accelerate coding workflows, refactor legacy code, generate tests, and automate documentation.

---

# Codespaces

Right click to open in GitHub Codespaces:

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/ChrisPolewiak/GitHub-Copilot-Workshop?quickstart=1)



## 🎯 Workshop Goals

This workshop demonstrates practical use cases for GitHub Copilot, including:

- **Code generation** from natural language comments
- **Code explanation** and documentation with AI assistance
- **Refactoring** legacy and obfuscated code
- **Test generation** using pytest
- **Data transformation** (CSV to JSON)
- **Infrastructure as Code** (Bicep to YAML)
- **Script conversion** between languages (PowerShell to Bash)
- **Automated documentation** generation

---

## 📋 Prerequisites

Before starting the workshop, ensure you have:

- **Visual Studio Code** installed
- **GitHub Copilot** extension enabled (requires active subscription)
- **GitHub Copilot Chat** extension enabled
- **Python 3.x** (for Python labs)
- **Node.js** (for JavaScript lab)
- **Azure Bicep CLI** (optional, for Lab 06)
- **pytest** (for Lab 07): `pip install pytest`

---

## 🗂️ Repository Structure

```text
GitHub-Copilot-Workshop/
│
├── 01-create-fn/              # Generate Python functions from comments
│   ├── main.py                # Example Python file
│   └── readme.md              # Lab instructions
│
├── 02-improve-fn/             # Add docstrings and comments using Copilot Chat
│   ├── example01.py           # Sample function to improve
│   ├── example02.py           # Another sample function
│   └── readme.md              # Lab instructions
│
├── 03-refactor-js/            # Refactor obfuscated jQuery to clean JavaScript
│   ├── example.js             # Obfuscated JavaScript code
│   └── readme.md              # Lab instructions
│
├── 04-refactor-legacy/        # Refactor legacy Python code
│   ├── example01.py           # Legacy Python code
│   └── readme.md              # Lab instructions
│
├── 05-csv-to-json/            # Convert CSV to JSON using AI-generated code
│   ├── data.csv               # Sample CSV data
│   └── readme.md              # Lab instructions
│
├── 06-bicep-to-yaml/          # Generate YAML config from Bicep template
│   ├── deploy.bicep           # Azure Bicep template
│   └── readme.md              # Lab instructions
│
├── 07-generate-tests/         # Auto-generate unit tests with pytest
│   └── readme.md              # Lab instructions
│
├── 08-powershell-to-bash/     # Convert PowerShell scripts to Bash
│   └── readme.md              # Lab instructions
│
├── 09-generate-readme/        # Generate repository documentation
│   └── readme.md              # Lab instructions
│
└── 10-webapp-from-sql/        # Generate full CRUD web app from SQL schema
    ├── schema.sql             # Database schema
    └── readme.md              # Lab instructions
```

---

## 🚀 How to Run the Examples

### General Workflow

Each lab follows a similar pattern:

1. **Navigate to the lab folder**

    ```powershell
   cd 01-create-fn
   ```

2. **Read the `readme.md`** to understand the lab goals and tasks

3. **Use the suggested prompts** with GitHub Copilot or Copilot Chat

4. **Accept suggestions** using `Tab` (inline) or apply chat responses

5. **Run/test the code** to verify the output

---

### Lab-Specific Instructions

#### **Lab 01 — Generate Functions from Comments (Python)**

- Create a Python file and write only comments describing functions
- Press `Enter` after comments and let Copilot generate the code
- Accept suggestions with `Tab`
- Test by running: `python main.py`

#### **Lab 02 — Improve Functions with Copilot Chat**

- Open existing Python files
- Use `/explain` to understand the code
- Ask Copilot Chat to add docstrings and comments
- Review and accept changes

#### **Lab 03 — Refactor Obfuscated JavaScript**

- Open `example.js` with messy jQuery code
- Use Copilot Chat to understand and refactor the code
- Convert to clean, modern JavaScript
- Test in browser or Node.js

#### **Lab 04 — Refactor Legacy Python Code**

- Open `example01.py` with legacy code
- Use `/explain` to understand the logic
- Use `/fix` to refactor into modern, clean Python
- Verify behavior remains unchanged

#### **Lab 05 — Convert CSV to JSON**

- Use natural language prompts to generate conversion script
- Run: `python convert.py`
- Check `output.json` for results

#### **Lab 06 — Generate YAML from Bicep**

- Open `deploy.bicep`
- Use `/explain` to analyze parameters
- Ask Copilot to generate `deploy.yaml` with sample values
- Verify YAML structure matches Bicep expectations

#### **Lab 07 — Generate Unit Tests**

- Open your Python functions file
- Ask Copilot Chat to generate pytest tests
- Run tests: `pytest test_function.py`
- Review coverage and edge cases

#### **Lab 08 — Convert PowerShell to Bash**

- Open PowerShell script
- Use `/explain` to understand the script
- Ask Copilot to convert to Bash with same behavior
- Test on Linux/Mac or WSL

#### **Lab 09 — Generate README**

- Use `/explain` to analyze the entire repository
- Ask Copilot to generate comprehensive README
- Review and customize as needed

#### **Lab 10 — Generate Full CRUD Web App from SQL Schema**

- Create a new project folder
- Add `schema.sql` to the project
- Use Copilot Chat with the provided prompt to generate:
  - Flask application structure (routes, models, templates)
  - Bootstrap UI with navigation
  - CRUD operations for Categories and Products
- Run: `flask --app app run --debug`
- Test all CRUD operations in the browser

---

## 💡 Key Copilot Commands

### **Inline Suggestions**

- `Tab` — Accept suggestion
- `Alt + ]` — Next suggestion
- `Alt + [` — Previous suggestion
- `Esc` — Dismiss suggestion

### **Copilot Chat Commands**

- `/explain` — Explain selected code
- `/fix` — Fix problems in code
- `/tests` — Generate unit tests
- `/doc` — Add documentation
- `@workspace` — Include workspace context

---

## 🎓 Learning Outcomes

After completing this workshop, you will be able to:

✅ Generate code from natural language descriptions  
✅ Refactor and modernize legacy codebases  
✅ Automatically generate unit tests  
✅ Convert between programming languages  
✅ Generate infrastructure configuration files  
✅ Create comprehensive documentation with AI assistance  
✅ Improve code quality with AI-powered suggestions  

---

## 📚 Additional Resources

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [GitHub Copilot Best Practices](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/)
- [VS Code Copilot Extension](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)

---

## 🤝 Contributing

This is a workshop repository. Feel free to:

- Add more labs
- Improve existing examples
- Share feedback and suggestions

---

## 📄 License

This workshop is provided for educational purposes.

---

## 🔄 Workflow Diagram

```text
┌─────────────────┐
│  Write Comment  │
│   or Prompt     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ GitHub Copilot  │
│   Generates     │
│      Code       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Review & Test  │
│     Output      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Accept or Refine│
└─────────────────┘
            GitHub Copilot Workshop Flow
            ═══════════════════════════════

    ┌─────────────────────────────────────────────────────────┐
    │                    DEVELOPER INPUT                      │
    │  • Write comments describing desired functionality      │
    │  • Ask questions in Copilot Chat                        │
    │  • Select code for refactoring                          │
    └───────────────────────┬─────────────────────────────────┘
                │
                ▼
    ┌─────────────────────────────────────────────────────────┐
    │                  GITHUB COPILOT AI                      │
    │  ┌─────────────────────────────────────────────────┐   │
    │  │  Inline Suggestions  │  Copilot Chat (Agent)    │   │
    │  │  ─────────────────── │  ───────────────────────  │   │
    │  │  • Auto-complete     │  • /explain              │   │
    │  │  • Function gen      │  • /fix                  │   │
    │  │  • Code snippets     │  • /tests                │   │
    │  │                      │  • /doc                  │   │
    │  └─────────────────────────────────────────────────┘   │
    └───────────────────────┬─────────────────────────────────┘
                │
                ▼
    ┌─────────────────────────────────────────────────────────┐
    │                    AI GENERATES                         │
    │  • Python/JavaScript/Bash code                          │
    │  • Unit tests (pytest)                                  │
    │  • Documentation & comments                             │
    │  • Refactored clean code                                │
    │  • Configuration files (YAML, JSON)                     │
    └───────────────────────┬─────────────────────────────────┘
                │
                ▼
    ┌─────────────────────────────────────────────────────────┐
    │                 DEVELOPER REVIEWS                       │
    │  • Press Tab to accept inline suggestions               │
    │  • Review chat responses                                │
    │  • Test generated code                                  │
    │  • Verify behavior matches requirements                 │
    └───────────────────────┬─────────────────────────────────┘
                │
        ┌───────────┴───────────┐
        │                       │
        ▼                       ▼
    ┌─────────────────────┐ ┌─────────────────────┐
    │   ✅ ACCEPT         │ │   🔄 REFINE         │
    │   Deploy/Use        │ │   Ask for changes   │
    │   the code          │ │   Iterate again     │
    └─────────────────────┘ └──────────┬──────────┘
                       │
                       │
        └──────────────────────┘
             (Loop back to input)


    Example Flow for Lab 01:
    ═══════════════════════

    Comment: "Create function that calculates average"
     │
     ▼
    Copilot generates:
     def average(numbers):
         return sum(numbers) / len(numbers)
     │
     ▼
    Press Tab → Test → ✅ Success!
```


## Happy Coding with GitHub Copilot! 🚀
