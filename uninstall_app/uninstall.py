"""
# Uninstall
The `uninstall.py` module is used to delete the `quizmaster`
folder.
"""

from sources.logic.logs_manager import logs_manager

from typing import final

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.logger import Logger as log
from kivy.core.window import Window

from sources.ui.uninstall_menu import UninstallMenu


logs_manager.delete_old_logs(30)


@final
class UninstallQuizMasterApp(App):
    """
    # Uninstall Quiz Masster App
    The `UninstallQuizMasterApp` class contains methods to interact with the
    app.
    """

    def build(self) -> ScreenManager:
        """
        # Build
        The `build` method contains the kivy app architchture.
        ```python
        Window.set_icon("resources/images/uninstall-logo.png") # Sets the logo
        ```
        """

        log.info("UninstallApp: The Uninstall App was run.")

        Window.set_icon("resources/images/uninstall-logo.png")

        sm = ScreenManager()
        sm.add_widget(UninstallMenu(name="UninstallMenu"))
        return sm


if __name__ == "__main__":
    UninstallQuizMasterApp().run()
