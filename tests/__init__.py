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

*** fichier : test_points_allowed.py
    2 tests :
    - Lors de la réservation, si la demande du nombre de places est inférieure au nombre de points
    disponibles, alors le message 'Great-booking complete!' s'affiche.
    - Lors de la réservation, si la demande du nombre de places est supérieure au nombre de points
    disponibles, alors le message 'You can't redeem more points than available.' s'affiche.


*** fichier : test_places_less_than_12.py
    2 tests :
    - Si la demande de réservation est de moins de 12 places elle est effectuée et
    le message 'Great-booking complete!' s'affiche.
    - Si la demande de réservation est de plus de 12 places elle n'est pas effectuée et
    le message d'alert 'You can't request more than 12 places.' s'affiche.


*** fichier : test_point_updated.py
    3 tests :
    - Teste la mise à jour du nombre de points disponibles pour le club.
    - Teste la possibilité d'utiliser tous les points disponibles d'un club.
    - Lorsque le concours est complet, le lien 'Book Places' est remplacé par le message
    'This contest is full'


*** fichier : test_competitions_dates.py
    2 tests :
    - Lorsque la date de la compétition est passée, le lien 'Book Places' est remplacé par
    le message 'Past competition'
    - Lorsque la date de la compétition est à venir, le lien 'Book Places' apparait sur la page
"""
