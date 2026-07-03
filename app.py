from flask import Flask, render_template, request, jsonify
from chatbot import ask_llm
import os
from rag import (
    load_pdf,
    split_documents,
    create_vector_store,
    retrieve_documents
)

app = Flask(__name__)

vector_store = None

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    global vector_store

    data = request.get_json()

    question = data["message"]

    if vector_store is None:
        return jsonify({
            "response": "Please upload a PDF first."
        })

    documents = retrieve_documents(vector_store, question)

    context = "\n\n".join(
        [doc.page_content for doc in documents]
    )

    response = ask_llm(question, context)

    return jsonify({
        "response": response
    })

@app.route("/upload", methods=["POST"])
def upload():

    global vector_store

    try:

        if "pdf" not in request.files:
            return jsonify({
                "message": "❌ No file selected."
            }), 400

        file = request.files["pdf"]

        if file.filename == "":
            return jsonify({
                "message": "❌ Please choose a PDF."
            }), 400

        filepath = os.path.join(UPLOAD_FOLDER, file.filename)

        file.save(filepath)

        documents = load_pdf(filepath)

        chunks = split_documents(documents)

        vector_store = create_vector_store(chunks)

        return jsonify({
            "message": f"✅ {file.filename} uploaded successfully!"
        })

    except Exception as e:

        print(e)

        return jsonify({
            "message": "❌ Error processing PDF."
        }), 500



if __name__ == "__main__":
    app.run(debug=True)