"""Module de gestion du paquet de cartes pour le jeu Crapette Tarot."""

from dataclasses import dataclass
from typing import List
import random


@dataclass
class Carte:
    """Représente une carte de tarot."""

    nom: str
    valeur: int
    type: str  # "atout", "excuse" ou "couleur"

    def __repr__(self) -> str:
        return f"{self.nom} ({self.type})"


class Deck:
    """Paquet de 78 cartes pour le tarot."""

    def __init__(self) -> None:
        self.cartes: List[Carte] = []
        self._creer_deck()

    def _creer_deck(self) -> None:
        """Génère les 78 cartes du paquet."""
        # Atouts 1 à 21
        for valeur in range(1, 22):
            nom = f"Atout {valeur}"
            self.cartes.append(Carte(nom=nom, valeur=valeur, type="atout"))

        # Excuse (Joker)
        self.cartes.append(Carte(nom="Excuse", valeur=0, type="excuse"))

        # Cartes de couleur
        couleurs = ["♠", "♥", "♦", "♣"]
        noms = [
            ("1", 1),
            ("2", 2),
            ("3", 3),
            ("4", 4),
            ("5", 5),
            ("6", 6),
            ("7", 7),
            ("8", 8),
            ("9", 9),
            ("10", 10),
            ("Valet", 11),
            ("Cavalier", 12),
            ("Dame", 13),
            ("Roi", 14),
        ]

        for couleur in couleurs:
            for nom, valeur in noms:
                carte_nom = f"{nom} de {couleur}"
                self.cartes.append(
                    Carte(nom=carte_nom, valeur=valeur, type="couleur")
                )

    def shuffle(self) -> None:
        """Mélange le paquet de cartes."""
        random.shuffle(self.cartes)

    def draw(self) -> Carte:
        """Pioche une carte du dessus du paquet."""
        if not self.cartes:
            raise IndexError("Le paquet est vide")
        return self.cartes.pop()

    def __len__(self) -> int:
        return len(self.cartes)
