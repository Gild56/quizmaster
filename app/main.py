"""
# Main
The `main.py` file is used to run the project.

It also cantains the kivy App class called `QuizMasterApp`.
"""

from sources.logic.logs_manager import logs_manager

from typing import final

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.logger import Logger as log
from kivy.core.window import Window

from sources.logic.points_manager import points_manager
from sources.logic.questions_manager import questions_manager
from sources.logic.settings_manager import settings_manager
from sources.logic.resource_path import resource_path

from sources.ui.main_menu import MainMenu
from sources.ui.question_menu import QuestionMenu
from sources.ui.result_menu import ResultMenu
from sources.ui.settings_menu import SettingsMenu

logs_manager.delete_old_logs(30)


@final
class QuizMasterApp(App):
    """
    # Quiz Masster App
    The `QuizMasterApp` class containsmethods to interact with the
    app.

    ```python
    class QuizMasterApp(App):
        def build(self) -> ScreenManager:
            #...
        def on_stop(self) -> None:
            #...
    ```

    ## Build
    The `build` method contains the kivy app architchture.

    ## On Stop
    The `on_stop` method is activated when the window is closig.
    """
    def build(self) -> ScreenManager:
        """
        # Build
        The `build` method contains the kivy app architchture:
        ```python
            def build(self):
                Window.set_icon("resources/images/logo.png") # Sets the logo

                sm = ScreenManager()
                sm.add_widget(MainMenu(name="MainMenu"))
                sm.add_widget(QuestionMenu(name="QuestionMenu"))
                sm.add_widget(ResultMenu(name="ResultMenu"))
                sm.add_widget(SettingsMenu(name="SettingsMenu"))
                return sm
        ```
        You can add screens before `return sm` like that:
        ```python
        sm.add_widget(YourMenu(name="YourMenu"))
        ```
        """
        Window.set_icon(resource_path("resources/images/logo.png"))

        sm = ScreenManager()
        sm.add_widget(MainMenu(name="MainMenu"))
        sm.add_widget(QuestionMenu(name="QuestionMenu"))
        sm.add_widget(ResultMenu(name="ResultMenu"))
        sm.add_widget(SettingsMenu(name="SettingsMenu"))
        return sm

    def on_stop(self) -> None:
        """
        # On Stop
        The `on_stop` method is activated when the window is closig.

        You can add your code, but at the moment
        it only saves data and makes you loose when
        you quitted and a question was asked.
        """
        settings_manager.save_data()
        if questions_manager.status:
            log.info(
                "Main: The app stopped when a question "
                "was asked. Points were lost."
            )
            points_manager.lose()


if __name__ == "__main__":
    QuizMasterApp().run()
