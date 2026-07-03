# 📄 DocuMind AI – RAG Chatbot

## Overview

DocuMind AI is a Retrieval-Augmented Generation (RAG) chatbot that answers user questions based on an uploaded PDF document.

The application uses LangChain, FAISS, HuggingFace Embeddings, Ollama, and Llama 3.2 to provide accurate document-based responses.

---

## Features

- Upload any PDF
- Ask questions about the uploaded document
- Local LLM using Ollama (Llama 3.2)
- FAISS vector database
- HuggingFace Embeddings
- Flask web interface

---

## Technologies Used

- Python
- Flask
- LangChain
- Ollama
- Llama 3.2
- FAISS
- HuggingFace Embeddings
- HTML
- CSS
- JavaScript

---

## Project Flow

Upload PDF

↓

Read PDF

↓

Split into Chunks

↓

Create Embeddings

↓

Store in FAISS

↓

Retrieve Relevant Chunks

↓

Generate Answer using Llama 3.2

---

## Future Improvements

- Multiple PDF support
- Chat history
- User authentication
- Cloud deployment
- Citation of document sources
