import os
from dotenv import load_dotenv

import openai
# Load environment variables from .env file
load_dotenv()

# select OpenAI model to use
OPEN_AI_MODEL = "gpt-3.5-turbo"
# app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

def make_api_json_format(string) -> dict:
    """Converts a string to JSON format expected by 
    the OpenAI API chat completion end-point"""
    return {"role": "user", "content": string}

class Character:
    """Class containing information attributes and methods for characters"""
    def __init__(self, name: str, speaking_to: str, topic: str):

        self.name = name
        self.topic = topic
        self.initial_prompt = make_api_json_format(self.get_initial_prompt(speaking_to))
        self.messages = [self.initial_prompt]

    def get_initial_prompt(self, speaking_to: str) -> str:
        """Returns initial message/prompt for the given character""" 
        return (
            f"Imagine you are {self.name} and you are speaking to {speaking_to} "
            f"about {self.topic}. Make sure to speak exactly in {self.name}'s tone of voice and character. Tell them your name "
            f"and keep your intro to one sentence."
        )
    
    def get_response(self):
        """Creates a response using the OpenAI ChatCompletion end-point
        and previous message history"""
        response = openai.ChatCompletion.create(
                    model=OPEN_AI_MODEL,
                    messages=self.messages
        ).choices[0].message.content
        return response

    def update_message_history(self, latest_message: str):
        """Based on latest chat response, update character's chat history"""
        self.messages.append(make_api_json_format(latest_message))