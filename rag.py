from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def load_pdf(pdf_path):

    loader = PyPDFLoader(pdf_path)

    documents = loader.load()

    return documents

def split_documents(documents):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = text_splitter.split_documents(documents)

    return chunks

def create_vector_store(chunks):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = FAISS.from_documents(
        chunks,
        embeddings
    )

    return vector_store

def retrieve_documents(vector_store, question):

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 2}
    )

    documents = retriever.invoke(question)

    return documents