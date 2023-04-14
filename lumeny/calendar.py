"""Define the commands that generate commands correspoends to the calendar manipulation"""

from typing import Dict, List
import datetime

from lumeny.ai import chat, create_system_msg, create_user_msg


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
    response = chat(conversation, model="gpt-4")
    return response


# def is_period_of_time(instruct: str) -> str:
#     prompt_content: str = "Your task is to classify a sentence. You will receive a sentence that contains a reference to either a specific time point or a time interval. Determine if it is a time interval mentioned in the sentence, e.g. 'for 1 hour' 'for 20 mins' 'half an hour' '2 hours' are time intervals. Simply reply 'yes' or 'no' without further explanation."
#     sys_msg = create_system_msg(prompt_content)

#     example_1 = [
#         {"role": "user", "content": "Write thesis for 2 hours at 10pm"},
#         {"role": "assistant", "content": "yes"},
#     ]

#     example_2 = [
#         {"role": "user", "content": "Ride bike tomorrow at 8pm for 1 hour"},
#         {"role": "assistant", "content": "no"},
#     ]

#     example_3 = [
#         {"role": "user", "content": "2 hours writing thesis at 10 pm tomorrow"},
#         {"role": "assistant", "content": "yes"},
#     ]

#     conversation: List[Dict] = [sys_msg]

#     conversation.extend(example_1)
#     conversation.extend(example_2)
#     conversation.extend(example_3)

#     conversation.extend(example_3)

#     user_message = create_user_msg(instruct)
#     conversation.append(user_message)

#     response = chat(conversation, model="gpt-3.5-turbo", temperature=0)

#     return response == "yes"


# TODO add a command to extract time related information from the command


# def extract_time_related_information(the_instruction: str) -> str:
#     """Extract the time related information from the command.

#     :param command: the command
#     :return: the time related information
#     """

#     prompt = """
#      TODO
#     """

#     return prompt


# def test_is_period_of_time(instructions: List, answers: List) -> None:
#     for ans, instruction in zip(answers, list_of_instructions):
#         if is_period_of_time(instruction):
#             if ans == "True":
#                 print("correct, true")
#             else:
#                 print("error with the instruction", instruction)
#         else:
#             if ans == "False":
#                 print("correct, false")
#             else:
#                 print("error with the instruction", instruction)


if __name__ == "__main__":

    list_of_instructions = [
        "Ride bike tomorrow at 8pm for 1 hour",
        "Write thesis for 2 hours at 10pm",
        "meeting with lina next wednesday at 11:30",
        "Learn python for 2 hours in three weeks at 7pm",
        "Go to gym at 7pm",
        "Meditation at 1am",
        "A one hour meeting at 7",
    ]

    answers = ["True", "True", "False", "True", "False", "False", "True"]

    for instruction in list_of_instructions:
        command = generate_command_with_gpt4(instruction)

        print(command)

    # print(generate_command_with_gpt4( "Learn python for 2 hours in three weeks at 7pm"))
    # print(generate_command_with_gpt4("meeting with lina next wednesday at 11:30"))
