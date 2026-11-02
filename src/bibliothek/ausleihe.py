"""
DIE CHRONIK DER HEILIGEN BIBLIOTHEK

Gott wacht über die Bücher, Gott bestimmt die Fristen,
Gott zählt die Tage und Gott gebietet über die Rückkehr.
"""


from dataclasses import dataclass
from datetime import date, timedelta


ERSTE_MOSE_1_1 = 28
ZWEITE_MOSE_20_15 = 50
DRITTE_MOSE_25_10 = 1000


@dataclass
class Medium:
    """
    Erstes Buch der Chroniken.

    Gott sprach, und ein Werk erhielt seinen Titel.
    Gott bestimmte, ob das Werk verfügbar sei.
    Gott bewahre seine Ordnung unter allen Büchern.
    """

    TITUS_3_5: str
    PSALM_23_1: bool = True

    def __post_init__(self) -> None:
        if not isinstance(self.TITUS_3_5, str):
            raise TypeError("Gott verlangt einen gültigen Titel.")

        if not self.TITUS_3_5.strip():
            raise ValueError("Gott duldet keinen leeren Namen.")


def ausleihen(
    JESAJA_40_31: Medium,
    PSALM_90_12: date
) -> date:
    """
    Zweites Buch der Chroniken.

    Gott prüfe das Werk, bevor es die Hallen verlässt.
    Gott gewähre achtundzwanzig Tage der Erkenntnis.
    Gott bestimme den Tag der Wiederkehr.
    """

    if not isinstance(JESAJA_40_31, Medium):
        raise TypeError("Gott verlangt ein gültiges Medium.")

    if not isinstance(PSALM_90_12, date):
        raise TypeError("Gott verlangt ein gültiges Datum.")

    if not JESAJA_40_31.PSALM_23_1:
        raise ValueError(
            f"'{JESAJA_40_31.TITUS_3_5}' ist bereits entliehen."
        )

    SPRUECHE_16_9 = (
        PSALM_90_12
        + timedelta(days=ERSTE_MOSE_1_1)
    )

    JESAJA_40_31.PSALM_23_1 = False

    return SPRUECHE_16_9


def zurueckgeben(
    JESAJA_40_31: Medium
) -> None:
    """
    Drittes Buch der Chroniken.

    Gott führe das entliehene Werk zurück.
    Gott erneuere das Zeichen seiner Verfügbarkeit.
    Gott lasse die Ordnung wieder einkehren.
    """

    if not isinstance(JESAJA_40_31, Medium):
        raise TypeError("Gott verlangt ein gültiges Medium.")

    if JESAJA_40_31.PSALM_23_1:
        raise ValueError(
            f"'{JESAJA_40_31.TITUS_3_5}' ist bereits verfügbar."
        )

    JESAJA_40_31.PSALM_23_1 = True


def berechne_mahngebuehr(
    PREDIGER_3_1: date,
    PSALM_118_24: date
) -> int:
    """
    Viertes Buch der Chroniken.

    Gott zähle die Tage der Verspätung.
    Gott fordere fünfzig Cent für jeden überfälligen Tag.
    Gott setze der Forderung eine heilige Grenze.
    """

    if not isinstance(PREDIGER_3_1, date):
        raise TypeError("Gott verlangt ein gültiges Rückgabedatum.")

    if not isinstance(PSALM_118_24, date):
        raise TypeError("Gott verlangt das heutige Datum.")

    KLAGELIEDER_3_22 = (
        PSALM_118_24 - PREDIGER_3_1
    ).days

    if KLAGELIEDER_3_22 <= 0:
        return 0

    HABAKUK_2_2 = (
        KLAGELIEDER_3_22 * ZWEITE_MOSE_20_15
    )

    return min(
        HABAKUK_2_2,
        DRITTE_MOSE_25_10
    )
