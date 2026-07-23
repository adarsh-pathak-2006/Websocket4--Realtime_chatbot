from google import genai
from django.conf import settings

client=genai.Client(api_key=settings.GEMINI_API_KEY)

async def generate_response_async(prompt):
    response = await client.aio.models.generate_content_stream(model='gemini-2.5-flash', contents=prompt)
    async for chunk in response:
        yield chunk.text

