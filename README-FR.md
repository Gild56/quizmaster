# Application de Test de QI

Bonjour ! C'est un projet **multiplateforme** *(pour iOS, Android et Windows)*. Vous pourez **compléter des tests**, **collecter des points**, **écouter** votre **musique préférée**, **persaonnaliser tout à votre goût** et bien *plus* encore !

**Avant personnaliser le projet lisez la [LICENSE](LICENSE.md) !**

Back to the [english version](\..\..\..\README.md)

Allez voir les [crédits](credits.md) du projet.

Consultez le [changelog](changelog.md) pour voir toutes les mises à jour et les changements du projet.

Si une erreur s'est produite [le dossier des logs](\..\..\logs/) est là pour vous aider !

## Premiers Pas sur Windows 10 / 11

Pour commencer votre expérience avec le jeu, vous avez seulement besoin d'ouvrir le racourcis nommé `Quiz Master`.

## Personnalisation

Vous pouvez également personnaliser ce jeu - ajouter des polices, des images, des quiz, de la musique, etc.

**Actuellement, vous pouvez personnaliser le jeu uniquement sur Windows 10 / 11 !**

### Chansons personnalisées

Il y a d'excellentes chansons disponibles dans le jeu.

Mais, vous pouvez également ajouter vos propres chansons au jeu.

Pour ce faire, il vous suffit de mettre vos chansons dans le dossier `quizmaster/app/resources/music`.

**Pour appliquer vos changements, vous devez redémarrer le jeu !**

### Questions personnalisées

Si vous souhaitez personnaliser le quiz, c'est possible !

Il vous suffit d'aller dans `quizmaster/app/resources/databases` et de choisir la langue que vous souhaitez modifier.

Vous pouvez mettre ce que vous voulez, mais souvenez-vous que si vous ne configurez pas correctement les questions, cela peut ne pas fonctionner !

Pour configurer correctement vos questions, vous devez écrire :

"Votre question (elle peut être un peu longue et vous n'avez pas besoin d'inclure de sauts de ligne `\n`)", "La bonne réponse", "La mauvaise réponse n°1", "La mauvaise réponse n°2", "La mauvaise réponse n°3"

#### **Exemples :**

```python
# Comme ça :

"Quel animal est le symbole du champion de tennis René Lacoste ?", "Le crocodile", "Le panda", "Le jaguar", "Le puma"

# Ou comme ça :

"Sur les 250 marins partis en 1519 avec Magellan, combien sont revenus à Séville 3 ans plus tard ?", "18", "115", "249", "60"
```

### Ajouter une image à votre question

Pour ajouter une image, vous devez l'indiquer dans le fichier `quizmaster/app/resources/databases/images.csv`.

La ligne où vous mettez le nom de votre image doit correspondre exactement à la ligne de la question dans votre fichier de base de données.

Si vous souhaitez ajouter une image uniquement à certaines questions, laissez les lignes correspondantes vides.

#### **Exemples :**

```python
# Comme ça :

""
"magellan.jpg"
"calcium.jpeg"
""
"marseille.jpg"

# Et ainsi de suite...
```

Vous pouvez utiliser les formats `.jpeg`, `.jpg`, `.png`.

**Cela appliquera les images à toutes les langues !**

**Si la ligne n'est pas correctement configurée, cela peut faire planter le jeu ou ne pas fonctionner correctement !**

**Pour appliquer vos changements, vous devez redémarrer le jeu !**

### Polices personnalisées

Il est également possible d'ajouter des polices personnalisées.

Il y a deux polices dans le jeu par défaut :

1. La grande (appelée Pusab) est dans le dossier `quizmaster/app/resources/fonts` et s'appelle **`big_font.ttf`**.

2. La plus petite (appelée Aller) est dans le même dossier et s'appelle *`small_font.ttf`*.

Notez que vous devriez choisir des polices qui supportent les **lettres cyrilliques** (les polices par défaut sont des *versions cyrilliques* d'Aller et Pusab), sauf si vous n'allez pas vous en servir.

**Pour appliquer vos changements, vous devez redémarrer le jeu !**

## Contactez-moi

Pour me contacter :
* [mon Telegram](https://t.me/gild56) (Je regarde souvent)
* [mon Discord](https://discord.com/users/gild56) (Je regarde rarement)
* [mon Gmail](mailto:gild56gmd@gmail.com) (Je ne regarde jamais xD)
