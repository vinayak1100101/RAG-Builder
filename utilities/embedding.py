from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os
embeddings=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
def embedding(chunks:list):
    db=FAISS.from_documents(chunks,embeddings)
    if 'vectorstore' not in os.listdir():
        os.makedirs('vectorstore')
    db.save_local('vectorstore')
    return db