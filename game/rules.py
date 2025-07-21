"""Règles de pose pour le jeu Crapette Tarot."""

from __future__ import annotations

from typing import Dict, List, Optional

from .deck import Carte


COULEURS = ["♠", "♥", "♦", "♣"]


def get_couleur(carte: Carte) -> Optional[str]:
    """Retourne le symbole de couleur pour une carte de couleur."""
    if carte.type != "couleur":
        return None
    # Les cartes de couleur ont un nom du type "4 de ♥".
    return carte.nom.split()[-1]


def peut_poser(carte: Carte, pile: List[Carte]) -> bool:
    """Vérifie si `carte` peut être placée sur `pile`.

    - Les cartes doivent être posées dans l'ordre croissant.
    - Les fondations de couleur doivent également respecter la couleur.
    - L'Excuse ne peut être posée sur aucune pile.
    """

    if carte.type == "excuse":
        return False

    if not pile:
        if carte.type == "atout":
            return carte.valeur == 1
        if carte.type == "couleur":
            return carte.valeur == 1
        return False

    dessus = pile[-1]

    # Types différents -> pose impossible
    if carte.type != dessus.type:
        return False

    if carte.type == "atout":
        return carte.valeur == dessus.valeur + 1

    if carte.type == "couleur":
        if get_couleur(carte) != get_couleur(dessus):
            return False
        return carte.valeur == dessus.valeur + 1

    return False


def fondation_complete(pile: List[Carte]) -> bool:
    """Retourne ``True`` si la fondation de couleur est complète (1 à 14)."""
    if len(pile) != 14:
        return False
    couleur = get_couleur(pile[0])
    for index, carte in enumerate(pile, start=1):
        if carte.type != "couleur" or get_couleur(carte) != couleur:
            return False
        if carte.valeur != index:
            return False
    return True


def atouts_complets(pile: List[Carte]) -> bool:
    """Retourne ``True`` si la pile d'atouts est complète (1 à 21)."""
    if len(pile) != 21:
        return False
    for index, carte in enumerate(pile, start=1):
        if carte.type != "atout" or carte.valeur != index:
            return False
    return True


def partie_terminee(
    fondations: Dict[str, List[Carte]],
    pile_atouts: List[Carte],
    talons: List[List[Carte]],
) -> bool:
    """Détermine si la partie est terminée."""
    if not atouts_complets(pile_atouts):
        return False
    for couleur in COULEURS:
        if couleur not in fondations or not fondation_complete(fondations[couleur]):
            return False
    return all(len(talon) == 0 for talon in talons)

