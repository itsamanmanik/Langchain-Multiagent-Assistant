# 🤖 Multi-Agent Coding Assistant

A **LangGraph + LangChain** powered multi-agent system that helps you **write and debug Python code** — running **100% locally** using Ollama. No API keys. No cost.

---

## 🧠 Agent Pipeline

```
User Request
     │
     ▼
┌──────────────┐
│ 🧠 Planner   │  Breaks down the problem into a structured plan
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ 💻 Coder     │  Writes clean Python code following the plan
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ 🐛 Debugger  │  Reviews code, fixes bugs, returns final output
└──────────────┘
```

---

## 🗂️ Project Structure

```
langchain-multiagent-assistant/
├── agents/
│   ├── __init__.py
│   ├── planner.py       # Planner agent
│   ├── coder.py         # Coder agent
│   └── debugger.py      # Debugger agent
├── ui/
│   └── app.py           # Streamlit web UI
├── graph.py             # LangGraph orchestration
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## ⚙️ Setup & Run

### 1. Install Ollama
Download from [https://ollama.com](https://ollama.com) and install it.

### 2. Pull a model
```bash
ollama pull llama3
```

### 3. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/langchain-multiagent-assistant.git
cd langchain-multiagent-assistant
```

### 4. Create a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 5. Install dependencies
```bash
pip install -r requirements.txt
```

### 6. Run the app
```bash
streamlit run ui/app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🚀 Usage

1. Type your coding task (e.g. *"Write a Python function to find all prime numbers up to N"*)
2. Or paste broken code and ask it to debug
3. Click **Run Agents**
4. View the Plan → Code → Debugged Code pipeline
5. Download the final `.py` file

---

## 🛠️ Supported Models (via Ollama)

| Model | Command |
|---|---|
| LLaMA 3 (recommended) | `ollama pull llama3` |
| CodeLlama | `ollama pull codellama` |
| Mistral | `ollama pull mistral` |
| Gemma 2 | `ollama pull gemma2` |

---

## 👤 Author

**Aman Manikpuri**  
[LinkedIn](https://linkedin.com/in/aman-manikpuri) · [GitHub](https://github.com/itsamanmanik)
