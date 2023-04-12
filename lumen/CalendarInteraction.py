from lumen.ai import chat, create_system_msg, create_user_msg, create_ai_msg
import datetime
import os
from typing import Dict, List


def generate_command_with_gpt4(instruction: str) -> str:

    today = datetime.date.today()
    today = today.strftime("%d-%m-%Y")
    # get the weekday of today
    weekday = datetime.datetime.today().weekday()
    
    # weekdays
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    prompt_content = f"You are a Linux terminal that writes commands for the khal calendar program. Output a command to add the event to the specified calendar ('personal' or 'daily') based on the provided description, use daily as default calendar. Use these flags when needed: -a for the calendar, -l for location(optional), -r for repeat (daily, weekly, monthly, yearly). Infer a reasonable time unless instructed otherwise, provide time in hh:mm 24h format, provide date DD.MM.YYYY format. Syntax: khal new [-a CALENDAR] [OPTIONS] [START [END | DELTA] [TIMEZONE] SUMMARY [:: DESCRIPTION]]. Provide one command without explanation or say 'error' for unclear inputs. today is {today}, {weekdays[weekday]}"
    
    # get the date of today in the format DD-MM-YYYY
    custom_system_prompt: Dict[str, str] = create_system_msg(prompt_content)

    conversation: List[Dict] = [custom_system_prompt]
    user_message=create_user_msg(instruction)
    conversation.append(user_message)
    response=chat(conversation, model="gpt-4")
    return response


# generate time and date with gpt3

def generate_time_with_gpt3(instruction: str) -> str:

    today = datetime.date.today()
    today = today.strftime("%d-%m-%Y")
    # get the weekday of today
    weekday = datetime.datetime.today().weekday()
    # weekdays
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    prompt_content = f"You will be given a instruction. Capture the time mentioned in the instruction. You should return only the time in the format hh:mm. If the prompt contains a duration of time, return hh:mm hh:mm for the start time and end time. today is {today}, {weekdays[weekday]}. You should only reply the time without any explaination"
    # get the date of today in the format DD-MM-YYYY
    custom_system_prompt: Dict[str, str] = create_system_msg(prompt_content)
    
    example_1 = [{"role": "user", "content": "Ride bike tomorrow at 8pm for 1 hour"}, {"role": "assistant", "content": "20:00 21:00"}]

    example_2 = [{"role": "user", "content": "Write thesis for 2 hours at 10pm"}, {"role": "assistant", "content": "22:00"}]
    
    conversation: List[Dict] = [custom_system_prompt]
    conversation.append(example_1[0])
    conversation.append(example_1[1])
    conversation.append(example_2[0])
    conversation.append(example_2[1])

    user_message=create_user_msg(instruction)
    conversation.append(user_message)
    response=chat(conversation, model="gpt-3.5-turbo")
    return response

if __name__ == "__main__":
    print(generate_time_with_gpt3("Learn python for 2 hours in three weeks at 7pm"))
    print(generate_time_with_gpt3("meeting with lina at 7am"))

    print(generate_command_with_gpt4("Learn python for 2 hours in three weeks at 7pm"))
    print(generate_command_with_gpt4("meeting with lina next wednesday at 11:30"))