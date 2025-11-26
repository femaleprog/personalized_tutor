from mistralai import Mistral
import numpy as np
import faiss
import os
import json
from dotenv import load_dotenv
load_dotenv()


api_key = os.environ.get("MISTRAL_API_KEY")
client = Mistral(api_key = api_key)

data_path = os.path.join(os.path.dirname(__file__),'../../data/ai_resources.json')

with open(data_path, 'r') as f:
    resources = json.load(f)


def get_text_embedding(input):
    embeddings_batch_response = client.embeddings.create(
          model="mistral-embed",
          inputs=input
      )
    return embeddings_batch_response.data[0].embedding



def get_chunks(resources : list) -> list :
    chunks = []
    for item in resources:
        chunk = f"""
        Title : {item['title']},
        Type : {item['type']}
        Provider: {item['provider']}
        Topics: {', '.join(item['topics'])}
        Summary: {item['summary']}
        Link: {item['link']}
        """
        chunks.append(chunk.strip())
    return chunks


def retrieve_chunk(question : str):

    chunks = get_chunks(resources)
    text_embeddings = np.array([get_text_embedding(chunk) for chunk in chunks])
    d = text_embeddings.shape[1]
    index = faiss.IndexFlatL2(d)
    index.add(text_embeddings)
    question_embeddings = np.array([get_text_embedding(question)])
    D, I = index.search(question_embeddings, k=3) # distance, index
    retrieved_chunk = [chunks[i] for i in I.tolist()[0]]
    return retrieved_chunk




