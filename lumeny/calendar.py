"""Define the commands that generate commands correspoends to the calendar manipulation"""

from typing import Dict, List
import datetime

from datetime import datetime, timedelta

from lumeny.ai_utils import chat_with_gpt, create_system_msg, create_user_msg


def repeat_learn(the_topic: str, repeat_days: List[int], start_day: int = 0) -> str:
    """
    the functions to create an event that follows the forgetting curves.
    The default is to repeat at 2, 5, 14, 30 days after.

    :param the_topic: What event it is
    :param repeat_days: the scheme to repeat an tpoic
    :param start_date int: the date you viewed/learnt this topic, relative to today. Default is 0
    :return: the command
    """

    if repeat_days is None:
        repeat_days = [2, 5, 14, 30]

    today: datetime = datetime.today()

    start_date: datetime = today - timedelta(days=start_day)

    repeat_dates: List[datetime] = [
        start_date + timedelta(days=day) for day in repeat_days
    ]

    repeat_commands: str = ""

    for i, day in enumerate(repeat_dates):
        date_str: str = day.strftime("%d.%m.%Y")
        repeat_commands += f"khal new -a personal {date_str} {date_str} {the_topic} :: {the_topic} for the {i+1}th time ; "

    return repeat_commands


def generate_command_with_gpt4(the_instruction: str) -> str:
    """
    Generate a khal command to add an event to the calendar with the gpt4 model.

    :param instruction: The natural language instruction
    :return: the khal command
    """
    today = datetime.date.today()
    today = today.strftime("%d-%m-%Y")
    # get the weekday of today
    weekday = datetime.datetime.today().weekday()

    # weekdays
    weekdays = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    print(f"today is {today} {weekdays[weekday]}")

    prompt_content = f"""
    You are a Linux terminal that writes commands for the khal calendar program. 
    Output a command to add the event to the specified calendar ('personal' or 'daily') based on the provided description, use daily as default calendar.
    The event is 1 hour long if not specified. Use these flags when needed: -a for the calendar, -l for location(optional), -r for repeat (daily, weekly, monthly, yearly).
    provide time in hh:mm 24h format, provide date DD.MM.YYYY format. Syntax: khal new [-a CALENDAR] [OPTIONS] [START [END | DELTA] [TIMEZONE] SUMMARY [:: DESCRIPTION]].
    Provide one command without explanation or say 'error' for unclear inputs. today is {today}, {weekdays[weekday]}.
    """

    # get the date of today in the format DD-MM-YYYY
    custom_system_prompt: Dict[str, str] = create_system_msg(prompt_content)

    conversation: List[Dict] = [custom_system_prompt]
    user_message = create_user_msg(the_instruction)
    conversation.append(user_message)
    response = chat_with_gpt(conversation, model="gpt-4")
    return response


if __name__ == "__main__":
    repeat_learn("Learn the MMK chapter 1")
