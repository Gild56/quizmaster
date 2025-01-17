"""
# Uninstall Menu
The `uninnstall.py` module only contains the `UninstallMenu` class.

It corresponds to the only screen of the `Uninstall App`.
"""

import os
import webbrowser
import subprocess
from typing import final

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.logger import Logger as log
from kivy.core.window import Window

from sources.logic.resource_path import resource_path
from sources.logic.text_manager import text_manager as txt
from sources.ui.colors import WHITE, RED, LIGHT_BLUE, DARK_BLUE


@final
class UninstallMenu(Screen):
    """
    # Uninstall Menu
    The `UninstallMenu` class corresponds to the only screen of the
    `Uninstall App`.
    """

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.BATCH_PATH = resource_path("../command/uninstall-def.bat")
        if not os.path.exists(self.BATCH_PATH):
            log.error(
                f"UninstallMenu: The <{self.VBS_PATH}> file path does "
                "not exist."
            )

        self.main_color = LIGHT_BLUE
        Window.clearcolor = DARK_BLUE

        self.main_layout = BoxLayout(
            orientation="vertical",
            spacing=32,
            padding=32
        )

        self.top_layout = BoxLayout(
            spacing=0,
            padding=0
        )

        self.title_label = Label(
            text=txt.uninstall_title,
            size_hint=(1, 0.3),
            font_size=70,
            font_name=txt.big_font,
            pos_hint={"center_x": 0.5, "center_y": 0.8}
        )

        self.website_button = Button(
            text=txt.website,
            pos_hint={"center_x": 0.5, "center_y": 0.2},
            size_hint=(0.7, 0.5),
            color=WHITE,
            font_size=64,
            font_name=txt.big_font,
            background_color=LIGHT_BLUE,
            halign="center"
        )

        self.uninstall_button = Button(
            text=txt.uninstall,
            pos_hint={"center_x": 0.5, "center_y": 0.2},
            size_hint=(0.7, 0.5),
            color=WHITE,
            font_size=64,
            font_name=txt.big_font,
            background_color=LIGHT_BLUE
        )

        self.website_button.bind(on_press=self.open_website)
        self.uninstall_button.bind(on_press=self.show_popup)

        self.main_layout.add_widget(self.title_label)
        self.main_layout.add_widget(self.website_button)
        self.main_layout.add_widget(self.uninstall_button)
        self.add_widget(self.main_layout)

    def uninstall(self, instance=None) -> None:
        """
        # Uninstall
        The `uninstall` method runs the `uninstall-def.bat` file
        which deletes the `quizmaster` folder.
        """

        subprocess.Popen(self.BATCH_PATH, shell=True)

    def open_website(self, instance=None):
        """
        # Open Website
        The `open_website` method runs the
        `app/resources/web/help.html` file which corresponds to the
        help webpage.
        """
        webbrowser.open(resource_path("resources/web/help.html"))

    def show_popup(self, instance=None) -> None:
        """
        # Show Popup
        The `show_popup` method shows a popup with two buttons:
        Confirm or Not.
        """

        def yes_action(instance=None) -> None:
            self.uninstall()

        def close_popup(instance=None) -> None:
            self.popup.dismiss()

        self.current_text = txt.sure

        layout = BoxLayout(
            orientation="vertical",
            padding=10
        )

        title_label = Label(
            text=txt.warning,
            font_size="24sp",
            font_name=txt.small_font
        )

        explanation_label = Label(
            text=txt.warning_message,
            font_size="14sp",
            halign="center"
        )

        button_layout = GridLayout(
            cols=2,
            spacing=10
        )

        yes_button = Button(
            text=txt.yes,
            font_name=txt.small_font,
            background_color=RED
        )

        no_button = Button(
            text=txt.no,
            font_name=txt.small_font,
            background_color=RED
        )

        yes_button.bind(on_press=yes_action)
        no_button.bind(on_press=close_popup)

        button_layout.add_widget(yes_button)
        button_layout.add_widget(no_button)

        layout.add_widget(title_label)
        layout.add_widget(explanation_label)
        layout.add_widget(button_layout)

        self.popup = Popup(
            title=self.current_text.replace("\n", " "),
            content=layout,
            size_hint=(0.6, 0.4),
            background_color=RED
        )

        self.popup.open()
