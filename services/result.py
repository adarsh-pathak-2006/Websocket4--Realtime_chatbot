from services.build_prompt import build_prompt
from services.ping import generate_response

def final_response(query):
    prompt=build_prompt(query=query)
    answer=generate_response(prompt)
    return answer