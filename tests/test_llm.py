import sys
sys.path.append('/Users/cozzy/Desktop/personal-projects/tutor/src')
import requests

from rag import retrieve_chunk
from model import run_mistral
def test_llm():

    response = requests.get('https://raw.githubusercontent.com/run-llama/llama_index/main/docs/docs/examples/data/paul_graham/paul_graham_essay.txt')
    text = response.text
    question = "What were the two main things the author worked on before college?"
    retrieved_chunk = retrieve_chunk(question, text)
    response = run_mistral(question,retrieve_chunk)

test_llm()