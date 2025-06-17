from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunker(docs:list):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
    chunks=text_splitter.split_documents(docs)
    return chunks