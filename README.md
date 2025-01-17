# Quiz Master App<!-- omit from toc -->

## Table of Contents<!-- omit from toc -->

- [First Steps on Windows 10 / 11](#first-steps-on-windows-10--11)
- [Personalization](#personalization)
  - [Custom songs](#custom-songs)
  - [Custom questions](#custom-questions)
  - [Add an image to your question](#add-an-image-to-your-question)
  - [Custom fonts](#custom-fonts)
- [Contact me](#contact-me)

## Hello!<!-- omit from toc -->

It's a **cross-platform** *(iOS, Android & Windows)* project. You can **complete tests**, **collect points**, **presonalize all** for your taste, listen your **favorite music** and much *more*!

![Quiz Master](app/resources/images/logo.ico)

**Before presonalizing the project, read the [LICENSE](LICENSE.md)!**

Go check the [credits](app/resources/markdown/credits.md) of the project.

Check the [changelog](app/resources/markdown/changelog.md) to see all the updates and changes of the project.

If an error occured, the [the logs folder](logs/) file is here to help!

## First Steps on Windows 10 / 11

To start your experience with the game, you can just run the `play.vbs` file or `play.bat` file if it don't works, which are in the `command` folder.

## Personalization

You can also personalize this game - add some fonts, images, quizzes, music, etc.

**Currently, you can personalize the game only on Windows 10 / 11!**

### Custom songs

There are great songs available in the game.

But, you can also add your own songs to the game.

To do this, you just need to put your songs in the `quizmaster/app/resources/music` folder.

**To apply your changes, you need to restart the game!**

### Custom questions

If you want to customize the quiz, you can!

You just need to go in the `quizmaster/app/resources/databases` and choose the language you want to change.

You can put anything, but remember that if you don't set the questions correctly, it may not work!

To set your questions correctly you must write:

"Your question (it can be a bit long and you don't need to include `\n` line breaks)","The true answer","The wrong answer №1","The wrong answer №2","The wrong answer №3"

**Examples:**

```python
# Like that:

"What animal is the symbol of the former tennis champion René Lacoste?","The crocodile","The panda","The jaguar","The puma"

# Or that:

"Out of 250 sailors who left in 1519 with Magellan, how many returned to Seville 3 years later?","18","115","249","60"
```

### Add an image to your question

To add an image, you must indicate it in the `quizmaster/app/resources/databases/images.csv`

The line where you put the name of your image must match the exact line of the question in your database file.

If you want to add an image to only certain questions, leave the corresponding lines empty.

**Examples:**

```python
# Like that:

""
"magellan.jpg"
"calcium.jpeg"
""
"marseille.jpg"

# And so on...
```

You can use the `.jpeg`, `.jpg`, `.png` formats, the others may not be supported.

**This will apply the images to all languages!**

**If the line isn't set correctly, it may not work correctly!**

**To apply your changes, you need to restart the game!**

### Custom fonts

It is also possible to add some custom fonts.

There are two fonts in the vanilla game:

1. The big one (called Pusab) is in the `quizmaster/app/resources/fonts` folder and called **`big_font.ttf`**.

2. The smaller one (called Aller) is in the same folder and called *`small_font.ttf`*.

Note that you should choose fonts that support **Cyrillic letters** (as the default ones are *Cyrillic versions* of Aller and Pusab), except if you will not need it.

**To apply your changes, you need to restart the game!**

## Contact me

To contact me:

- [my Telegram](https://t.me/gild56)
- [my Discord](https://discord.com/users/gild56)
- [my Gmail](mailto:gild56gmd@gmail.com)
