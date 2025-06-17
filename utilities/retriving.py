#loading vectordb
from langchain_community.vectorstores import FAISS
from utilities.embedding import embeddings
from langchain_openai import ChatOpenAI
import os 
from dotenv import load_dotenv
load_dotenv()

def retriving(query: str):
    db = FAISS.load_local('vectorstore', embeddings, allow_dangerous_deserialization=True)
    retrived_contents = db.similarity_search(query, k=3)
    llm = ChatOpenAI(
        model='gpt-4o-mini', 
        temperature=0.6
    )
    prompt = f"""
    Use the following content extracted from a document to answer the user's question.

    ### Extracted Content:
    {retrived_contents}

    ### Question:
    {query}
    """
    response = llm.invoke(prompt)
    return response.content
