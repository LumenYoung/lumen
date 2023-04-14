import openai
import os
from typing import Dict, List
import datetime
from lumeny.ConfigLoader import ConfigLoader

# Set your API key from environment variables
config = ConfigLoader().get_config()
openai.api_key = config["openai"]["api"]

# Function to interact with the chatcompletion API


def chat(conversation, model="gpt-4", temperature:float =0.1):

    response = openai.ChatCompletion.create(
        model=model, messages=conversation, temperature=temperature)

    return response["choices"][0]["message"]["content"]


def create_system_msg(prompt: str) -> Dict[str, str]:
    return {
        "role": "system",
        "content": prompt
    }


def create_user_msg(prompt: str) -> Dict[str, str]:
    return {
        "role": "user",
        "content": prompt
    }


def create_ai_msg(prompt: str) -> Dict[str, str]:
    return {
        "role": "assistant",
        "content": prompt
    }


# Example usage
if __name__ == "__main__":

    today = datetime.date.today()

    today = today.strftime("%d-%m-%Y")
    # get the weekday of today
    weekday = datetime.datetime.today().weekday()

    # weekdays
    weekdays = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]

    prompt_content = f"You are a Linux terminal that writes commands for the khal calendar program. Output a command to add the event to the specified calendar ('personal' or 'daily') based on the provided description, use daily as default calendar. Use these flags when needed: -a for the calendar, -l for location(optional), -r for repeat (daily, weekly, monthly, yearly). Infer a reasonable time unless instructed otherwise, provide time in hh:mm 24h format, provide date DD.MM.YYYY format. Syntax: khal new [-a CALENDAR] [OPTIONS] [START [END | DELTA] [TIMEZONE] SUMMARY [:: DESCRIPTION]]. Provide one command without explanation or say 'error' for unclear inputs. today is {today}, {weekdays[weekday]}"

    print(today)
    print(weekday)

    # get the date of today in the format DD-MM-YYYY

    custom_system_prompt: Dict[str, str] = create_system_msg(prompt_content)

    print("To quit the conversation, type exit.")

    conversation: List[Dict] = [custom_system_prompt]
    user_message = create_user_msg(input("User: "))
    conversation.append(user_message)

    response = chat(conversation)
    print(response)
