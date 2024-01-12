import requests
import time
import json
import os
import re
from dotenv import load_dotenv

load_dotenv()

BOT_ID = os.getenv("BOT_ID")
GROUP_ID = os.getenv("GROUP_ID")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
USER_ID = os.getenv("USER_ID")
LAST_MESSAGE_ID = None


def send_message(text="", attachments=None):
    """Send a message to the group using the bot."""
    post_url = "https://api.groupme.com/v3/bots/post"
    data = {"bot_id": BOT_ID, "text": text, "attachments": attachments or []}

    response = requests.post(post_url, json=data)
    return response.status_code == 202


def get_group_messages(since_id=None):
    params = {"token": ACCESS_TOKEN}
    if since_id:
        params["since_id"] = since_id

    get_url = f"https://api.groupme.com/v3/groups/{GROUP_ID}/messages"
    response = requests.get(get_url, params=params)
    if response.status_code == 200:
        # this shows how to use the .get() method to get specifically the messages but there is more you can do (hint: sample.json)
        return response.json().get("response", {}).get("messages", [])
    return []


def process_message(message):
    """Process and respond to a message."""
    global LAST_MESSAGE_ID
    text = message["text"].lower()
    sender = message["sender_type"]
    user_id = message["sender_id"]

    if user_id == USER_ID:
        # i.e. responding to a specific message (note that this checks if "hello bot" is anywhere in the message, not just the beginning)
        if "hello bot" in text:
            send_message("sup")

        if "do math" in text:

            expression = text[len("Do math"):].strip()
            print(f"Evaluating expression: {expression}")

            result = eval(expression)
            send_message(f"SOLUTION: {result}")

    if sender != "bot":
        if "good morning" in text:
            send_message("Have a terrific morning KITTEN!!")
        if "good night" in text:
            send_message("Get some good sleep Kitten!")

    LAST_MESSAGE_ID = message["id"]


def main():
    global LAST_MESSAGE_ID

    group_message = get_group_messages()
    recent_message = None

    if group_message and len(group_message) > 0:
        recent_message = group_message[0]['id']

    # this is an infinite loop that will try to read (potentially) new messages every 10 seconds, but you can change this to run only once or whatever you want
    while True:
        messages = get_group_messages(recent_message)
        # print("MESSAGES")
        # print(messages)
        if messages:
            for message in reversed(messages):
                process_message(message)

            recent_message = messages[0]['id']
        time.sleep(10)


if __name__ == "__main__":
    main()
