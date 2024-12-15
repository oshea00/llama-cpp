from openai import OpenAI
client = OpenAI(base_url="http://127.0.0.1:8080", api_key="na")

completion = client.chat.completions.create(
    model="Phi3",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message.content)