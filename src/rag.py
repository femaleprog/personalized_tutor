from mistralai import Mistral
import numpy as np
import faiss
from getpass import getpass

api_key= getpass("Type your API Key")
client = Mistral(api_key=api_key)

def get_text_embedding(input):
    embeddings_batch_response = client.embeddings.create(
          model="mistral-embed",
          inputs=input
      )
    return embeddings_batch_response.data[0].embedding



def get_chunks(text : str, chunk_size : int = 2048 ) -> list :

    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    return chunks

def retrieve_chunk(question : str,  text : str):

    chunks = get_chunks(text)
    text_embeddings = np.array([get_text_embedding(chunk) for chunk in chunks])
    d = text_embeddings.shape[1]
    index = faiss.IndexFlatL2(d)
    index.add(text_embeddings)
    question_embeddings = np.array([get_text_embedding(question)])
    D, I = index.search(question_embeddings, k=2) # distance, index
    retrieved_chunk = [chunks[i] for i in I.tolist()[0]]
    return retrieved_chunk




