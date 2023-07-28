import os
import timeit
from pygments.lexer import RegexLexer
from pygments.token import Text, Comment


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


def main():
    notify("test", "test")


if __name__ == "__main__":
    main()
