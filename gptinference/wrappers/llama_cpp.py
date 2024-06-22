import os
from typing import Dict, Any, List, Union
# from llama_cpp import Llama
import random
import time
import pdb

class LlamaCppWrapper:
    @staticmethod
    def call(
        prompt: Union[str, List[str], List[Dict[str, str]]],
        max_tokens: int,
        engine,
        temperature: float,
        logprobs: bool,
    ) -> dict:
        
            # if is_chat_based_agent(engine): # gpt 3.5 onwards.
            # check if batched requests (list of text prompts) are requested.
            # batched_requested = isinstance(prompt, List) and len(prompt) > 1 and isinstance(prompt[0], str)
            # assert not (batched_requested and is_chat_based_agent(engine)), \
            #     f"Open AI does not support batched requests. Check your prompt in the call to OpenaiAPIWrapper."
            
        if isinstance(prompt, List):
            assert len(prompt) >= 1, f"No prompt given as input to the LLama CPP system"

        # check if prompt is a list of strings or a list of dictionaries
        # gpt-3.5-turbo onwards does not support a batched list of prompts.
        # but, the conversation API does support a list of dictionaries.
        conversational_content = [{"role": "user", "content": prompt[0]}] if isinstance(prompt, List) and isinstance(prompt[0], str) \
                    else ([{"role": "user", "content": prompt}] if isinstance(prompt, str) \
                    else prompt)
        pdb.set_trace()
        response = engine.create_chat_completion(
            messages=conversational_content,
            temperature=temperature,
            max_tokens=max_tokens,
            logprobs=logprobs,
            top_logprobs=1
        )
        return response

    @staticmethod
    def get_first_response(response) -> Dict[str, Any]:
        """Returns the first response from the list of responses.
        Sample response:
        {
        "choices": [
            {
            "finish_reason": "stop",
            "index": 0,
            "message": {
                "content": "The 2020 World Series was played in Texas at Globe Life Field in Arlington.",
                "role": "assistant"
            },
            "logprobs": null
            }
        ],
        "created": 1677664795,
        "id": "chatcmpl-7QyqpwdfhqwajicIEznoc6Q47XAyW",
        "model": "gpt-3.5-turbo-0613",
        "object": "chat.completion",
        "usage": {
            "completion_tokens": 17,
            "prompt_tokens": 57,
            "total_tokens": 74
        }
        }
        """
        pdb.set_trace()
        # if is_chat_based_agent(engine):
        text = response['choices'][0]['message']['content']
        # else:
        #     text = response["choices"][0]["text"]
        return text

    # @staticmethod
    # def get_first_response_batched(response, engine) -> List[Dict[str, Any]]:
    #     """Returns the first response from the list of responses."""
    #     if is_chat_based_agent(engine):
    #         for r in response["choices"]:
    #             yield r.message.content
    #     else:
    #         for r in response["choices"]:
    #             yield r["text"]

    # @staticmethod
    # def get_all_responses(response, engine) -> Dict[str, Any]:
    #     """Returns the list of responses."""
    #     return [choice["text"] for choice in response["choices"]]  # type: ignore