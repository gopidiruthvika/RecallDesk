# 🧠 RecallDesk

### AI Customer Support with Persistent Memory

RecallDesk is an AI-powered customer support agent that remembers important information from previous customer interactions and uses that context to provide more personalized support.

Instead of asking customers to repeatedly explain the same problem, RecallDesk can recall relevant previous interactions and continue the conversation with context.

---

## 🎯 Problem

Traditional AI customer support systems often treat each conversation as a new interaction.

For example:

> Customer: "My UPI payment is failing."

Later:

> Customer: "My UPI payment is failing again."

Without persistent memory, the support agent may not know what happened previously.

RecallDesk solves this by storing important customer interaction information and recalling it when relevant.

---

## 💡 How RecallDesk Works

```text
Customer
   │
   ▼
RecallDesk Interface
   │
   ├──► Recall previous customer information
   │          │
   │          ▼
   │      Hindsight Memory
   │
   ▼
Groq LLM
   │
   ▼
Personalized Support Response
   │
   ▼
Store new interaction
   │
   ▼
Hindsight Memory
```

The core workflow is:

1. Customer submits a support question.
2. RecallDesk searches Hindsight for relevant previous information.
3. Retrieved information is provided to the LLM as context.
4. The LLM generates a personalized support response.
5. The new interaction is stored in Hindsight for future conversations.

---

## 🧠 Why Hindsight?

Hindsight provides persistent memory for RecallDesk.

It allows the application to:

* Retain customer interaction information.
* Recall relevant information during future interactions.
* Maintain customer-specific memory.
* Use previous context to personalize support responses.

RecallDesk uses customer-specific tags so that memories are associated with the correct customer.

---

## 🧪 Example

### First interaction

**Customer ID:** `DEMO003`

**Customer:**

> My UPI payment is failing on my Android phone.

At this point, there may be no previous memory for the customer.

RecallDesk generates a support response and stores the interaction.

### Later interaction

**Customer:**

> My UPI payment is failing again. What should I do?

RecallDesk retrieves relevant information from the customer's previous interaction.

The AI can then use that context to provide a more personalized response instead of treating the customer as completely new.

---

## 🛠️ Technologies

* **Python** — Application development
* **Streamlit** — User interface
* **Hindsight** — Persistent memory
* **Groq** — Large language model inference
* **python-dotenv** — Environment variable management
* **GitHub** — Version control and project hosting

---

## 📁 Project Structure

```text
RecallDesk/
│
├── app.py
├── hindsight_memory.py
├── llm.py
├── requirements.txt
├── .env.example
├── .gitignore
│
├── test_agent.py
├── test_groq.py
└── test_hindsight.py
```

### File Description

**`app.py`**
Main Streamlit application.

**`hindsight_memory.py`**
Handles retaining and recalling customer memories using Hindsight.

**`llm.py`**
Handles communication with the Groq LLM.

**`requirements.txt`**
Contains the Python dependencies required to run the project.

**`.env.example`**
Template showing the environment variables required by the application.

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/shivanireddy445/RecallDesk.git
cd RecallDesk
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project directory.

Add:

```text
HINDSIGHT_API_KEY=your_hindsight_api_key
HINDSIGHT_BASE_URL=https://api.hindsight.vectorize.io
GROQ_API_KEY=your_groq_api_key
```

Never commit the `.env` file or expose API keys publicly.

### 5. Run RecallDesk

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🔐 Security

API keys are stored in `.env` and excluded from Git using `.gitignore`.

The repository only contains `.env.example` with placeholder values.

Never add real API keys to the GitHub repository.

---

## 🚀 Future Improvements

Possible future improvements include:

* Conversation history view.
* Better memory summarization.
* Automatic detection of important customer preferences.
* Support for multiple support categories.
* Analytics for recurring customer issues.
* Human support-agent handoff.
* More advanced customer profiles.

---

## 📌 Limitations

The current version is an MVP focused on demonstrating persistent customer memory.

The support interactions are primarily designed for demonstration and do not connect to a real customer support platform or payment system.

---

## 👩‍💻 Project

**RecallDesk**
AI Customer Support with Persistent Memory

Built with Python, Streamlit, Hindsight, and Groq.
