import os
from dotenv import load_dotenv

load_dotenv()

import google.generativeai as genai

api_key = os.getenv("GEMINI_API")
genai.configure(api_key=api_key)

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

topic = input("Enter the topic you want to learn: ")
time = input("Enter how much days, weeks or months you have, and how much hours you can dedicate per day: ")
level = input("Enter your prior experience in this domain: ")
addComm = input("Any additional comments?: ")

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

prompt = f"""You are a excellent in the {topic}. Now a person wants to learn the same topic in {time}.
        He/She has {level} level of knowledge in the field. Now generate a roadmap with references and tags (tags must be related to the topic) for the person.
        Show topics in details and all tags should start with '#' only and in an array format, Like [#john, #doe].
        If the time is too low (like in minutes or seconds, then reply appropriately (No if not possible))."""

if(addComm):
    prompt = prompt + "Additional Notes by user: " + addComm

print(prompt)

prompt_parts = [
  prompt
]

response = model.generate_content(prompt_parts)
print(response.text)