"""
This is a module that 1) parse the input markdown file into paragraph and store them as dictionary, we also parse each line as a task, which is stored in the dictionary 2) pick a random task from the dictionary and return it as a string given specific category (which section)
"""

import logging
import re
from typing import Dict, List
from config_loader import ConfigLoader
import random

logging.basicConfig(filename="testing.log", encoding="utf-8", level=logging.DEBUG)


def parse_markdown(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    sections = {}
    current_section = None
    in_front_matter = False
    in_settings = False

    for line in lines:
        line = line.strip()
        if line == "---":  # front matter starts or ends
            in_front_matter = not in_front_matter
        elif line.startswith("%% kanban:settings"):  # settings starts
            in_settings = True
        elif not in_front_matter and not in_settings:
            if line.startswith("## "):  # new section starts
                section_name = line[3:]
                sections[section_name] = []
                current_section = section_name
            elif current_section is not None and line:  # line in current section
                sections[current_section].append(line)

    return sections


def output_task(task: str) -> None:
    task: Dict = parse_line(task)

    print(
        "Hi, we got a task for you: \n",
        f"Task: \n \t {task['task']}\n",
        f"Current decomposition: \n \t {task['steps']}\n",
        "Lets get started!",
    )


def parse_line(line: str) -> Dict:
    # Replace consecutive <br> with a single one
    line = re.sub(r"(<br>)+", "<br>", line)

    # Split by <br>
    parts = line.split("<br>")

    # Parse main task
    main_task_match = re.search(r"- \[.\] (.+)(:)?", parts[0])
    if main_task_match:
        main_task = main_task_match.group(1)
    else:
        main_task = ""

    # Parse subtasks
    steps = []
    for part in parts[1:]:
        task_match = re.search(r"- \[(.)\] (.+)", part)
        if task_match:
            status, task = task_match.groups()
            if status.lower() == "x":
                task = "(done) " + task
            steps.append(task)

    # Return result
    return {"task": main_task, "steps": steps}


def available_sections() -> List[str]:
    config_loader = ConfigLoader()
    config = config_loader.get_config()

    return list(config["task_list"]["sections"].keys())


# random task picker
def pick_random_task(
    file: Dict,
    config: Dict,
    section: str = None,
) -> str:
    markdown_sections = config["task_list"]["sections"]

    section_names = [
        markdown_sections[section_code]["section_name"]
        for section_code in markdown_sections
    ]

    if section is None:
        # choose a random section
        section = random.choice(section_names)
    elif section not in section_names:
        raise ValueError(f"Section {section} not found.")

    tasks: List = file[section]

    # choose a random paragraph
    task: str = random.choice(tasks)

    return task


def random_task_picker(section_code: str = None):
    config_loader = ConfigLoader()
    config = config_loader.get_config()

    # translate section_code to section name

    file = config["task_list"]["file"]
    file = parse_markdown(file)

    section_chosen: str = config["task_list"]["sections"][section_code]["section_name"] if section_code is not None else None

    task = pick_random_task(file, config, section_chosen)

    output_task(task)


if __name__ == "__main__":
    config_loader = ConfigLoader()
    config = config_loader.get_config()

    print(available_sections())
