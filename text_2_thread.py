import os
from llm import LLM

def thread_creator_prompt(text):
    prompt = f"""\You are a twitter thread generator, Your job is to take the following delimited text as input and generate a list of JSON formatted twitter thread.
    each part should not be more than 100 words, make each part engaging enough and ensure that all the text is included across different tweets.
    
    text: ```{text}```
    
    output format : <json> [{{"number":"part_text"}}, ...] </json>
    """
    return prompt

def main():
    model = LLM(model_id="gemma:2b")
    files = os.listdir("./inputs")
    for file in files:
        if file[-4:] == ".txt":
            print(f"for {file}: ")
            with open(f"./inputs/{file}", 'r') as f:
                text = f.read()
                prompt = thread_creator_prompt(text)
                print(prompt)
                output = model.generate_full_response(messages=[{"role": "user", "content": prompt}])
                print(output)

if __name__ == "__main__":
    main()