"""
# Main Menu
The `main_menu.py` module only contains the `MainMenu` class.

It corresponds to the home screen.
"""

from typing import final

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.logger import Logger as log

from sources.logic.settings_manager import settings_manager
from sources.logic.music_manager import music_manager
from sources.logic.questions_manager import questions_manager
from sources.logic.points_manager import points_manager
from sources.logic.text_manager import text_manager as txt

from sources.ui.colors import WHITE


@final
class MainMenu(Screen):
    """
    # Main Menu
    The `MainMenu` class corresponds to the home screen.
    """

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        Clock.schedule_interval(self.update_music, 0)

        self.main_layout = BoxLayout(
            orientation="vertical",
            spacing=32,
            padding=32
        )

        self.top_layout = BoxLayout(
            spacing=0,
            padding=0
        )

        self.dedications_label = Label(
            size_hint=(0.3, 0.3),
            font_size=25,
            font_name=txt.small_font,
            pos_hint={"center_x": 0.5, "center_y": 0.8}
        )

        self.name_label = Label(
            size_hint=(1, 0.3),
            font_size=70,
            font_name=txt.big_font,
            pos_hint={"center_x": 0.5, "center_y": 0.8}
        )

        self.stats_label = Label(
            size_hint=(0.3, 0.3),
            font_size=25,
            font_name=txt.small_font,
            pos_hint={"center_x": 0.5, "center_y": 0.8},
            halign="right"
        )

        self.settings_button = Button(
            pos_hint={"center_x": 0.5, "center_y": 0.7},
            size_hint=(0.7, 0.5),
            color=WHITE,
            font_size=50,
            font_name=txt.big_font,
            halign="center"
        )

        self.play_button = Button(
            pos_hint={"center_x": 0.5, "center_y": 0.2},
            size_hint=(0.7, 0.5),
            color=WHITE,
            font_size=64,
            font_name=txt.big_font
        )

        self.update_labels()

        self.settings_button.bind(on_press=self.open_settings)

        self.play_button.bind(on_press=self.open_question)

        self.top_layout.add_widget(self.dedications_label)
        self.top_layout.add_widget(self.name_label)
        self.top_layout.add_widget(self.stats_label)
        self.main_layout.add_widget(self.top_layout)
        self.main_layout.add_widget(self.settings_button)
        self.main_layout.add_widget(self.play_button)

        self.add_widget(self.main_layout)

    def update_music(self, instance=None) -> None:
        """
        # Update Music
        The `update_music` method starts a new song when the previous
        finished.
        """

        music_manager.check_song()
        music_manager.set_volumes(
            settings_manager.music_volume, settings_manager.sounds_volume
        )

    def update_labels(self, instance=None) -> None:
        """
        # Update Labels
        The `update_labels` method updates the label's text when, for
        example, a new language was set or points count was changed.
        """

        self.stats_label.text = (
            f"{txt.points}: {points_manager.points}\n"
            f"{txt.win_streak}: {points_manager.win_streak}\n"
            f"{txt.best_win_streak}: "
            f"{points_manager.best_win_streak}"
        )

        self.play_button.text = txt.play
        self.settings_button.text = txt.settings
        self.name_label.text = txt.name
        self.dedications_label.text = txt.dedications

        self.play_button.background_color = \
            settings_manager.main_color

        self.settings_button.background_color = \
            settings_manager.main_color

    def open_question(self, instance=None) -> None:
        """
        # Open Question
        The `open_question` method opens the question menu.
        """

        questions_manager.status = True
        music_manager.transition.play()
        music_manager.button_clicked.play()
        self.manager.current = "QuestionMenu"
        self.manager.get_screen("QuestionMenu").update_labels()
        log.info(
            "Main Menu: Going to the next screen -> QuestionMenu."
        )

    def open_settings(self, instance=None) -> None:
        """
        # Open Settings
        The `open_settings` method opens the settings menu.
        """

        music_manager.transition.play()
        music_manager.button_clicked.play()
        self.manager.current = "SettingsMenu"
        self.manager.get_screen("SettingsMenu").update_labels()
        self.manager.get_screen("SettingsMenu").update_menu()
        log.info("Main Menu: Going to the next screen -> SettingsMenu.")
