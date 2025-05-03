import chromadb

def init_collection(name="slides"):
    client = chromadb.Client()
    return client.create_collection(name=name)

def add_documents(collection, docs, start_slide=1):
    metadatas = [{"slide": i + start_slide} for i in range(len(docs))]
    ids = [str(i) for i in range(len(docs))]
    collection.add(documents=docs, metadatas=metadatas, ids=ids)

def query_documents(collection, query, n=2):
    return collection.query(query_texts=[query], n_results=n)
