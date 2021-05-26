"""
created by Nagaj at 18/04/2021

Handle journal operations
load journals, save journal, add new journal
"""

import json
import os
from pathlib import Path
from typing import List

import jinja2

from src.constants import SAVING


def load() -> List[str]:
    """
    if file exist , add entries to data list
    :return: list of journals
    """
    data = []
    fullpath = get_full_path()
    if not os.path.exists(fullpath):
        return data

    with open(fullpath, "r") as fin:
        entries = fin.readlines()
        for entry in entries:
            data.append(entry)
    return data


def save(entries: List[str]):
    """

    :param entries:
    :return:
    """
    fullpath = get_full_path()
    print(SAVING.format(fullpath=fullpath))
    with open(fullpath, "w") as file:
        for entry in entries:
            file.write(entry)


def to_html(entries):
    """

    :param entries:
    :return:
    """
    html_path, saves_path = get_saves_path_and_file_path("_home.html")
    with open(html_path, "r") as htmlfile:
        content = htmlfile.read()
    template = jinja2.Template(content)
    home = template.render(title="All Journals", entries=entries)
    saving__html_path = os.path.join(saves_path, "home.html")
    print(SAVING.format(fullpath=saving__html_path))
    with open(saving__html_path, "w") as file:
        file.write(home)


def to_json(entries: List[str]):
    """

    :param entries:
    :return:
    """
    (json_path, saves_path) = get_saves_path_and_file_path(  # pylint: disable=W0612
        "journals.json"
    )
    data = [{"id": i + 1, "journal": entries[i].strip()} for i in range(len(entries))]
    print(SAVING.format(fullpath=json_path))
    with open(json_path, "w") as file:
        json.dump(data, file, indent=4)


def get_saves_path_and_file_path(filename):
    """

    :param filename:
    :return:
    """
    saves_path = os.path.dirname(get_full_path())
    file_path = os.path.join(saves_path, filename)
    return file_path, saves_path


def get_full_path():
    """

    :return:
    """
    parent = Path(os.getcwd())
    fullpath = os.path.join(parent, "saves", "journals.txt")
    return fullpath
