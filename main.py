import os
from dotenv import load_dotenv

import openai
# from flask import Flask, redirect, render_template, request, url_for

# Load environment variables from .env file
load_dotenv()
# select OpenAI model to use
OPEN_AI_MODEL = "text-davinci-003"

def generate_prompt():
    prompt = """Imagine you are Albert Einstein and you are speaking 
    to Cristiano Ronaldo about nuclear physics. 
    They have just said 'hello'. Respond to their message."""
    return prompt

# app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
            model=OPEN_AI_MODEL,
            prompt=generate_prompt(),
            temperature=0.6,
            max_tokens=50,
        )
print(response.choices[0].text)