from termcolor import colored

from src.points import points_as_percentage, gpa_points, PASS_POINTS, GPA_POINTS


def welcome_message():
    TITLE = "COMPUTER ORGANIZATION POINTS\nVU AMSTERDAM 2024"
    SEPARATOR = "=" * 50
    OVERVIEW = "=" * 20 + " OVERVIEW " + "=" * 20

    message = [SEPARATOR, TITLE, SEPARATOR, "\n", OVERVIEW, points_message(), SEPARATOR]
    colors = ["red", "magenta", "red", "none", "red", "none", "red"]

    for line, color in zip(message, colors):
        if color == "none":
            print(line)
        else:
            print(colored(line, color))


def points_message():
    points = 10000
    point_col = points_color(points)
    gpa = gpa_points(points)
    percentage_points = points_as_percentage(points)

    message = (f"🎯 You currently have {colored(points, point_col)} points.\n"
               f"🎓 Your current grade is {colored(str(gpa) + ' GPA', gpa_color(gpa))}.\n"
               f"💯 You have obtained {colored(str(percentage_points) + '%', point_col)} of the total "
               f"points.\n")

    if points < PASS_POINTS:
        message += (
            f"\n❌ You have {colored('not', 'red')} passed yet. You need {colored(str(PASS_POINTS - points), 'red')} more points to "
            f"pass.")
    else:  # TODO: add check for exam
        message += f"\n✅ You have {colored('passed', 'green')}, assuming you passed the exam."

    return message


def points_color(points):
    if points < PASS_POINTS:
        return "red"
    elif points < GPA_POINTS:
        return "yellow"
    else:
        return "green"


def gpa_color(gpa):
    if gpa < 5.5:
        return "red"
    elif gpa < 8:
        return "yellow"
    else:
        return "green"
