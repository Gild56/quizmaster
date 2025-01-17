"""
# Music Manager
The `music_manager.py file` only contains the `MusicManager` class.

It manages music playing at the background and sound effects
"""

import os
import pygame
from random import shuffle
from typing import final, Optional

from sources.logic.resource_path import resource_path
from kivy.logger import Logger as log


@final
class MusicManager():
    """
    # Pygame Music Manager
    The `PygameMusicManager` class takes care about music and sound
    effects.

    It contains these methods:
    - `randomize_song` shuffles the list of songs or pops the last
    song.
    - `check_song` verifies if a song plays. If it is not, it'll play
    the next song in the list.
    - `next_song` plays the next song without waiting for the end of
    the previous song.

    The difference with the `MusicManager` class is that it uses
    Pygame, so that's useful for converting to .exe with PyInstaller
    because of the `GstPlayerException` error.

    `
    kivy.lib.gstplayer._gstplayer.GstPlayerException:
    Unable to create a playbin.
    Consider setting the environment variable GST_REGISTRY to
    a user accessible path, such as ~/registry.bin
    `
    """

    def __init__(self) -> None:
        pygame.mixer.init()

        self.remaining_songs = []
        self.current_song = None

        self.songs_list = self._load_music_files("resources/music")

        self.transition = pygame.mixer.Sound(
            resource_path("resources/sounds/transition.mp3"))
        self.button_clicked = pygame.mixer.Sound(
            resource_path("resources/sounds/8bit-click.wav"))
        self.win = pygame.mixer.Sound(
            resource_path("resources/sounds/win.mp3"))
        self.lose = pygame.mixer.Sound(
            resource_path("resources/sounds/lose.wav"))

        self.randomize_song()
        self._play_music()

    def _load_music_files(self, directory: str) -> list[str]:
        """
        # Load Music Files
        The `_load_music_files` method loads all .mp3 files from the
        given directory.
        """
        return [
            f
            for f in os.listdir(resource_path(directory))
            if f.endswith('.mp3')
        ]

    def _play_music(self) -> None:
        """
        # Play Music
        The `play_music` plays the next song when it's called.
        """
        if self.current_song:
            pygame.mixer.music.stop()

        self.randomize_song()
        song_path = resource_path(
            f"resources/music/{self.current_song}.mp3"
        )
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play(-1)
        log.info(f"Playing next song: {self.current_song}")

    def randomize_song(
        self, complete_shuffle: Optional[bool] = False
    ) -> None:
        """
        # Randomize Song
        The `randomize_song` method shuffles the list of songs if
        theres no more songs available or pops the last song.

        It can also do a complete shuffle of the playlist when the
        `complete_shuffle` argument is `True`
        """
        if not self.remaining_songs or complete_shuffle:
            self.remaining_songs = self.songs_list.copy()
            shuffle(self.remaining_songs)
            print("Shuffled playlist.")

        song_file = self.remaining_songs.pop()
        self.current_song, _ = os.path.splitext(song_file)

    def check_song(self) -> None:
        """
        # Check Song
        The `check_song` method verifies if a song is playing. If it
        isn't, it'll play the next one.
        """
        if not pygame.mixer.music.get_busy():
            self._play_music()

    def next_song(self) -> None:
        """
        # Next Song
        The `next_song` method plays the next song without waiting
        for the end of the previous song.
        """
        pygame.mixer.music.stop()
        self._play_music()

    def set_volumes(self, music_volume: float, sounds_volume: float) -> None:
        """
        # Set Volumes
        The `set_volumes` method adjusts the volume for music and
        sound effects.
        """
        pygame.mixer.music.set_volume(music_volume)
        self.transition.set_volume(sounds_volume)
        self.button_clicked.set_volume(sounds_volume)
        self.win.set_volume(sounds_volume)
        self.lose.set_volume(sounds_volume)


music_manager = MusicManager()
