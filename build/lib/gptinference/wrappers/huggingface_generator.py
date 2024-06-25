import os
from typing import Dict, Any, List, Union
from transformers import AutoTokenizer, AutoModelForCausalLM
# from llama_cpp import Llama
import random
import time
from transformers import pipeline
import pdb

class HuggingFaceGeneratorWrapper:
    @staticmethod
    def call(
        prompt: Union[str, List[str], List[Dict[str, str]]],
        max_tokens: int,
        temperature: float,
        generator: pipeline,
        device: str = "cpu",
    ) -> dict:
            
        if isinstance(prompt, List):
            assert len(prompt) >= 1, f"No prompt given as input to the HF Generator Wrapper system"

        # pass through generator

        # pdb.set_trace()

        do_sample = False
        if temperature > 0:
            do_sample=True

        print("..........................................................", do_sample)

        response = generator(prompt,
                            max_new_tokens=max_tokens,
                            temperature=temperature,
                            return_full_text=False,
                            do_sample=do_sample) 

        return response

    @staticmethod
    def get_first_response(response) -> Dict[str, Any]:
        # pdb.set_trace()
        # if is_chat_based_agent(engine):
        # assert response[0]['generated_text'][-1]['role'] == 'assistant'
        text = response[0]['generated_text']
        # else:
        #     text = response["choices"][0]["text"]
        return text