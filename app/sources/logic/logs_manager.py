"""
# Logger
The `logs_manager.pymodule only contains the `LogsManager` class.

It formats and saves logs in the logs folder, counts files in the
logs folder and deletes old ones.
"""

import os
from logging import NOTSET, FileHandler
from datetime import datetime
from typing import final

from kivy.logger import Logger as log
from kivy.logger import KivyFormatter

from sources.logic.resource_path import resource_path


@final
class LogsManager():
    """
    # Logs Manager
    The `LogsManager` class contains two mathods:
    - `specify_logging` specifies the logs saving.
    - `delete_old_logs` deletes old logs if the files count is bigger
    than the `max_files`.
    """

    def __init__(
        self, logs_folder: str | None = "logs/",
        max_files: int | None = 10
    ) -> None:

        self.handler = None  # It'll be a `FileHandler`

        self.logs_folder = resource_path(logs_folder)
        self.filename = ""
        self.file_path = ""
        self.max_files = max_files

        self.custom_formatting = KivyFormatter(
            "[%(levelname)-7s] %(message)s", use_color=False
        )

        if not os.path.exists(self.logs_folder):
            os.makedirs(self.logs_folder)
            log.info(
                "Logs: The logs folder does not exist. A new "
                f"logs folder was created at <{logs_folder}>"
            )

        self.files = os.listdir(self.logs_folder)

        self.specify_logging()

    def specify_logging(self) -> None:
        """
        # Specify Logging
        The `specify_logging` specifies the logs saving folder and
        text formating making it look like Kivy's logs in the
        terminal.
        """

        self.filename = (
            f"log_{datetime.now().strftime('%d-%m-%y_%H-%M-%S')}.log"
        )

        self.file_path = resource_path(
            self.logs_folder + "/" + self.filename
        )

        self.handler = FileHandler(self.file_path, mode="a")
        self.handler.setLevel(NOTSET)
        self.handler.setFormatter(self.custom_formatting)

        log.info(
            "Logs: Record log in "
            f"<{self.logs_folder}/{self.filename}>"
        )

        log.addHandler(self.handler)

    def delete_old_logs(self, max_files: int | None = None) -> None:
        """
        # Delete Old Logs
        The `delete_old_logs` method deletes the oldest logs when
        `max_files` is bigger than logs count in the folder.
        """

        if max_files is not None:
            self.max_files = max_files

        if len(self.files) <= self.max_files:
            return

        self.files.sort()

        old_files_count = len(self.files) - self.max_files + 1

        for i in range(old_files_count):
            old_file = resource_path(f"logs/{self.files[i]}")
            os.remove(old_file)
            log.info(
                f"Logs: Deleted old log: <logs/{self.files[i]}>"
            )


logs_manager = LogsManager()
"""
# Logs Manager
`logs_manager` is an object of the `LogsManager` class which
contains two mathods:
- `specify_logging` specifies the logs saving.
- `delete_old_logs` deletes old logs if the files count is bigger
than the `max_files`
"""
