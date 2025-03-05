import chainlit as cl
from dotenv import load_dotenv
import os
from utils.speech_utils import recognize_speech
from utils.ai_utils import ai_response
from utils.youtube_utils import play_youtube

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

@cl.on_chat_start
async def start_chat():
    actions = [
        cl.Action(name="voice_input", value="voice_input", label="🎤 Speak", payload={"type": "voice_input"})
    ]
    await cl.Message(content="Click the button below to speak or type your query:", actions=actions).send()

@cl.action_callback("voice_input")
async def on_voice_input(action: cl.Action):
    transcribed_text = recognize_speech()

    await cl.Message(content=transcribed_text, author="User").send()
    await process_input(transcribed_text)

@cl.on_message
async def main(message: cl.Message):
    user_input = message.content.lower()
    await process_input(user_input)

async def process_input(user_input):
    if "play" in user_input:
        query = user_input.replace("play", "").strip()
        response_text = play_youtube(query)
    elif "listen" in user_input:
        response_text = recognize_speech()
    else:
        response_text = ai_response(user_input)

    await cl.Message(content=response_text).send()

if __name__ == "__main__":
    cl.run()