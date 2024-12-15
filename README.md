# Running llama-server locally with docker

Running a local LLM using llama.cpp project.

## Prerequisites
* Huggingface cli update/install
```
pip install -U "huggingface_hub[cli]"
```
* Docker desktop


## Running llama-server
Steps:
* Download the GGUF file for model you want to host. A good model that runs on CPU and has MIT license is Phi-3.
```
huggingface-cli download microsoft/Phi-3-mini-4k-instruct-gguf Phi-3-mini-4k-instruct-q4.gguf --local-dir ~/repos/models --local-dir-use-symlinks False
```
* Run the model using docker server container
```
docker run -d -v ~/repos/models:/models -p 8080:5000  ghcr.io/ggerganov/llama.cpp:server -m /models/Phi-3-mini-4k-instruct-q4.gguf --port 5000
```
* UI at http://127.0.0.1:8080
* API at http://127.0.0.1:8080/v1/chat/completions
* Curl script
```
curl http://127.0.0.1:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "Phi3",
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "Hello!"
      }
    ]
  }'
  
```
* Python example using openai package
```python
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
```
