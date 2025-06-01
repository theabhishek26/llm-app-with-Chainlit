from together import Together
from src.prompt import  system_instruction

client = Together()

messages=[{"role": "user", "content": system_instruction}]
def ask_order(messages,model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",temperature=0):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message.content

