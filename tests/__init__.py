"""
     ### Plan de tests

*** fichier : test_email.py
    5 tests :
    - La saisie d'un mail valide (présent dans les données des clubs) permet de se connecter.
    - La saisie d'un mail non valide (non présent dans les données des clubs),
    provoque l'affichage du message: "Sorry, that email wasn't found.".
    - Si le champ 'email' reste vide, alors le message: "Sorry, that email wasn't found." s'affiche.
    - Si le champ 'email' est complété avec une chaine de caratère quelconque,
    alors le message: "Sorry, that email wasn't found." s'affiche.
    - S'il existe plusieurs clubs avec le même email alors le message "Email must be unique." s'affiche.

"""
