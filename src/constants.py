"""
created by Nagaj at 19/04/2021
"""

# ############  options ####################

ACCEPT = "y"
CLOSE = "x"
LIST = "l"
ADD = "a"

ACTION_OPTIONS = ("a", "l", "x")
ACCEPT_REFUSE_OPTIONS = ("y", "n")

# ##############  messages ################

OPENING_MSG = "Enter Your Command a[add], l[list], x[close]"
ENTER_TEXT = "Enter Your Text: "
NO_ITEMS_TO_SHOW = "No Items To Show"
HTML_MSG = "Do you want to export to html ? y[yes], n[no]"
JSON_MSG = "Do you want to export to json ? y[yes], n[no]"
INVALID__OPTION_COMMAND = (
    "Invalid <{command}> Enter Your Command a[add], l[list], x[close]"
)
INVALID_ACCEPT_REFUSE_COMMAND = "Invalid <{command}> Enter Your Command y[yes], n[no]"
BYE = "Done. Goodbye"

# #############  break lines ################

BREAK_LINE = "#" * 50 + "\n"


# #######   saving msgs  ####################
SAVING = "saving text to '{fullpath}'"
