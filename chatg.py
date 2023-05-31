import openai
import time
openai.api_key = "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"

def generate_response(prompt):
    response = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=1000, n=1,stop=None,temperature=0.5)
    message = response.choices[0].text
    return message.strip()

while True:
    user_input = input("你： ")
    prompt = "ChatGPT: " + user_input + "\nUser: "
    chat_bot_response = generate_response(prompt)
    print("ChatGPT: " + chat_bot_response)

