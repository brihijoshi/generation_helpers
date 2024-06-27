from gptinference.helper import LLamaCppHelper
from gptinference.helper import HuggingFaceGeneratorHelper

helper = HuggingFaceGeneratorHelper(model="microsoft/Phi-3-mini-4k-instruct", cache_path='cache.jsonl', device='cpu')

# helper = LLamaCppHelper(repo_id="Qwen/Qwen2-0.5B-Instruct-GGUF",filename="*q8_0.gguf",cache_path="cache.jsonl")

messages=[
    [
    {
      "role": "system",
      "content": "You are an expert travel guide.",
    },
    {
      "role": "user",
      "content": "Tell me fun things to do in San Francisco.",
    }
    ]
]

print(helper.call_batch(prompts=messages, temperature=1.0, cache_result=False, num_return_sequences=3))