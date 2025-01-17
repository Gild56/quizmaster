"""
# Result Menu
The `result_menu.py` module only contains the `ResultMenu` class.

It correspnds to the result (true/false) answer screen.
"""

from random import choice
from typing import final

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.logger import Logger as log

from sources.logic.music_manager import music_manager
from sources.logic.points_manager import points_manager
from sources.logic.settings_manager import settings_manager
from sources.logic.text_manager import text_manager as txt

from sources.ui.colors import DARK_GREEN, GREEN, DARK_RED, RED
from sources.ui.colors import WHITE


@final
class ResultMenu(Screen):
    """
    # Result Menu
    The `ResultMenu` class correspnds to the result (true/false)
    answer screen.
    """

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.main_layout = BoxLayout(
            orientation="vertical",
            spacing=8,
            padding=20
        )

        self.top_text = Label(
            size_hint=(1, 0.3),
            font_size=96,
            font_name=txt.big_font
        )

        self.bottom_text = Label(
            size_hint=(1, 0.3),
            font_size=64,
            font_name=txt.small_font
        )

        self.stats_label = Label(
            size_hint=(0.3, 0.3),
            font_size=25,
            font_name=txt.small_font,
            pos_hint={"center_x": 0.5, "center_y": 0.8},
            halign="center"
        )

        self.exit_button = Button(
            text=txt.main_menu,
            pos_hint={"center_x": 0.5, "center_y": 0.4},
            size_hint=(0.5, 0.2),
            background_color=settings_manager.main_color,
            color=WHITE,
            font_size=32,
            font_name=txt.small_font,
            halign="center"
        )

        self.next_screen_button = Button(
            text=txt.next,
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint=(0.5, 0.2),
            background_color=settings_manager.main_color,
            color=WHITE,
            font_size=64,
            font_name=txt.big_font
        )

        self.next_screen_button.bind(on_press=self.next_screen)
        self.exit_button.bind(on_press=self.exit_to_main_menu)

        self.main_layout.add_widget(self.top_text)
        self.main_layout.add_widget(self.bottom_text)
        self.main_layout.add_widget(self.stats_label)
        self.main_layout.add_widget(self.exit_button)
        self.main_layout.add_widget(self.next_screen_button)

        self.add_widget(self.main_layout)

    def update_labels(self, is_correct, instance=None) -> None:
        """
        # Update Labels
        The `update_labels` method updates the label's text when, for
        example, a new language was set or points count was changed.
        """

        self.exit_button.text = txt.main_menu
        self.next_screen_button.text = txt.next
        if is_correct:
            self.bottom_text.font_size = 64
            self.top_text.text = choice(txt.good_answers)
            self.bottom_text.text = choice(txt.keep_it_messages)
            Window.clearcolor = DARK_GREEN
            self.exit_button.background_color = GREEN
            self.next_screen_button.background_color = GREEN

        else:
            self.bottom_text.font_size = 32
            Window.clearcolor = DARK_RED
            self.exit_button.background_color = RED
            self.next_screen_button.background_color = RED
            self.top_text.text = choice(txt.wrong_answers)
            t = self.manager.get_screen("QuestionMenu").true_answer
            self.bottom_text.text = (
                f"{txt.correct_answer}: \"{t}\"."
            )

        self.stats_label.text = (
            f"{txt.points}: {points_manager.points}\n "
            f"{txt.win_streak}: {points_manager.win_streak}\n "
            f"{txt.best_win_streak}: "
            f"{points_manager.best_win_streak}"
        )

    def next_screen(self, instance=None) -> None:
        """
        # Next Screen
        The `next_screen` method makes the sceen change to the
        question menu.
        """

        music_manager.button_clicked.play()
        music_manager.transition.play()

        self.manager.current = "QuestionMenu"
        self.manager.get_screen("QuestionMenu").update_labels()
        log.info("Result Menu: Going to the next screen -> QuestionMenu.")

        Window.clearcolor = settings_manager.bg_color

    def exit_to_main_menu(self, instance=None) -> None:
        """
        # Exit to Main Menu
        The `exit_to_main_menu` method makes the screen change to the
        main menu.
        """
        music_manager.button_clicked.play()
        music_manager.transition.play()

        self.manager.current = "MainMenu"
        self.manager.get_screen("MainMenu").update_labels()
        log.info("Result Menu: Going to the next screen -> MainMenu.")

        Window.clearcolor = settings_manager.bg_color
