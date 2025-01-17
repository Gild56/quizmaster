"""
# Questions manager
The `questions_manager.pymodule only contains the `QuestionsManager`
class.

It takes questions, answers and images from databases and converts
it to be used in UI.
"""

import os
import pandas as pd
from random import randint, shuffle
from typing import final

from sources.logic.resource_path import resource_path
from kivy.logger import Logger as log

from sources.logic.text_manager import text_manager as txt
from sources.logic.settings_manager import settings_manager


@final
class QuestionsManager():
    """
    The `QuestionsManager` class reads databases, randomizes
    questions and returns the question, answers and image.

    It contains only one method - `rand_quest` which does
    all of this.

    It takes one argument : images_ordered which is bool.
    If it's true it'll assocate images with question, if it isn't,
    it'll take random images every time.
    """

    def __init__(self, images_ordered: bool | None = False) -> None:

        self.question = ""
        self.true_answer = ""
        self.wrong_answer1 = ""
        self.wrong_answer2 = ""
        self.wrong_answer3 = ""
        self.image = ""

        self.enough_images = True
        self.status = False
        self.current_language = ""
        self.images_ordered = images_ordered
        self.question_numbers = []

        self.csv_img = resource_path("resources/databases/images.csv")
        self.df_img = pd.read_csv(self.csv_img)
        self.quest_count_images = len(self.df_img) - 1

        self.csv_name = ""

    def _replace_ukrainian(
        self, text_input: str | None = "There's no text"
    ) -> str:
        """
        # Replace Ukrainian
        The `_replace_ukrainian` method is used to replace letters of
        the ukrainian alphabet which aren't supported by current
        fonts, by latin's (frech which have same letters, but
        supported by the fonts) or standad cyrillic (russian) letters.
        """

        text = text_input
        str(text_input)
        text = text.replace("ї", "ï").replace("і", "i")
        text = text.replace("Ї", "Ï").replace("І", "I")
        text = text.replace("Є", "Е").replace("є", "е")
        text = text.replace("Ґ", "г").replace("ґ", "г")
        return text

    def _change_the_language(self) -> None:
        """
        # Change The Language
        The `_change_the_language` method is used to change the database when
        `txt.language` changed.

        If nothing has changed it doesn't do anything.
        """

        self.csv_name = resource_path(
            f"resources/databases/{self.current_language}.csv"
        )

        self.df = pd.read_csv(self.csv_name)
        self.quest_count = len(self.df) - 1

        self.question_numbers = []

        for i in range(self.quest_count):
            self.question_numbers.append(i)

        self.question_numbers_randomized = \
            self.question_numbers.copy()

        shuffle(self.question_numbers_randomized)

        self.question_numbers = [-1] + self.question_numbers

    def _format_text(self, text_input, max_length) -> str:
        """
        # Format Text
        The `_format_text` method is used to cut a string into parts
        by words with a min lengh that's given in the 2nd argument:
        `max_lengh`.
        """

        text = str(text_input)

        text = self._replace_ukrainian(text)
        # Because fonts don't support ukrainian translation

        try:
            words = text.split(" ")
        except Exception:
            log.info(
                f"Questions: In <{text}> there no spaces. "
                "Can not split this text."
            )
            return text

        wrapped_lines = []
        current_line = []
        current_length = 0

        for word in words:

            if current_length > 0:
                the_space_count = 1

            else:
                the_space_count = 0

            line_length = current_length + \
                len(word) + the_space_count

            if line_length > max_length:
                wrapped_lines.append(" ".join(current_line))
                current_line = [word]
                current_length = len(word)

            else:
                if current_length > 0:
                    current_line.append(word)
                    the_space_count = 1
                else:
                    current_line = [word]
                    the_space_count = 0

                current_length += len(word) + the_space_count

        if current_line:
            wrapped_lines.append(" ".join(current_line))

        return "\n".join(wrapped_lines)

    def _extract_quest(self) -> tuple[str, str, str, str, str, str]:
        """
        # Extract Question
        The `_extract_quest` method is used to extract the asked
        question (question, answers and image) from the database.
        """

        # Image Extraction
        if self.images_ordered:
            try:
                self.image = self.df_img.iloc[
                    self.quest_numb, 0
                ]
            except Exception:
                log.error(
                    "There is not enough of images to "
                    "have an image per question!\n"
                    "Maybe try to change the <images_ordered> "
                    "argument in questions_manager = "
                    "QuestionsManager(images_ordered) to <False>"
                )

        else:
            self.image = self.df_img.iloc[
                randint(0, self.quest_count_images), 0
            ]

        self.image = resource_path(f"resources/images/{self.image}")

        if not os.path.exists(self.image) and self.enough_images:
            log.error(
                f"The image path <{self.image}> does not exist!"
            )

            self.image = ""

        # Question Extraction
        self.question = self._format_text(
            self.df.iloc[self.quest_numb, 0], 35
        ) + "\n\n\n\n\n"  # Костыли
        # It's there because Kivy refuses to move up the question.
        # So, it moves the question a little bit upper.

        # Answers Extraction
        self.true_answer = self.df.iloc[self.quest_numb, 1]
        self.wrong_answer1 = self.df.iloc[self.quest_numb, 2]
        self.wrong_answer2 = self.df.iloc[self.quest_numb, 3]
        self.wrong_answer3 = self.df.iloc[self.quest_numb, 4]

        for i in (
            self.true_answer, self.wrong_answer1,
            self.wrong_answer2, self.wrong_answer3
        ):
            self._format_text(i, 20)

        return (
            self.question, self.true_answer,
            self.wrong_answer1, self.wrong_answer2,
            self.wrong_answer3, self.image
        )

    def rand_quest(
        self
    ) -> tuple[str, str, str, str, str, str]:
        """
        # Randomize Question
        The `rand_quest` method is used to randomize the number of the
        question which is saved in the variable `quest_numb`.
        """

        if txt.current_language != self.current_language:
            self.current_language = txt.current_language
            self._change_the_language()

        if settings_manager.randomizing_style == "normal":
            if len(self.question_numbers_randomized) == 0:
                for i in range(self.quest_count):
                    self.question_numbers_randomized.append(i)

                shuffle(self.question_numbers_randomized)

            self.quest_numb = self.question_numbers_randomized[0]

            self.question_numbers_randomized.pop(0)

        elif settings_manager.randomizing_style == "alternative":
            self.quest_numb = randint(
                0, self.quest_count
            )

        elif settings_manager.randomizing_style == "in_order":
            if len(self.question_numbers) == 0:
                for i in range(self.quest_count):
                    self.question_numbers.append(i)

            self.quest_numb = self.question_numbers[0]

            self.question_numbers.pop(0)

        log.info(
            f"Questions: The <{self.quest_numb + 1} / "
            f"{self.quest_count + 1}> question is asked."
        )

        return self._extract_quest()


questions_manager = QuestionsManager(images_ordered=True)
"""
# Questions Manager
`questions_manager` is an object of the `QuestionsManager`
class which reads databases, randomizes questions and returns the
question, answers and image.

It contains only one method - `rand_quest()` which does
all of this.

It takes one argument : images_ordered which is bool.
If it's true it'll assocate images with question, if it isn't,
it'll take random images every time.
"""
