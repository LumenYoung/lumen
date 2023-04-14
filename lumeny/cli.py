# cli.py
import os
import questionary as q
import click
from prompt_toolkit.lexers import PygmentsLexer
from lumeny.utils import InputLexer
# from lumen.tui import launch_tui
from lumeny.calendar import generate_command_with_gpt4


@click.group()
def cli():
    pass

@click.command()
def add():
    """Interactively add events to your calendar. 
    """

    def add_one_event() -> None:
        request: str = q.text("What you will do (enter to abort): ", qmark="",
                              lexer=PygmentsLexer(InputLexer)).ask()

        if request == "":
            return
        
        command = generate_command_with_gpt4(request)
        if q.confirm(f"Execute: {command}", qmark="?").ask():
            try:
                os.system(command)
                # print in green: command executed
                print(f"\033[1;32mEvent Added!\033[0m")
            except Exception as e:
                print(e)
                print("Error executing command")
    
    while True:
        add_one_event()
        if not q.confirm("Add another event?", qmark="").ask():
            break
    

@click.command()
@click.argument("input", nargs=-1)
def will(input):
    """
    Add events to the calendar. Accept any number of arguments and treat them as one string.
    """

    # If no argument is passed, show the help screen
    # If input arguments are passed, concatenate them to form a single string
    input_str = " ".join(input)
    command: str = generate_command_with_gpt4(input_str)

    if q.confirm(f"Execute: {command}", qmark="?").ask():
        try:
            os.system(command)
            print(f"\033[1;32mEvent Added!\033[0m")
        except Exception as e:
            print(e)
            print("Error executing command")


@click.command()
def show():
    """
    Launch the Text User Interface (TUI).
    """
    print("Show")

    # launch_tui()


cli.add_command(will)
cli.add_command(show)
cli.add_command(add)

if __name__ == "__main__":
    cli()
