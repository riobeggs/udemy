# Constants
QUESTION_DATA = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {
        "text": "Approximately one quarter of human bones are in the feet.",
        "answer": "True",
    },
    {
        "text": "The total surface area of a human lungs is the size of a football pitch.",
        "answer": "True",
    },
    {
        "text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.",
        "answer": "True",
    },
    {
        "text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.",
        "answer": "False",
    },
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {
        "text": "No piece of square dry paper can be folded in half more than 7 times.",
        "answer": "False",
    },
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"},
]


class Question:
    def __init__(self, text, answer, question_number, score) -> None:
        self.text = text
        self.answer = answer
        self.question_number = question_number
        self.score = score

    def get_users_answer(self) -> str:
        valid_answers = ("true", "false")
        users_answer = None

        while users_answer not in valid_answers:
            users_answer = input(
                f"Q.{self.question_number}: {self.text} (True/False): "
            ).lower()

        if self.answer == users_answer.capitalize():
            self.score += 1
            print("You got it right!")
            print(f"The correct answer was: {self.answer}.")
            print(f"Your current score is: {self.score}/{self.question_number}.")


def main() -> None:
    question_number = 0
    score = 0

    for question in QUESTION_DATA:
        question_number += 1
        text = question["text"]
        answer = question["answer"]

        Question(text, answer, question_number, score).get_users_answer()


if __name__ == "__main__":
    main()
