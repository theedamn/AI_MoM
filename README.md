
# AI Mother

## Project Overview

The Motherly AI Chatbot is a conversational artificial intelligence designed to communicate with users in a warm and caring manner, emulating the speech style of a mother. The chatbot aims to provide a comforting and nurturing experience for users seeking support, information, or casual conversation.

The chatbot is integrated with SMS functionality, enabling users to interact with it through text messages. This integration allows users to access the chatbot's services conveniently from their mobile devices.

### It uses BARD API (Limited access) if you don't have it means use OpenAI API or GPT4All (Local LLM)



## Features

-    Motherly Tone: The chatbot uses language and responses that mimic the caring and compassionate style of a mother.

-   SMS Integration: Users can interact with the chatbot through SMS messages, making it accessible and user-friendly for those without internet access or who prefer text-based communication.

-  Contextual Understanding: The chatbot is designed to comprehend and retain context during conversations, enabling more natural and engaging interactions.

- Information Retrieval: The chatbot can provide useful information on a wide range of topics, such as general knowledge, advice, recipes, and more.

-   Emotional Support: The chatbot is programmed to offer empathetic responses and words of encouragement to users who express emotional distress.

- Customizable Responses: The chatbot's responses can be personalized and extended to suit specific use cases or user preferences.

## SMS Demo

![Alt Text](https://github.com/theedamn/AI_MoM/blob/main/SmS_Demo.gif)
## SMS Integration

The SMS integration allows users to communicate with the chatbot through text messages on their mobile phones. The process for interacting with the chatbot via SMS is as follows:

- Users send an SMS message to a designated phone number associated with the chatbot.

-   The chatbot receives the message and processes it to understand the user's intent.

-   The chatbot responds with a caring and informative message based on the user's input.

-  If the user's message requires further input or information, the chatbot engages in a conversational exchange until the user's query is resolved.

-   The chatbot can also send proactive messages to users if they have opted to receive notifications or reminders.
## Using Local Language Models

The Motherly AI Chatbot can also be configured to use local language models (LLMs) for improved performance and privacy. By using LLMs, the chatbot's responses can be generated locally without relying on external services, providing more control over data and reducing latency.

Some functions are commented they are

- OpenAI model usage function

- Local LLM function

if you want to give it a try remove the comment of the function and comment the current fucntion to use
## Dependencies and Deployment

Clone it first 

``` 
git clone https://github.com/theedamn/AI_MoM.git

cd AI_MoM

```

Run 

```
poetry install

```
To install all the Dependencies and additionally Run

```
pip install -r requirements.txt

```

Then Run this to host the server

```
poetry run python textbase/textbase_cli.py test main.py

```

In another terminal run 

``` 
python3 sms.py

```

This activates SMS integration







## Enviromental Variables

Run this in Bash

``` 
export my_num=  # your Twilio Register Number

export acc_ssid= # Your Twilio Register SSID 

export auth_token= # Your Twilio Auth Tokens

export bard_api_key= # Your BARD API

export OPENAI_API_KEY = # OpenAI API Key

```
## SMS_Integration Procedure

- You need a Twilio account 

- check the Twilio documentations for further info

- ngrok is need to port forward so that the sms can be received in local machine

- if ngrok twilio is done. Everything is good to go for sms SMS Integration
## Contributing

If you wish to contribute to the Motherly AI Chatbot project, follow these steps:

- Fork the project repository from GitHub.

- Create a new branch for your changes.

-  Make your changes and improvements to the code.

- Test your changes thoroughly to ensure they work as expected.

- Submit a pull request to merge your changes into the main project.

- Await feedback from the project maintainers and make any requested changes.

- Once approved, your contributions will be merged into the main project.