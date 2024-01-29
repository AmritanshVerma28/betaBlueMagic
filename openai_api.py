import os
from openai import OpenAI


class openAI():

    def get_res(self,ip):
        print("get res called")
        print("get_res start")
        client = OpenAI(
            # This is the default and can be omitted
            api_key=os.environ.get("OPENAI_API_KEY"),
        )
        system_msg = """You are chatting with an python programmer. You only respond by writing python codes. The output produced should be directly executable in python"""
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": system_msg,
                },
                {
                    "role": "user",
                    "content": ip,
                }
            ],
            model="gpt-3.5-turbo",
        )
        print()
        op = chat_completion.choices[0].message.content
        print("op is "+str(op))
        print("get_res end")
        return op