from gptinference.openai_wrapper import LLamaCppHelper

helper = LLamaCppHelper(repo_id="Qwen/Qwen2-0.5B-Instruct-GGUF",filename="*q8_0.gguf",cache_path="cache.jsonl")

messages=[
    {
      "role": "system",
      "content": "You are an expert travel guide.",
    },
    {
      "role": "user",
      "content": "Tell me fun things to do in San Francisco.",
    }
]

helper.call(prompt=messages,logprobs=True)