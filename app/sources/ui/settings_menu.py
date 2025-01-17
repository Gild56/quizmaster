"""
# Settings Menu
The `settings_menui.py` module only contains the `SettingsMenu`
class.

It corresponds to the settings screen..
"""

from typing import final

from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.clock import Clock
from kivy.logger import Logger as log

from sources.logic.music_manager import music_manager
from sources.logic.settings_manager import settings_manager
from sources.logic.points_manager import points_manager
from sources.logic.questions_manager import questions_manager
from sources.logic.text_manager import text_manager as txt

from sources.ui.colors import RED, WHITE


@final
class SettingsMenu(Screen):
    """
    # Settings Menu
    The `SettingsMenu` class .
    """

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        Clock.schedule_interval(self.update_music, 0)

        self.main_layout = BoxLayout(
            spacing=0,
            padding=0
        )

        self.left_layout = BoxLayout(
            orientation="vertical",
            spacing=32,
            padding=32
        )

        self.right_layout = BoxLayout(
            orientation="vertical",
            spacing=0,
            padding=32
        )

        self.reset_settings_button = Button(
            size_hint=(1, 0.1),
            color=WHITE,
            font_size=32,
            font_name=txt.small_font,
            halign="center",
            on_press=self.show_popup
        )

        self.clear_button = Button(
            size_hint=(1, 0.1),
            color=WHITE,
            font_size=32,
            font_name=txt.small_font,
            on_press=self.show_popup
        )

        self.next_song_button = Button(
            size_hint=(1, 0.1),
            color=WHITE,
            font_size=32,
            font_name=txt.small_font,
            on_press=self.next_song
        )

        self.return_button = Button(
            size_hint=(1, 0.1),
            color=WHITE,
            font_size=32,
            font_name=txt.small_font,
            on_press=self.return_in_main_menu
        )

        self.music_label = Label(
            font_size=32,
            font_name=txt.big_font
        )

        self.music_slider = Slider(
            min=0,
            max=100,
            value=settings_manager.music_volume * 100
        )

        self.sounds_label = Label(
            font_size=32,
            font_name=txt.big_font
        )

        self.sounds_slider = Slider(
            min=0,
            max=100,
            value=settings_manager.sounds_volume * 100
        )

        self.drawing_images_layout = BoxLayout()

        self.drawing_images_checkbox = CheckBox(
            size_hint=(0, 0),
            pos_hint={"center_x": 1, "center_y": 0.5}
        )

        self.drawing_images_label = Label(
            font_size=25,
            font_name=txt.small_font,
            halign="right"
        )

        self.rainbow_buttons_layout = BoxLayout()

        self.rainbow_buttons_checkbox = CheckBox(
            size_hint=(0, 0),
            pos_hint={"center_x": 1, "center_y": 0.5}
        )

        self.rainbow_buttons_label = Label(
            font_size=25,
            font_name=txt.small_font,
            halign="right"
        )

        # Languages

        self.languages_label = Label(
            font_size=32,
            font_name=txt.big_font
        )

        self.languages_layout1 = BoxLayout(
            spacing=16,
            padding=16
        )

        self.english_checkbox = CheckBox(
            group="languages"
        )

        self.english_label = Label(
            font_size=25,
            font_name=txt.small_font
        )

        self.french_checkbox = CheckBox(
            group="languages"
        )

        self.french_label = Label(
            font_size=25,
            font_name=txt.small_font
        )

        self.languages_layout2 = BoxLayout(
            spacing=16,
            padding=16
        )

        self.russian_checkbox = CheckBox(
            group="languages"
        )

        self.russian_label = Label(
            font_size=25,
            font_name=txt.small_font
        )

        self.ukrainian_checkbox = CheckBox(
            group="languages"
        )

        self.ukrainian_label = Label(
            font_size=25,
            font_name=txt.small_font
        )

        # Color theme

        self.color_theme_label = Label(
            font_size=32,
            font_name=txt.big_font
        )

        self.color_themes_layout1 = BoxLayout(
            spacing=16,
            padding=16
        )

        self.blue_checkbox = CheckBox(
            group="colors"
        )

        self.blue_label = Label(
            font_size=25,
            font_name=txt.small_font
        )

        self.orange_checkbox = CheckBox(
            group="colors"
        )

        self.orange_label = Label(
            font_size=25,
            font_name=txt.small_font
        )

        self.color_themes_layout2 = BoxLayout(
            spacing=16,
            padding=16
        )

        self.violet_checkbox = CheckBox(
            group="colors"
        )

        self.violet_label = Label(
            font_size=25,
            font_name=txt.small_font
        )

        self.pink_checkbox = CheckBox(
            group="colors"
        )

        self.pink_label = Label(
            font_size=25,
            font_name=txt.small_font
        )

        self.color_themes_layout3 = BoxLayout(
            spacing=16,
            padding=16
        )

        self.yellow_checkbox = CheckBox(
            group="colors"
        )

        self.yellow_label = Label(
            font_size=25,
            font_name=txt.small_font
        )

        self.cyan_checkbox = CheckBox(
            group="colors"
        )

        self.cyan_label = Label(
            font_size=25,
            font_name=txt.small_font
        )

        self.color_themes_layout4 = BoxLayout(
            spacing=16,
            padding=16
        )

        self.grey_checkbox = CheckBox(
            group="colors"
        )

        self.grey_label = Label(
            font_size=25,
            font_name=txt.small_font
        )

        self.black_checkbox = CheckBox(
            group="colors"
        )

        self.black_label = Label(
            font_size=25,
            font_name=txt.small_font
        )

        # Questions randomizing styles

        self.randomizing_styles_label = Label(
            font_size=32,
            font_name=txt.big_font
        )

        self.randomizing_styles_layout1 = BoxLayout(
            spacing=16,
            padding=16
        )

        self.normal_checkbox = CheckBox(
            group="randomizing_styles"
        )

        self.normal_label = Label(
            font_size=25,
            font_name=txt.small_font
        )

        self.alternative_checkbox = CheckBox(
            group="randomizing_styles"
        )

        self.alternative_label = Label(
            font_size=25,
            font_name=txt.small_font
        )

        self.randomizing_styles_layout2 = BoxLayout(
            spacing=16,
            padding=16
        )

        self.in_order_checkbox = CheckBox(
            group="randomizing_styles"
        )

        self.in_order_label = Label(
            font_size=25,
            font_name=txt.small_font,
            halign="right"
        )

        # Adding methods to buttons

        self.drawing_images_checkbox.bind(active=self.drawing_images)
        self.rainbow_buttons_checkbox.bind(active=self.rainbow_buttons)

        self.normal_checkbox.bind(active=self.set_randomizing_style)
        self.alternative_checkbox.bind(active=self.set_randomizing_style)
        self.in_order_checkbox.bind(active=self.set_randomizing_style)

        self.english_checkbox.bind(active=self.set_language)
        self.french_checkbox.bind(active=self.set_language)
        self.russian_checkbox.bind(active=self.set_language)
        self.ukrainian_checkbox.bind(active=self.set_language)

        self.blue_checkbox.bind(active=self.set_color)
        self.orange_checkbox.bind(active=self.set_color)
        self.violet_checkbox.bind(active=self.set_color)
        self.pink_checkbox.bind(active=self.set_color)
        self.yellow_checkbox.bind(active=self.set_color)
        self.cyan_checkbox.bind(active=self.set_color)
        self.grey_checkbox.bind(active=self.set_color)
        self.black_checkbox.bind(active=self.set_color)

        # Adding widgets to layouts

        self.randomizing_styles_layout1.add_widget(self.normal_checkbox)
        self.randomizing_styles_layout1.add_widget(self.normal_label)
        self.randomizing_styles_layout1.add_widget(self.alternative_checkbox)
        self.randomizing_styles_layout1.add_widget(self.alternative_label)

        self.randomizing_styles_layout2.add_widget(self.in_order_checkbox)
        self.randomizing_styles_layout2.add_widget(self.in_order_label)

        self.languages_layout1.add_widget(self.english_checkbox)
        self.languages_layout1.add_widget(self.english_label)
        self.languages_layout1.add_widget(self.french_checkbox)
        self.languages_layout1.add_widget(self.french_label)

        self.languages_layout2.add_widget(self.russian_checkbox)
        self.languages_layout2.add_widget(self.russian_label)
        self.languages_layout2.add_widget(self.ukrainian_checkbox)
        self.languages_layout2.add_widget(self.ukrainian_label)

        self.color_themes_layout1.add_widget(self.blue_checkbox)
        self.color_themes_layout1.add_widget(self.blue_label)
        self.color_themes_layout1.add_widget(self.orange_checkbox)
        self.color_themes_layout1.add_widget(self.orange_label)

        self.color_themes_layout2.add_widget(self.violet_checkbox)
        self.color_themes_layout2.add_widget(self.violet_label)
        self.color_themes_layout2.add_widget(self.pink_checkbox)
        self.color_themes_layout2.add_widget(self.pink_label)

        self.color_themes_layout3.add_widget(self.yellow_checkbox)
        self.color_themes_layout3.add_widget(self.yellow_label)
        self.color_themes_layout3.add_widget(self.cyan_checkbox)
        self.color_themes_layout3.add_widget(self.cyan_label)

        self.color_themes_layout4.add_widget(self.grey_checkbox)
        self.color_themes_layout4.add_widget(self.grey_label)
        self.color_themes_layout4.add_widget(self.black_checkbox)
        self.color_themes_layout4.add_widget(self.black_label)

        self.drawing_images_layout.add_widget(self.drawing_images_checkbox)
        self.drawing_images_layout.add_widget(self.drawing_images_label)

        self.rainbow_buttons_layout.add_widget(self.rainbow_buttons_checkbox)
        self.rainbow_buttons_layout.add_widget(self.rainbow_buttons_label)

        self.right_layout.add_widget(self.drawing_images_layout)
        self.right_layout.add_widget(self.rainbow_buttons_layout)

        self.right_layout.add_widget(self.languages_label)
        self.right_layout.add_widget(self.languages_layout1)
        self.right_layout.add_widget(self.languages_layout2)
        self.right_layout.add_widget(self.music_label)
        self.right_layout.add_widget(self.music_slider)
        self.right_layout.add_widget(self.sounds_label)
        self.right_layout.add_widget(self.sounds_slider)

        self.right_layout.add_widget(self.color_theme_label)
        self.right_layout.add_widget(self.color_themes_layout1)
        self.right_layout.add_widget(self.color_themes_layout2)
        self.right_layout.add_widget(self.color_themes_layout3)
        self.right_layout.add_widget(self.color_themes_layout4)
        self.right_layout.add_widget(self.randomizing_styles_label)
        self.right_layout.add_widget(self.randomizing_styles_layout1)
        self.right_layout.add_widget(self.randomizing_styles_layout2)

        self.left_layout.add_widget(self.reset_settings_button)
        self.left_layout.add_widget(self.clear_button)
        self.left_layout.add_widget(self.next_song_button)
        self.left_layout.add_widget(self.return_button)

        self.main_layout.add_widget(self.left_layout)
        self.main_layout.add_widget(self.right_layout)

        self.add_widget(self.main_layout)

        self.update_labels()

    def update_labels(self, instance=None) -> None:

        # Костыли :(
        self.rainbow_buttons_label.text = \
            txt.rainbow_buttons + "          "
        self.drawing_images_label.text = \
            txt.drawing_images + "          "
        self.in_order_label.text = \
            txt.in_order + "                        "

        # !Don't change this part
        #  Kivy library doesn't accept to center
        #  to left objects of a layout.
        #  So, I set horizontal align to the right
        #  And made the line longer

        self.reset_settings_button.text = txt.reset_settings
        self.clear_button.text = txt.clear_stats
        self.next_song_button.text = txt.next_song
        self.return_button.text = txt.main_menu

        self.music_label.text = txt.music
        self.sounds_label.text = txt.sounds

        self.languages_label.text = txt.languages

        self.normal_label.text = txt.normal
        self.alternative_label.text = txt.alternative
        self.randomizing_styles_label.text = txt.randomizing_styles

        self.english_label.text = txt.english
        self.french_label.text = txt.french
        self.russian_label.text = txt.russian
        self.ukrainian_label.text = txt.ukrainian
        self.color_theme_label.text = txt.color_theme

        self.blue_label.text = txt.blue
        self.orange_label.text = txt.orange
        self.violet_label.text = txt.violet
        self.pink_label.text = txt.pink
        self.yellow_label.text = txt.yellow
        self.cyan_label.text = txt.cyan
        self.grey_label.text = txt.grey
        self.black_label.text = txt.black

        self.reset_settings_button.background_color = \
            settings_manager.main_color
        self.clear_button.background_color = \
            settings_manager.main_color
        self.next_song_button.background_color = \
            settings_manager.main_color
        self.return_button.background_color = \
            settings_manager.main_color

    def update_menu(self, instance=None) -> None:

        if settings_manager.drawing_images:
            self.drawing_images_checkbox.active = True
        else:
            self.drawing_images_checkbox.active = False

        if settings_manager.rainbow_buttons:
            self.rainbow_buttons_checkbox.active = True
        else:
            self.rainbow_buttons_checkbox.active = False

        if settings_manager.menus_color == "blue":
            self.blue_checkbox.active = True
        elif settings_manager.menus_color == "orange":
            self.orange_checkbox.active = True
        elif settings_manager.menus_color == "violet":
            self.violet_checkbox.active = True
        elif settings_manager.menus_color == "pink":
            self.pink_checkbox.active = True
        elif settings_manager.menus_color == "yellow":
            self.yellow_checkbox.active = True
        elif settings_manager.menus_color == "cyan":
            self.cyan_checkbox.active = True
        elif settings_manager.menus_color == "grey":
            self.grey_checkbox.active = True
        else:
            self.black_checkbox.active = True

        if settings_manager.current_language == "en-EN":
            self.english_checkbox.active = True
        elif settings_manager.current_language == "fr-FR":
            self.french_checkbox.active = True
        elif settings_manager.current_language == "ru-RU":
            self.russian_checkbox.active = True
        else:
            self.ukrainian_checkbox.active = True

        if settings_manager.randomizing_style == "alternative":
            self.alternative_checkbox.active = True
        elif settings_manager.randomizing_style == "in_order":
            self.in_order_checkbox.active = True
        else:
            self.normal_checkbox.active = True

        self.music_slider.value = \
            settings_manager.music_volume * 100
        self.sounds_slider.value = \
            settings_manager.sounds_volume * 100

    def update_music(self, instance=None) -> None:
        settings_manager.music_volume = \
            round(self.music_slider.value / 100, 2)
        settings_manager.sounds_volume = \
            round(self.sounds_slider.value / 100, 2)

    def reset_settings(self, instance=None) -> None:
        settings_manager.clear_data()
        txt.set_system_language()
        self.update_labels()
        music_manager.button_clicked.play()
        settings_manager.save_data()

    def return_in_main_menu(self, instance=None) -> None:
        questions_manager.status = True
        settings_manager.save_data()

        music_manager.button_clicked.play()
        music_manager.transition.play()

        self.manager.current = "MainMenu"
        self.manager.get_screen("MainMenu").update_labels()
        log.info("Settings Menu: Going to the next screen -> MainMenu.")

    def clear_stats(self, instance=None) -> None:
        music_manager.button_clicked.play()
        points_manager.clear_data()

    def next_song(self, instance=None) -> None:
        music_manager.button_clicked.play()
        music_manager.next_song()

    def rainbow_buttons(self, checkbox=None, value=False) -> None:
        if not value:
            settings_manager.rainbow_buttons = value
            return
        settings_manager.save_data()
        music_manager.button_clicked.play()

    def drawing_images(self, checkbox=None, value=False) -> None:
        if not value:
            settings_manager.drawing_images = value
            return
        settings_manager.save_data()
        music_manager.button_clicked.play()

    def set_language(self, checkbox=None, value=False) -> None:
        if not value:
            return

        if checkbox == self.english_checkbox:
            self.new_languge = "en-EN"
        elif checkbox == self.french_checkbox:
            self.new_languge = "fr-FR"
        elif checkbox == self.russian_checkbox:
            self.new_languge = "ru-RU"
        else:
            self.new_languge = "uk-UA"

        txt.set_language(self.new_languge)
        settings_manager.current_language = self.new_languge

        settings_manager.save_data()
        self.update_labels()
        music_manager.button_clicked.play()

    def set_color(self, checkbox=None, value=None) -> None:
        if not value:
            return

        if checkbox == self.blue_checkbox:
            settings_manager.menus_color = "blue"
        elif checkbox == self.orange_checkbox:
            settings_manager.menus_color = "orange"
        elif checkbox == self.violet_checkbox:
            settings_manager.menus_color = "violet"
        elif checkbox == self.pink_checkbox:
            settings_manager.menus_color = "pink"
        elif checkbox == self.yellow_checkbox:
            settings_manager.menus_color = "yellow"
        elif checkbox == self.cyan_checkbox:
            settings_manager.menus_color = "cyan"
        elif checkbox == self.grey_checkbox:
            settings_manager.menus_color = "grey"
        else:
            settings_manager.menus_color = "black"

        log.info(
            "Settings: The menus color was changed to "
            + str(settings_manager.menus_color)
        )

        settings_manager.color_change()
        self.update_labels()
        music_manager.button_clicked.play()

    def set_randomizing_style(self, checkbox=None, value=False) -> None:
        if not value:
            return

        if checkbox == self.normal_checkbox:
            settings_manager.randomizing_style = "normal"
        elif checkbox == self.alternative_checkbox_checkbox:
            settings_manager.randomizing_style = "alternative"
        else:
            settings_manager.randomizing_style = "in_order"

        settings_manager.save_data()
        music_manager.button_clicked.play()

    def show_popup(self, instance=None) -> None:

        def yes_action(instance=None) -> None:
            if self.current_text == txt.clear_stats:
                self.clear_stats()
            else:
                self.reset_settings()

            self.popup.dismiss()

        def close_popup(instance=None) -> None:
            self.popup.dismiss()

        if instance.text == txt.clear_stats:
            self.current_text = txt.clear_stats
        else:
            self.current_text = txt.reset_settings

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
