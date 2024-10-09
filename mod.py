from deep_translator import GoogleTranslator
from langdetect import detect, detect_langs, DetectorFactory


def read_file(filename: str):
    with open(filename, "r") as file:
        lang = file.readline()
        triangle_sides = file.readline().split(":")[-1].split(" ")
        triangle_sides.remove(triangle_sides[0])
        if len(triangle_sides) != 3:
            raise
        return lang, triangle_sides


def is_triangle_exists(triangle: list) -> bool:
    triangle_sides = triangle.copy()

    max_side = max(triangle_sides)
    triangle_sides.remove(max_side)

    side1 = int(triangle_sides[0])
    side2 = int(triangle_sides[1])
    if int(max_side) < side1 + side2:
        return True
    return False


def is_triangle_right(triangle: list) -> bool:
    triangle_sides = triangle.copy()

    max_side = max(triangle_sides)
    triangle_sides.remove(max_side)

    side1 = int(triangle_sides[0])
    side2 = int(triangle_sides[1])

    if side1**2 + side2**2 == int(max_side) ** 2:
        return True
    return False


def translate(text, dest):
    try:
        translation = []
        for string in text:
            translation.append(
                GoogleTranslator(source="auto", target=dest).translate(string)
            )
        return translation
    except Exception as e:
        return f"Error during translation: {e}"
