# 📄 DocuMind AI - Personal Data Assistant

An AI-powered chatbot that answers questions from an uploaded PDF using **Retrieval-Augmented Generation (RAG)**. The application combines **Flask**, **LangChain**, **FAISS**, **HuggingFace Embeddings**, and **Llama 3.2 (via Ollama)** to provide accurate document-based responses.

---

## 🚀 Features

- 📄 Upload any PDF document
- 💬 Ask questions about the uploaded document
- 🤖 AI-generated answers using Llama 3.2
- 🔍 Semantic search using FAISS Vector Database
- 🧠 HuggingFace sentence embeddings
- ⚡ Runs completely locally using Ollama
- 🌐 Simple Flask-based web interface

---

## 🏗️ Project Architecture

```
                User
                  │
                  ▼
          Upload PDF / Ask Question
                  │
                  ▼
              Flask Backend
                  │
      ┌───────────┴───────────┐
      ▼                       ▼
   PDF Upload              Chat Request
      │                       │
      ▼                       ▼
 PyPDFLoader            Retrieve Chunks
      │                       │
      ▼                       ▼
Text Splitter            FAISS Search
      │                       │
      ▼                       ▼
Embeddings               Relevant Context
      │                       │
      └──────────────┬────────┘
                     ▼
               Llama 3.2 (Ollama)
                     ▼
                Final Response
```

---

## 🛠️ Technologies Used

### Backend
- Python
- Flask

### AI & Machine Learning
- LangChain
- Ollama
- Llama 3.2
- HuggingFace Embeddings
- FAISS

### Document Processing
- PyPDFLoader
- RecursiveCharacterTextSplitter

### Frontend
- HTML
- CSS
- JavaScript

---

## ⚙️ How It Works

1. User uploads a PDF document.
2. The PDF is read using **PyPDFLoader**.
3. The document is split into smaller chunks.
4. Each chunk is converted into vector embeddings.
5. The embeddings are stored inside a **FAISS Vector Database**.
6. When the user asks a question:
   - FAISS retrieves the most relevant chunks.
   - Those chunks are sent to **Llama 3.2**.
   - The LLM generates an answer using the retrieved context.

This approach is called **Retrieval-Augmented Generation (RAG)**.

---

## 📂 Project Structure

```
Personal-Data-Assistant/
│
├── app.py                 # Flask application
├── chatbot.py             # Llama interaction
├── rag.py                 # RAG pipeline
├── requirements.txt
├── README.md
├── .gitignore
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
└── uploads/
```

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/your-repository.git
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Ollama and pull the Llama model:

```bash
ollama pull llama3.2
```

Run the application:

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## 🎯 Future Improvements

- Support multiple PDFs
- Maintain chat history
- Display source citations
- Drag & Drop PDF upload
- User authentication
- Cloud deployment
- Streaming AI responses
- Better UI/UX

---

## 📚 Key Concepts Demonstrated

- Retrieval-Augmented Generation (RAG)
- Large Language Models (LLMs)
- Semantic Search
- Vector Databases
- Embeddings
- Prompt Engineering
- Flask Web Development
- REST APIs

---

## 👩‍💻 Author

**Vanshika Malhotra**

Built as an AI/ML project to demonstrate the practical implementation of Retrieval-Augmented Generation (RAG) using open-source tools.