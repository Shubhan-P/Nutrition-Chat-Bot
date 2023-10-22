import openai
import os


openai.api_key ="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"



user_input = input("any qestions about your nutritonal health? \n")
# Define the system message
system_msg = 'You are a helpful assistant who is a nutrition expert.'

# Define the user message
user_msg = 'This is a nutrition chatbot that will guide you through any questions or concerns you have with certain foods or what to eat and when or when you should excersice'

# Create a dataset using GPT
response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                        messages=[{"role": "system", "content": system_msg},
                                         {"role": "user", "content": user_input}])
print(response["choices"][0]["message"]["content"])





