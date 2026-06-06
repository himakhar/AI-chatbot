import os
from dotenv import load_dotenv
import openai

# Load .env file (if present) and use environment variable for API key.
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_gpt(prompt):
      response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
      )
      return response['choices'][0]['message']['content'].strip()


if __name__ == "__main__":
      try:
            while True:
                  user_input = input("You: ")
                  if user_input.lower() in ["quit", "exit", "bye"]:
                        break
                  if not openai.api_key:
                        print("Chatbot: API key not set. Set OPENAI_API_KEY to use the API.")
                        continue
                  response = chat_with_gpt(user_input)
                  print("Chatbot:", response)
      except KeyboardInterrupt:
            print("\nExiting.")
