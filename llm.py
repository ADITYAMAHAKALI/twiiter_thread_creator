from ollama import Client
from typing import List,Dict,Optional
class LLM():
    def __init__(self,model_id:str="mistral:text",host:str='http://localhost:11434'):
        self.model_id =  model_id
        self.client = Client(host=host)
    
    def generate_full_response(self,messages:List[Dict[str,str]])->str:
        response = self.client.chat(model=self.model_id, messages=messages)
        print(response)
        return response['message']['content']
   
    def generate_stream_response(self,messages:List[Dict[str,str]]):
        stream = self.client.chat(
        model=self.model_id,
        messages=messages,
        stream=True,
        )
        return stream

if __name__ == '__main__':
    llm = LLM()
    response = llm.generate_full_response([{"role":"system",
                                            "content":'you are an expert python coder'},
                                           {"role":"user",
                                            "content":"create a graph class, implementing graph data structure and methods"}
                                           ])
    messages = [
    {
        'role': 'user',
        'content': 'Why is the sky blue?',
    },
    ]

    response2 = llm.generate_full_response(messages=messages)
    print(response2)