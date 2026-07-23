def build_prompt(query):
    prompt=f"""
You are a helpful AI assistant.

User:
{query}

Assistant:
"""
    return prompt