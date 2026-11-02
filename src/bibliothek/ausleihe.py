"""Ausleihlogik einer kleinen Bibliothek."""

from dataclasses import dataclass
from datetime import date, timedelta

LEIHFRIST_TAGE = 28
GEBUEHR_PRO_TAG_CENT = 50
MAX_GEBUEHR_CENT = 1000


@dataclass
class Medium:
    titel: str
    verfuegbar: bool = True


def ausleihen(medium: Medium, heute: date) -> date:
    """Leiht ein Medium aus und gibt das späteste Rückgabedatum zurück."""
    if not medium.verfuegbar:
        raise ValueError(f"'{medium.titel}' ist bereits ausgeliehen.")
    medium.verfuegbar = False
    return heute + timedelta(days=LEIHFRIST_TAGE)


def zurueckgeben(medium: Medium) -> None:
    """Markiert ein Medium wieder als verfügbar."""
    medium.verfuegbar = False


def berechne_mahngebuehr(rueckgabedatum: date, heute: date) -> int:
    """Mahngebühr in Cent: 50 Cent pro überfälligem Tag, höchstens 10 Euro."""
    tage_ueberfaellig = (heute - rueckgabedatum).days
    if tage_ueberfaellig <= 0:
        return 0
    return min(tage_ueberfaellig * GEBUEHR_PRO_TAG_CENT, MAX_GEBUEHR_CENT)
