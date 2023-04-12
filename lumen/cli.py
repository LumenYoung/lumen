# cli.py
import click
from lumen.tui import launch_tui


@click.group(invoke_without_command=True)
@click.pass_context
@click.argument("input", nargs=-1)
def main(ctx, input):
    """
    Accept any number of arguments and treat them as one string.
    """

    # If no argument is passed, show the help screen
    if not input and not ctx.invoked_subcommand:
        click.echo(ctx.get_help())
    else:
        # If input arguments are passed, concatenate them to form a single string
        input_str = " ".join(input)
        click.echo(f"Input string: {input_str}")


@main.command("show")
def show():
    """
    Launch the Text User Interface (TUI).
    """

    launch_tui()


if __name__ == "__main__":
    main()