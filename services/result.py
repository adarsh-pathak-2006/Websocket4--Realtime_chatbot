from services.build_prompt import build_prompt
from services.ping import generate_response_async

async def final_response_async(query):
    prompt=build_prompt(query=query)
    async for chunk in generate_response_async(prompt):
        yield chunk