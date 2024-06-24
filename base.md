Le fichier `root.py` dans le dossier `views` permet de créer la fenêtre principale de l'application. Il contient la classe `Root` qui hérite de `tk.Tk` et qui est responsable de la création de la fenêtre principale de l'application.

Le fichier `base.py` dans le dossier `models` contient la classe `ObservableModel` qui est la classe de base pour les modèles observables. Cette classe contient un dictionnaire `_event_listeners` qui stocke les écouteurs d'événements. Elle contient également les méthodes `add_event_listener` et `trigger_event` qui permettent respectivement d'ajouter un écouteur d'événement et de déclencher un événement.

Les fichiers à l'intérieur de `views` permettent de créer les différentes vues de l'application.

Il est important de noter que les vues ne contiennent pas de "logique" métier. Elles se contentent d'afficher les données et de réagir aux événements.

Le fichier `main.py` dans le dossier `views` permet de switcher entre les différentes vues de l'application.

Dans la méthode `__init__`, nous initialisons un dictionnaire nommé `frames` qui va stocker tous les frames (pages) de notre application. Nous avons défini une méthode `_add_frame` pour initialiser et stocker les frames. La façon dont nous plaçons les frames dans la fenêtre principale est de les empiler les uns sur les autres. `sticky='nsew'` va garantir que chaque frame va couvrir toute la fenêtre principale, de sorte que les éléments des autres frames en dessous ne peuvent pas être vus.

La méthode `switch` va gérer la transition entre les pages. Lorsque nous passons le nom du frame à cette fonction, elle va faire avancer ce frame en appelant la méthode `tkraise`.

Le fichier `home.py` dans le dossier `controllers` contient la classe `HomeController` qui est responsable de la logique de la page d'accueil.
