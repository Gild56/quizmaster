"""
# Settings Manager
The `settings_manager.pymodule only contains `SettingsManager` class.

It manages, contains settings variables used in UI, saves and loads
informations from a json file.
"""

import os
import json
from typing import final

from kivy.core.window import Window

from sources.logic.resource_path import resource_path
from kivy.logger import Logger as log

from sources.logic.text_manager import text_manager as txt

from sources.ui.colors import LIGHT_BLUE, DARK_BLUE, LIGHT_ORANGE, DARK_ORANGE
from sources.ui.colors import PINK, DARK_PINK, YELLOW, DARK_YELLOW, LIGHT_CYAN
from sources.ui.colors import LIGHT_VIOLET, DARK_VIOLET, CYAN, GREY, DARK_GREY
from sources.ui.colors import BLACK


@final
class SettingsManager():
    """
    # Settings Manager
    The `SettingManager` class manages the settings, contains
    variables used in UI, saves and loads informations from a json
    file.

    It contains these methods:
    - `save_data` saves data in the settings.json file.
    - `import_data` imports data from the settings.json file.
    - `clear_data` clears the settings.json file.
    - `color_change` changes the color of the app's menus.
    """

    def __init__(self) -> None:
        self.music_volume = 0
        self.sounds_volume = 0
        self.menus_color = "blue"
        self.drawing_images = True
        self.randomizing_style = "normal"
        self.rainbow_buttons = False
        self.main_color = LIGHT_BLUE
        self.bg_color = DARK_BLUE

        self.RANDOMIZING_STYLES = [
            "normal", "alternative", "in_order"
        ]

        self.COLORS = [
            "blue", "orange",
            "violet", "pink",
            "yellow", "cyan",
            "grey", "black"
        ]

        if not os.path.exists(resource_path("sources/json/")):
            os.makedirs(resource_path("sources/json/"))
            log.info(
                "Settings: The sources/json/ folder does not exist. "
                "A new sources/json/ folder was created"
            )

        self.JSON_PATH = resource_path("sources/json/settings.json")

        if not os.path.exists(self.JSON_PATH):
            self.clear_data()
            log.info(
                "Settings: The sources/json/settings.json file "
                "does not exist. The new one was created."
            )
        self.import_data()

    def save_data(self) -> None:
        """
        # Save Data
        The `save_data` method saves data in the settings.json file.
        """

        with open(self.JSON_PATH, "w", encoding="UTF-8") as f:
            json.dump({
                "music_volume": self.music_volume,
                "sounds_volume": self.sounds_volume,
                "language": txt.current_language,
                "menus_color": self.menus_color,
                "drawing_images": self.drawing_images,
                "randomizing_style": self.randomizing_style,
                "rainbow_buttons": self.rainbow_buttons
            }, f)
        log.info(
            "Settings: Data has been saved in the settings.json file."
        )

    def import_data(self) -> None:
        """
        # Import Data
        The `mport_data` method imports data from the settings.json file.
        """

        try:
            with open(self.JSON_PATH, "r", encoding="UTF-8") as f:
                data = json.load(f)
                self.music_volume = data.get("music_volume", 0.5)
                self.sounds_volume = data.get("sounds_volume", 0.25)
                self.current_language = data.get("language", None)
                self.menus_color = data.get("menus_color", "blue")
                self.drawing_images = data.get("drawing_images", True)
                self.randomizing_style = data.get(
                    "randomizing_style", "normal"
                )
                self.rainbow_buttons = data.get("rainbow_buttons", False)

        except Exception:
            self.clear_data()
            log.warning(
                "The <settings.json> file wasn't set correctly. It was reset."
            )

        int(self.music_volume)
        int(self.sounds_volume)

        self.current_language.lower()
        self.randomizing_style.lower()

        if self.menus_color not in self.COLORS:
            self.menus_color = "blue"

        if self.music_volume > 1:
            self.music_volume = 1
        elif self.music_volume < 0:
            self.music_volume = 0

        if self.sounds_volume > 1:
            self.sounds_volume = 1
        elif self.sounds_volume < 0:
            self.sounds_volume = 0

        if self.randomizing_style not in self.RANDOMIZING_STYLES:
            self.randomizing_style = "normal"

        self.color_change()

        if self.drawing_images not in [True, False]:
            self.drawing_images = True

        if self.rainbow_buttons not in [True, False]:
            self.rainbow_buttons = False

        if self.current_language not in txt.ALL_LANGUAGES:
            txt.set_system_language()
        else:
            txt.current_language = self.current_language
            txt.set_language()

        log.info(
            "Settings: Data has been imported "
            "from the settings.json file."
        )

        self.save_data()

    def clear_data(self) -> None:
        """
        # Clear Data
        The `clear_data` method clears the settings.json file.
        """

        txt.set_system_language()
        with open(self.JSON_PATH, "w", encoding="UTF-8") as f:
            json.dump({
                "music_volume": 0.5,
                "sounds_volume": 0.25,
                "language": txt.current_language,
                "menus_color": "blue",
                "drawing_images": True,
                "randomizing_style": "normal",
                "rainbow_buttons": False
            }, f)

        log.info(
            "Settings: The settings data has been cleared."
        )

        self.import_data()

    def color_change(self) -> None:
        """
        # Color Change
        The `color_change` method changes the color of the app's menus.
        """

        if self.menus_color == "blue":
            self.main_color = LIGHT_BLUE
            self.bg_color = DARK_BLUE

        elif self.menus_color == "orange":
            self.main_color = LIGHT_ORANGE
            self.bg_color = DARK_ORANGE

        elif self.menus_color == "violet":
            self.main_color = LIGHT_VIOLET
            self.bg_color = DARK_VIOLET

        elif self.menus_color == "pink":
            self.main_color = PINK
            self.bg_color = DARK_PINK

        elif self.menus_color == "yellow":
            self.main_color = YELLOW
            self.bg_color = DARK_YELLOW

        elif self.menus_color == "cyan":
            self.main_color = LIGHT_CYAN
            self.bg_color = CYAN

        elif self.menus_color == "grey":
            self.main_color = GREY
            self.bg_color = DARK_GREY

        elif self.menus_color == "black":
            self.main_color = DARK_GREY
            self.bg_color = BLACK

        Window.clearcolor = self.bg_color

        self.save_data()


settings_manager = SettingsManager()
"""
# Settings Manager
`settings_manager` is the object of the `SettingManager` class
which manages the settings, contains variables used in UI,
saves and loads informations from a json file.

It contains these methods:
- `save_data` saves data in the settings.json file.
- `import_data` imports data from the settings.json file.
- `clear_data` clears the settings.json file.
- `color_change` changes the color of the app's menus.
"""
