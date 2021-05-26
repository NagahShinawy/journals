"""
created by Nagaj at 18/04/2021
"""
from src.constants import (
    INVALID__OPTION_COMMAND,
    INVALID_ACCEPT_REFUSE_COMMAND,
    ACTION_OPTIONS,
    ACCEPT_REFUSE_OPTIONS,
)


class CMD:
    """
        user command line actions
    """

    COMMANDS = ACTION_OPTIONS

    def __init__(self, command):
        self.command = self.set_command(command)

    def set_command(self, command):
        """

        :param command:
        :return:
        """
        while command not in self.COMMANDS:
            command = input(INVALID__OPTION_COMMAND.format(command=command))
        return command

    def __eq__(self, other):
        """

        :param other:
        :return:
        """
        return self.command == other


class AcceptOrRefuse(CMD):  # pylint: disable=R0903
    """
        user accept or refuse
    """

    COMMANDS = ACCEPT_REFUSE_OPTIONS

    def set_command(self, command):
        """

        :param command:
        :return:
        """
        while command not in self.COMMANDS:
            command = input(INVALID_ACCEPT_REFUSE_COMMAND.format(command=command))
        return command
