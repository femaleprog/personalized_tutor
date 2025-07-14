import sys
sys.path.append('/Users/cozzy/Desktop/personal-projects/tutor/src')
import requests

from rag import retrieve_chunk

def test_retrieval():

    response = requests.get('https://raw.githubusercontent.com/run-llama/llama_index/main/docs/docs/examples/data/paul_graham/paul_graham_essay.txt')
    text = response.text
    question = "What were the two main things the author worked on before college?"
    retrieved_chunk = retrieve_chunk(question, text)
    print(retrieved_chunk)
    return retrieved_chunk

test_retrieval()