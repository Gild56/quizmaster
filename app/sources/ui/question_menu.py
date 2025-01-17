"""
# Question Menu
The `question_menu.py` module corresponds to the asked question
screen.
"""

from typing import final
from random import randint

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.logger import Logger as log

from sources.logic.music_manager import music_manager
from sources.logic.questions_manager import questions_manager
from sources.logic.points_manager import points_manager
from sources.logic.settings_manager import settings_manager
from sources.logic.text_manager import text_manager as txt
from sources.logic.resource_path import resource_path

from sources.ui.colors import LIGHT_YELLOW, LIGHT_GREEN, LIGHT_CYAN, LIGHT_RED
from sources.ui.colors import WHITE


@final
class QuestionMenu(Screen):
    """
    # Question Manu
    The `QuestionMenu` class corresponds to the asked question
    screen.
    """

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.image = None
        self.previous_image = None

        self.update_variables()

        self.main_layout = BoxLayout(
            orientation="vertical",
            spacing=32,
            padding=32
        )

        self.image_layout = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            spacing=64,
            padding=64
        )

        self.question_text = Label(
            font_size=48,
            font_name=txt.big_font,
            halign="center"
        )

        self.top_answers_layout = BoxLayout(
            spacing=32,
            padding=32,
            size_hint_y=None
        )

        self.bottom_answers_layout = BoxLayout(
            spacing=32,
            padding=32,
            size_hint_y=None
        )

        self.true_button = Button(
            background_color=settings_manager.main_color,
            color=WHITE,
            font_size=32,
            font_name=txt.small_font,
            size_hint=(1, 3),
            halign="center"
        )

        self.wrong_button1 = Button(
            background_color=settings_manager.main_color,
            color=WHITE,
            font_size=32,
            font_name=txt.small_font,
            size_hint=(1, 3),
            halign="center"
        )

        self.wrong_button2 = Button(
            background_color=settings_manager.main_color,
            color=WHITE,
            font_size=32,
            font_name=txt.small_font,
            size_hint=(1, 3),
            halign="center"
        )

        self.wrong_button3 = Button(
            background_color=settings_manager.main_color,
            color=WHITE,
            font_size=32,
            font_name=txt.small_font,
            size_hint=(1, 3),
            halign="center"
        )

        self.main_layout.add_widget(self.question_text)
        self.main_layout.add_widget(self.image_layout)
        self.main_layout.add_widget(self.top_answers_layout)
        self.main_layout.add_widget(self.bottom_answers_layout)

        self.add_widget(self.main_layout)

        self.true_button.bind(on_press=self.check_answer)
        self.wrong_button1.bind(on_press=self.check_answer)
        self.wrong_button2.bind(on_press=self.check_answer)
        self.wrong_button3.bind(on_press=self.check_answer)

    def update_variables(self, instance=None) -> None:
        """
        # Update Variables
        The `update_variables` method updates the label's text when, for
        example, a new language was set or points count was changed.
        """

        (
            self.question, self.true_answer,
            self.wrong_answer1, self.wrong_answer2, self.wrong_answer3,
            self.image_path
        ) = questions_manager.rand_quest()

        if settings_manager.drawing_images:

            if self.image_path is None or self.image_path == "":
                self.image = None
                log.warning(
                    "Quest. Menu: There are no image for this "
                    "question. The image wasn't created."
                )

            elif not self.image_path.strip():
                self.image = None
                log.warning(
                    "Quest. Menu: There are no image "
                    f"with the <{self.image_path}> path. "
                    "The image wasn't created."
                )

            else:
                self.image = Image(
                    source=resource_path(self.image_path),
                    size_hint_y=None,
                    height=200
                )

        else:
            self.image = None

    def update_question(self, instance=None) -> None:
        """
        # Update Question
        The `update_question` method updates the label's text when a
        new question was asked.
        """

        self.question_text.text = self.question
        self.true_button.text = self.true_answer
        self.wrong_button1.text = self.wrong_answer1
        self.wrong_button2.text = self.wrong_answer2
        self.wrong_button3.text = self.wrong_answer3

        self.image_layout.clear_widgets()
        self.top_answers_layout.clear_widgets()
        self.bottom_answers_layout.clear_widgets()

        if settings_manager.drawing_images:
            if self.image:
                if self.previous_image:
                    self.image_layout.remove_widget(
                        self.previous_image
                    )
                self.image_layout.add_widget(self.image)
                self.previous_image = self.image

            else:
                if self.previous_image:
                    self.image_layout.remove_widget(
                        self.previous_image
                    )
                    self.previous_image = None
                log.warning(
                    "Quest. Menu: There are no image for this "
                    "question. The image wasn't added to the layout."
                )

        r = randint(1, 4)
        if r == 1:
            self.top_answers_layout.add_widget(self.true_button)
            self.top_answers_layout.add_widget(self.wrong_button1)
            self.bottom_answers_layout.add_widget(self.wrong_button2)
            self.bottom_answers_layout.add_widget(self.wrong_button3)

            if settings_manager.rainbow_buttons:
                self.true_button.background_color = LIGHT_RED
                self.wrong_button1.background_color = LIGHT_YELLOW
                self.wrong_button2.background_color = LIGHT_GREEN
                self.wrong_button3.background_color = LIGHT_CYAN

        elif r == 2:
            self.top_answers_layout.add_widget(self.wrong_button3)
            self.top_answers_layout.add_widget(self.true_button)
            self.bottom_answers_layout.add_widget(self.wrong_button1)
            self.bottom_answers_layout.add_widget(self.wrong_button2)

            if settings_manager.rainbow_buttons:
                self.wrong_button3.background_color = LIGHT_RED
                self.true_button.background_color = LIGHT_YELLOW
                self.wrong_button1.background_color = LIGHT_GREEN
                self.wrong_button2.background_color = LIGHT_CYAN

        elif r == 3:
            self.top_answers_layout.add_widget(self.wrong_button2)
            self.top_answers_layout.add_widget(self.wrong_button3)
            self.bottom_answers_layout.add_widget(self.true_button)
            self.bottom_answers_layout.add_widget(self.wrong_button1)

            if settings_manager.rainbow_buttons:
                self.wrong_button2.background_color = LIGHT_RED
                self.wrong_button3.background_color = LIGHT_YELLOW
                self.true_button.background_color = LIGHT_GREEN
                self.wrong_button1.background_color = LIGHT_CYAN

        else:
            self.top_answers_layout.add_widget(self.wrong_button1)
            self.top_answers_layout.add_widget(self.wrong_button2)
            self.bottom_answers_layout.add_widget(self.wrong_button3)
            self.bottom_answers_layout.add_widget(self.true_button)

            if settings_manager.rainbow_buttons:
                self.wrong_button1.background_color = LIGHT_RED
                self.wrong_button2.background_color = LIGHT_YELLOW
                self.wrong_button3.background_color = LIGHT_GREEN
                self.true_button.background_color = LIGHT_CYAN

        if not settings_manager.rainbow_buttons:
            self.true_button.background_color = \
                settings_manager.main_color

            self.wrong_button1.background_color = \
                settings_manager.main_color

            self.wrong_button2.background_color = \
                settings_manager.main_color

            self.wrong_button3.background_color = \
                settings_manager.main_color

    def update_labels(self, instance=None) -> None:
        """
        # Update Menu
        The `update_labels` method updates the label's text when, for
        example, a new language was set or points count was changed.
        """

        self.update_variables()
        self.update_question()

    def check_answer(self, instance=None) -> None:
        """
        # Check Answer
        The `check_answer` method verifies if the answer is `True` or
        `False`.
        """

        music_manager.button_clicked.play()
        if instance.text == questions_manager.true_answer:
            points_manager.win()
            win = True
            music_manager.win.play()
        else:
            points_manager.lose()
            win = False
            music_manager.lose.play()

        self.manager.current = "ResultMenu"
        self.manager.get_screen("ResultMenu").update_labels(win)
        questions_manager.status = False
        music_manager.transition.play()

        log.info(f"Quest. Menu: The answer was <{str(win).lower()}>.")
        log.info("Quest. Menu: Going to the next screen -> ResultMenu.")
