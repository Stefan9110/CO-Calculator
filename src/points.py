GPA_POINTS = 10000
MAX_POINTS = 17000
PASS_POINTS = 5500


def round_grade(grade):
    base = int(grade)
    decimal = grade - base

    if decimal < 0.25:
        return base
    elif 0.25 <= decimal < 0.75:
        return base + 0.5
    else:
        return base + 1


# GPA is rounded to the nearest 0.5 point (e.g. 9.25 -> 9.5, 9.75 -> 10)
# GPA is rounded down if the decimal is less than 0.25 (e.g. 9.24 -> 9, 9.74 -> 9.5)
# GPA is rounded up if the decimal is greater than or equal to 0.75 (e.g. 9.75 -> 10)
# Max GPA is 10
def gpa_points(points):
    if points < 0:
        raise ValueError("Points cannot be negative")

    grade = min(points / GPA_POINTS * 10, 10)
    return round_grade(grade)


# Returns the number of points required to obtain the given GPA
# GPA is rounded to the nearest 0.5 point (e.g. 9.25 -> 9.5, 9.75 -> 10)
# Therefore, you might need to obtain fewer points than the GPA would suggest
def required_points_for_gpa(gpa):
    if gpa < 0:
        raise ValueError("GPA cannot be negative")

    gpa = max(round_grade(gpa) - 0.25, 0)

    points = (gpa / 10) * GPA_POINTS
    return int(points)


def points_as_percentage(points):
    return round((points / MAX_POINTS) * 100, 2)
