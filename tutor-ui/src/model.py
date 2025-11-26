import os
from mistralai import Mistral

from dotenv import load_dotenv
load_dotenv()

api_key = os.environ.get("MISTRAL_API_KEY")
client = Mistral(api_key=api_key)

def generate_prompt(retrieved_chunk, question):

    prompt = f"""
    Context information is below.
    ---------------------
    {retrieved_chunk}
    ---------------------
    Given the context information and not prior knowledge, answer the query.
    Query: {question}
    Answer:
    """
    return prompt


def run_mistral(user_message, model="mistral-large-latest"):
    messages = [
        {
            "role": "user", "content": user_message
        }
    ]
    chat_response = client.chat.complete(
        model=model,
        messages=messages
    )
    return (chat_response.choices[0].message.content)

