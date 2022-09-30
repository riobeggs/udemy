import colorgram
import random
import turtle as turtle_module


class Colours:
    def __init__(self) -> None:
        self.rgb_colours = None

    def extract_colours(self) -> list:
        self.rgb_colours = []
        colours = colorgram.extract(
            "/Users/riobeggs/Downloads/georgios-domouchtsidis-CIMx-ymiuiI-unsplash.jpg",
            30,
        )
        for colour in colours:
            r = colour.rgb.r
            g = colour.rgb.g
            b = colour.rgb.b
            new_colour = (r, g, b)
            self.rgb_colours.append(new_colour)

        return self.rgb_colours


class Painting:
    def __init__(self) -> None:
        self.paint = turtle_module.Turtle()

    def paint_settings(self) -> None:
        turtle_module.colormode(255)
        self.paint.penup()
        self.paint.hideturtle()
        self.paint.speed("fastest")
        self.paint.setheading(225)
        self.paint.forward(300)
        self.paint.setheading(0)

    def paint_dots(self, colours) -> None:
        Painting().paint_settings()
        self.paint.penup()
        self.paint.hideturtle()
        for _ in range(10):
            for _ in range(10):
                self.paint.dot(20, random.choice(colours))
                self.paint.forward(50)
            self.paint.setheading(90)
            self.paint.forward(50)
            self.paint.setheading(180)
            self.paint.forward(500)
            self.paint.setheading(0)


def main() -> None:
    colours = Colours().extract_colours()

    Painting().paint_dots(colours)

    screen = turtle_module.Screen()
    screen.exitonclick()


if __name__ == "__main__":
    main()
