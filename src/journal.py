"""
created by Nagaj at 18/04/2021
"""


class Journal:  # pylint: disable=R0903
    """
    create new journal
    """

    entries = []

    def __init__(self, text: str):
        self.text = text

    def __str__(self):
        return self.text
