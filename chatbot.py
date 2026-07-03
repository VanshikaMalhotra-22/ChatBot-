from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2")

def ask_llm(question, context):

    prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the context below.

If the answer is not present in the context, say:
"I couldn't find that information in the uploaded document."

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    return response.content