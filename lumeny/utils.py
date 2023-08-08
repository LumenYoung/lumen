import os
import timeit
from pygments.lexer import RegexLexer
from pygments.token import Text, Comment
import openai
from typing import Dict, List


def notify(title: str, notification: str, icon: str = "arch") -> None:
    cmd = f"notify-send '{title}' '{notification}' --icon={icon}"
    os.system(cmd)


# write a decorator to time functions
def time_usage(func):
    def wrapper(*args, **kwargs):
        start = timeit.default_timer()
        result = func(*args, **kwargs)
        end = timeit.default_timer()
        # print in green: Time taken
        print(f"\033[1;32mTime usage: {end - start}\033[0m")
        return result

    return wrapper


class InputLexer(RegexLexer):
    tokens = {
        "root": [
            (r"[ ^(]`(.*?)`", Comment.Preproc),
            (r"^```(.*?$\n)?(.*?\n)+?^```$", Comment.Preproc),
            (r".+?", Text),
        ]
    }


def chat_with_gpt(
    the_conversation: List[Dict], model: str = "gpt-4", temperature: float = 0.1
):
    """

    The function to interact with the chatcompletion API

    :param the_conversation: conversation stored in list of dictionaries
    :param model: gpt3.5-turbo, gpt-4
    :param temperature: from 0 to 1, control the randomness of the response
    """

    response: Dict = openai.ChatCompletion.create(
        model=model, messages=the_conversation, temperature=temperature
    )

    return response["choices"][0]["message"]["content"]


def create_system_msg(prompt: str) -> Dict[str, str]:
    """
    Convert the prompt string to dictionary format

    :param prompt: The prompt for the system
    :return: Promt in dictionary format
    """
    return {"role": "system", "content": prompt}


def create_user_msg(prompt: str) -> Dict[str, str]:
    """

    Convert the user prompt string to dictionary format

    :param prompt: The prompt for the user
    :return: Promt in dictionary format
    """
    return {"role": "user", "content": prompt}


def create_ai_msg(prompt: str) -> Dict[str, str]:
    """

    Convert the ai prompt string to dictionary format

    :param prompt: The prompt for the ai
    :return: Promt in dictionary format
    """
    return {"role": "assistant", "content": prompt}


if __name__ == "__main__":
    main()
