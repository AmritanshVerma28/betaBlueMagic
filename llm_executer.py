import os
from dataclasses import dataclass, asdict
from ctransformers import AutoModelForCausalLM, AutoConfig
import time as t


@dataclass
class GenerationConfig:
    temperature: float
    top_k: int
    top_p: float
    repetition_penalty: float
    max_new_tokens: int
    seed: int
    reset: bool
    stream: bool
    threads: int
    stop: list[str]

class llm_executer():

    def get_generator_config(self,temperature=0.2, top_k=50, top_p=0.9,
                             repetition_penalty=1, max_new_tokens=512):

        generation_config = GenerationConfig(
            temperature=temperature,
            top_k=top_k,
            top_p=top_p,
            repetition_penalty=repetition_penalty,
            max_new_tokens=max_new_tokens,  # adjust as needed
            seed=42,
            reset=True,  # reset history (cache)
            stream=True,  # streaming per word/token
            threads=int(os.cpu_count() / 6),  # adjust for your CPU
            stop=["<|endoftext|>"],
        )
        return generation_config


    def format_prompt(self,ip: str, ty: str):
        if ty == "replit":
            op = """### Instruction:
    {""" + ty + """}

    ### Response:"""

        if ty == "llama_2_v1":
            op = """<s>[INST] <<SYS>>
    You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.

    If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.
    <</SYS>>

     [/INST]</s>
    <s>[INST] """ + ip + """ [/INST]"""
        if ty == "llama_2_v2":
            op = """[INST] """ + ip + """ [/INST]"""
        return op




    def generate(
            self,llm: AutoModelForCausalLM,
            generation_config: GenerationConfig,
            user_prompt: str,
    ):
        """run model inference, will return a Generator if streaming is true"""
        op = self.format_prompt(user_prompt,"llama_2_v2")
        llm_res = llm(op,**asdict(generation_config))
        return llm_res

    def get_response(self):
        generation_config = self.get_generator_config()



        config = AutoConfig.from_pretrained(
            bp,
            context_length=2048,
        )
        llm = AutoModelForCausalLM.from_pretrained(
            mp,
            model_type=mt,
            config=config,
        )

        formatted_user_prompt = format_prompt(qry.strip(), "replit")
        generator = generate(llm, generation_config, formatted_user_prompt)
        print("###### " + model_selected + " ######\n")
        for word in generator:
            #  p(word)
            print(word, end="", flush=True)
