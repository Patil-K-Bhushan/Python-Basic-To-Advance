from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv("OPENAI_API_KEY")
if not key:
    raise ValueError("API key not found. Check your . file.")

client = OpenAI(api_key=key)

messages = []

def completion(message):
    messages.append({"role": "user", "content": message})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    reply = response.choices[0].message.content
    print("Jarvis:", reply)

    messages.append({"role": "assistant", "content": reply})

if __name__ == "__main__":
    print("Hi, I am Jarvis. How may I help you?")
    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Jarvis: Goodbye! 👋")
            break

        completion(user_input)

