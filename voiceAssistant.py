import os
from dotenv import load_dotenv

from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface
from elevenlabs.types import ConversationConfig

load_dotenv()

user_name = "Prachi"
schedule = "DSA lecture at 8:30, Physics lab at 13:00"
prompt = "You are a helpful assistant. Your interlocutor has the following schedule: " + schedule
first_message = "Hello " + user_name + ", how can I help you today?"

AGENT_ID = os.getenv("AGENT_ID")
API_KEY = os.getenv("API_KEY")


client = ElevenLabs(api_key=API_KEY)

def print_agent_response(response):
    print(f"Agent: {response}")

def print_interrupted_response(original, corrected):
    print(f"Agent interrupted, truncated response: {corrected}")

def print_user_transcript(transcript):
    print(f"User: {transcript}")

# Create conversation session
conversation = Conversation(
    client,
    AGENT_ID,
    requires_auth=True,
    audio_interface=DefaultAudioInterface(),
    callback_agent_response=print_agent_response,
    callback_agent_response_correction=print_interrupted_response,
    callback_user_transcript=print_user_transcript,
)

# Start the real-time voice session
conversation.start_session()