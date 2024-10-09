import mod


def main():
    try:
        lang, triangle_sides = mod.read_file("MyData.txt")
        detected_lang = mod.detect(lang)
        text = [
            "Мова: ",
            "Трикутник зі сторонами: ",
            "існує.",
            "не існує.",
            "Трикутник є прямокутним",
            "Трикутник не є прямокутним",
            "Катет 1 = ",
            "Катет 2 = ",
            "Гіпотенуза = ",
        ]
        text = mod.translate(text, detected_lang)
        print(text[0] + detected_lang)

        if mod.is_triangle_exists(triangle_sides):
            print(
                text[1],
                triangle_sides[0],
                triangle_sides[1],
                triangle_sides[2],
                text[2],
            )

            if mod.is_triangle_right(triangle_sides):
                print(text[4])
                print(text[6] + triangle_sides[0])
                print(text[7] + triangle_sides[1])
                print(text[8] + triangle_sides[2])
            else:
                print(text[5])
        else:
            print(
                text[1],
                triangle_sides[0],
                triangle_sides[1],
                triangle_sides[2],
                text[3],
            )
    except Exception as e:
        print(f"Error reading file: {e}")
        print("Введіть сторони трикутника a, b, c: ")
        a = input("a = ")
        b = input("b = ")
        c = input("c = ")
        triangle_sides = [a, b, c]
        new_lang = input("Введіть мову інтерфейсу: ")
        new_text = [
            "Мова: ",
            "Трикутник зі сторонами: ",
            "існує.",
            "не існує.",
            "Трикутник є прямокутним",
            "Трикутник не є прямокутним",
            "Катет 1 = ",
            "Катет 2 = ",
            "Гіпотенуза = ",
        ]
        new_text = mod.translate(new_text, new_lang)
        result = new_text[0] + new_lang + "\n"

        if mod.is_triangle_exists(triangle_sides):
            result += (
                new_text[1]
                + triangle_sides[0]
                + triangle_sides[1]
                + triangle_sides[2]
                + new_text[2]
            )

            if mod.is_triangle_right(triangle_sides):
                result += (
                    new_text[4]
                    + "\n"
                    + new_text[6]
                    + triangle_sides[0]
                    + "\n"
                    + new_text[7]
                    + triangle_sides[1]
                    + "\n"
                    + new_text[8]
                    + triangle_sides[2]
                )

            else:
                result += new_text[5]
        else:
            result += (
                new_text[1]
                + triangle_sides[0]
                + triangle_sides[1]
                + triangle_sides[2]
                + new_text[3]
            )
        with open("MyData.txt", "w") as file:
            file.write(result)
            print('File "MyData.txt" is saved')


if __name__ == "__main__":
    main()
