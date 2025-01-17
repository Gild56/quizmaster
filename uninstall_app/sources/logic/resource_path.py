"""
# Resource Path
The `resouce_path.py file contains only one function: `resouce_path`.
It's used to get the complete path of a file or a folder.

It's also useful for converting the project into an executable (.exe).
"""

import os
import sys
from kivy.logger import Logger as log

def resource_path(relative_path:str | None = None) -> str:
    """
    # Resource Path
    The `resouce_path` function is used to get the complete path of a
    file or a folder.

    It's also useful for converting the project into an executable
    (.exe).
    """

    if relative_path == None:
        log.error(
            f"ResourcePath: The path <{relative_path}> wasn't found."
        )
        return relative_path

    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    file_path = os.path.join(base_path, str(relative_path))
    if os.path.exists(file_path):
        return file_path
    else:
        return os.path.join(base_path, "uninstall_app", str(relative_path))
