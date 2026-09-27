"""Reusable LLM comparison example: OpenAI vs Groq."""
import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
openai_client = OpenAI()
groq_client = OpenAI(api_key=os.getenv("GROQ_API_KEY"), base_url="https://api.groq.com/openai/v1")
def battle(prompt):
    messages = [{"role": "user", "content": prompt}]
    a = openai_client.chat.completions.create(model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"), messages=messages)
    b = groq_client.chat.completions.create(model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"), messages=messages)
    return a.choices[0].message.content, b.choices[0].message.content
if __name__ == "__main__":
    a, b = battle("Explain what an LLM is in two sentences.")
    print("\n--- OpenAI ---\n", a)
    print("\n--- Groq ---\n", b)
