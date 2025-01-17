"""
# Points Manager
The `points_manager.pymodule contains only one class:
`PointsManager`.

It counts points, saves and loads them from a json file.
"""
import os
import json
from typing import final

from sources.logic.resource_path import resource_path
from kivy.logger import Logger as log


@final
class PointsManager():
    """
    # Points Manager
    The `PointsManager` class counts points, saves and loads them
    from a json file.

    It contains these methods:
    - `save_data` saves data in the points.json file.
    - `import_data` imports data from the points.json file.
    - `clear_data` clears the points.json file.
    - `lose` makes the player lose points.
    - `win` makes the player win points.
    """

    def __init__(self) -> None:
        self.WINNING_POINTS = 7
        self.MAX_WINNING_WIN_STREAK_POINTS = 5
        self.WINNING_WIN_STREAK_POINTS = 1
        self.LOSING_POINTS = 10

        self.points = 0
        self.win_streak = 0
        self.best_win_streak = 0

        if not os.path.exists(resource_path("sources/json/")):
            os.makedirs(resource_path("sources/json/"))
            log.info(
                "Points: The <sources/json/> folder does"
                " not exist. A new <sources/json/> folder was "
                "created."
            )

        self.JSON_PATH = resource_path("sources/json/points.json")

        if not os.path.exists(self.JSON_PATH):
            log.info(
                "Points: The <sources/json/points.json> "
                "file does not exist. The new one was created."
            )
            with open(self.JSON_PATH, "w", encoding="UTF-8") as f:
                json.dump({
                    "points": 0,
                    "win_streak": 0,
                    "best_win_streak": 0
                }, f)

        try:
            self.import_data()
        except Exception:
            log.info(
                "Points: The <sources/json/points.json> "
                "format isn't the required one. "
                "The <sources/json/settings.json> file was reset."
            )

    def save_data(self) -> None:
        """
        # Save Data
        The `save_data` method saves data in the points.json file.
        """

        with open(self.JSON_PATH, "w", encoding="UTF-8") as f:
            json.dump({
                "points": self.points,
                "win_streak": self.win_streak,
                "best_win_streak": self.best_win_streak
            }, f)
        log.info(
            "Points: Data has been saved in the points.json file."
        )

    def import_data(self) -> None:
        """
        # Import Data
        The `import_data` method imports data from the points.json file.
        """

        if os.path.getsize(self.JSON_PATH) == 0:
            with open(self.JSON_PATH, "w", encoding="UTF-8") as f:
                json.dump({
                    "points": 0,
                    "win_streak": 0,
                    "best_win_streak": 0
                }, f)

        with open(self.JSON_PATH, "r", encoding="UTF-8") as f:
            data = json.load(f)
            self.points = data.get("points", 0)
            self.win_streak = data.get("win_streak", 0)
            self.best_win_streak = data.get("best_win_streak", 0)
        log.info(
            "Points: Data has been imported "
            "from the points.json file."
        )

    def clear_data(self) -> None:
        """
        # Clear Data
        The `clear_data` method clears the points.json file.
        """

        self.points, self.win_streak, self.best_win_streak = 0, 0, 0
        log.info("Points: The stats were succesfully cleared.")
        self.save_data()

    def win(self) -> None:
        """
        # Win
        The `win` method makes the player win points.
        """

        self.points += self.WINNING_POINTS

        if self.win_streak < self.MAX_WINNING_WIN_STREAK_POINTS:

            self.points += (
                self.win_streak * self.WINNING_WIN_STREAK_POINTS
            )

        else:
            self.points += (
                self.WINNING_WIN_STREAK_POINTS
                * self.MAX_WINNING_WIN_STREAK_POINTS
            )

        self.win_streak += 1

        if self.win_streak > self.best_win_streak:
            self.best_win_streak = self.win_streak

        self.save_data()

    def lose(self) -> None:
        """
        # Lose
        The `lose` method makes the player lose points.
        """

        self.win_streak = 0
        self.points -= self.LOSING_POINTS

        if self.points < 0:
            self.points = 0

        self.save_data()


points_manager = PointsManager()
"""
# Points Manager
`points_manager` is an object of the `PointsManager` class which
counts points, saves and loads them from a json file.

It contains these methods:
- `save_data` saves data in the points.json file.
- `import_data` imports data from the points.json file.
- `clear_data` clears the points.json file.
- `lose` makes the player lose points.
- `win` makes the player win points.
"""
