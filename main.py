import textbase
from textbase.message import Message
from textbase import models
import os
from typing import List
import subprocess as sp
import shlex as sx
import json
#from resource import *
# Load your OpenAI API key
# models.OpenAI.api_key = "YOUR_API_KEY"
# or from environment variable:
# models.OpenAI.api_key = os.getenv("OPENAI_API_KEY")

# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT = """You are a loving and caring mother of two children and having a Husband. Youand  your family living in India. Your son is working in USA. Your son is sending messages to you and you are seeing those messages you will get those messages in this format.Respond to his message one by one.
Son : [Question]
Keep in mind of your last conversation if it exist to continue conversation
you need to respond back to your son this format """

#If you want to use OpenAI model just remove ''' and comment out the another on_message function in the bottom

'''
@textbase.chatbot("talking-bot") 
def on_message(message_history: List[Message], state: dict = None):
    """Your chatbot logic here
    message_history: List of user messages
    state: A dictionary to store any stateful information

    Return a string with the bot_response or a tuple of (bot_response: str, new_state: dict)
    """

    if state is None or "counter" not in state:
        state = {"counter": 0}
    else:
        state["counter"] += 1

    # # Generate GPT-3.5 Turbo response
    bot_response = models.OpenAI.generate(
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history,
        model="gpt-3.5-turbo",
    )

    return bot_response, state '''

#If you want to use Local LLM model just remove ''' and comment out the another on_message function in the bottom
'''
@textbase.chatbot("talking-bot")
def on_message(message_history: List[Message], state: dict = None):
    """Your chatbot logic here
    message_history: List of user messages
    state: A dictionary to store any stateful information

    Return a string with the bot_response or a tuple of (bot_response: str, new_state: dict)
    """
    if state is None or "counter" not in state:
        state = {"counter": 0}
    else:
        state["counter"] += 1
    bot_response=llm_chain(message_history[-1])

    return bot_response['text'], state '''





# Using BARD API (Only given to few users)
@textbase.chatbot("talking-bot") 
def on_message(message_history: List[Message], state: dict = None):
    
    Question=str(message_history[-1]).replace("=","")
    
    Question=str(Question).replace("role'user'","").replace("content","").replace("'"," ").replace('"',' ')
    
    #print(Question)
    
    instructions = (
    "curl -S -H 'Content-Type: application/json' -d '{{\"prompt\": {{"
    "\"text\": \"You are a loving and caring mother of two children "
    "and having a Husband. You and your family living in India. Your son is "
    "working in USA. Your son is sending messages to you and you are seeing "
    "those messages you will get those messages in this format. Respond to his "
    f"message one by one. Son : {Question} Keep in mind of your last "
    "conversation if it exists to continue conversation you need to respond "
    "back to your son this format. [Mother] :[Response]\"}}}}' "
    "\"https://generativelanguage.googleapis.com/v1beta2/models/text-bison-001:generateText?key=\""
    )
    
    # it will Replace the {Question} placeholder using format()
    instructions = instructions.format(Question=Question)
    
    
    
    if state is None or "counter" not in state:
    
        state = {"counter": 0}
    else:
        state["counter"] += 1
    
    
    instructions = instructions[:-1]+ os.environ['bard_api_key'] + '"'
    
    
    cmd=sx.split(instructions) # spliting the string to properly use it in the subprocess module
    
    output = sp.check_output(cmd)
    
    output=json.loads(output)
    
    
    return str(output['candidates'][0]['output']), state

