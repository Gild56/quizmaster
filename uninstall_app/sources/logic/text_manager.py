"""
# Text Manager
The `text_manager.py` module only contains the `TextManager` class.

It manages labels showed on UI and their translate by json files.
"""

import locale
import json
from typing import final

from sources.logic.resource_path import resource_path
from kivy.logger import Logger as log


@final
class TextManager():
    """
    # Text Manager
    The `TextManager` class manages labels showed on UI and their
    translate by json files.

    It includes 4 methods:
    - `set_system_language` sets the language of the device.
    - `get_value` imports one specific translation from the json file.
    - `translate` imports all the translations and sets the variables
    usables in the UI part.
    - `set_language` sets the chosen language if it exists.
    """

    def __init__(self) -> None:

        self.ALL_LANGUAGES = [
            "en-EN", "fr-FR", "ru-RU", "uk-UA"
        ]

        self.current_language = None

        self.big_font = resource_path(
            "resources/fonts/big_font.ttf"
        )
        self.small_font = resource_path(
            "resources/fonts/small_font.ttf"
        )

        self.labels = None

        self.file = ""

        self.english = "English (En)"
        self.french = "Français (Fr)"
        self.russian = "Русский (Ru)"
        self.ukrainian = "Украïнська (Ua)"

        self.set_system_language()
        self.translate()

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

    def set_system_language(self) -> None:
        """
        # Set System Language
        The `set_system_language` method sets the language of the
        device.
        """

        self.system_language, _ = locale.getlocale()
        log.info(
            f"Text: The system language is {self.system_language}."
        )
        self.system_language = self.system_language.lower()

        if "ru" in self.system_language:
            self.set_language("ru-RU")

        elif "fr" in self.system_language:
            self.set_language("fr-FR")

        elif (
            "ukr" in self.system_language
            or "ua" in self.system_language
        ):
            self.set_language("uk-UA")

        else:
            self.set_language("en-EN")

    def get_value(self, key) -> str:
        """
        # Get Value
        The `get_value` method imports one specific translation from
        the json file.

        It takes an argument: key. It's the key of the json file and
        the text that will be returned if an error occured.
        """

        with open(self.file, "r", encoding="UTF-8") as f:
            data = json.load(f)
            value = data.get(key, "ERROR")

        if isinstance(value, int):
            return str(value)

        if value != "ERROR":
            return value

        log.error(
            f"Text: The <{key}> key wasn't found in the "
            f"<{self.current_language}.json> file."
        )
        return self._replace_ukrainian(key)

    def translate(self) -> None:
        """
        # Translate
        The `translate` method imports all the translations and
        sets the variables which usables in the UI part.
        """

        self.file = resource_path(
            f"resources/translations/{self.current_language}.json"
        )

        self.yes = self.get_value("Yes")
        self.no = self.get_value("No")
        self.uninstall_title = self.get_value("Uninstall Quiz Master App")
        self.uninstall = self.get_value("Uninstall")
        self.warning = self.get_value("WARNING!")
        self.website = self.get_value("Visit our website\nto get help!")
        self.sure = self.get_value(
            "Are you sure to delete the Quiz Master app?"
        )
        self.warning_message = self.get_value(
            "Warning\nYou will not be able to\nrestore the lost data."
        )

        log.info(
            "Text: The translation was extracted from the"
            f"<{self.current_language}.json> file."
        )

    def set_language(self, next_language_input=None) -> None:
        """
        # Set Language
        The `set_language` method sets the chosen language if it exists.
        """

        if next_language_input is None:
            next_language = self.current_language
        else:
            next_language = next_language_input

        if next_language in self.ALL_LANGUAGES:
            self.current_language = next_language

            self.translate()

            log.info(
                "Text: The language was "
                f"changed into <{self.current_language}>."
            )


text_manager = TextManager()
"""
# Text Manager
`text_manager` is the object of the `TextManager` class which manages
labels showed on UI and their translate by json files.

It includes 4 methods:
- `set_system_language` sets the language of the device.
- `get_value` imports one specific translation from the json file.
- `translate` imports all the translations and sets the variables
usables in the UI part.
- `set_language` sets the chosen language if it exists.
"""
