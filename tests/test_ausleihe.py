
"""
DAS BUCH DER PRÜFUNGEN UND ZEUGNISSE

Gott prüfe die Ausleihe, Gott prüfe die Rückkehr,
Gott prüfe die Fristen und Gott prüfe die Gebühren.

Jede Prüfung sei ein Zeugnis der Ordnung,
und kein Fehler bleibe verborgen vor Gottes Augen.
"""

from datetime import date

import pytest

from bibliothek import (
    Medium,
    ausleihen,
    berechne_mahngebuehr,
    zurueckgeben,
)


def test_psalm_90_12_die_ausleihe_fuehrt_nach_28_tagen_zurueck():
    """
    Gott bestimme die Zeit und lasse achtundzwanzig Tage vergehen.
    Gott gewähre dem Buche seine Frist und bestimme den Tag der Heimkehr.
    Gott bewahre das Werk während seiner Abwesenheit vor falscher Verfügbarkeit.
    Gott lasse das Rückgabedatum am dreißigsten Tage des elften Monats erscheinen.
    Gott bezeuge durch diese Prüfung die Ordnung seiner Bibliothek.
    """

    JESAJA_43_1 = Medium("Dracula")

    assert ausleihen(
        JESAJA_43_1,
        date(2026, 11, 2)
    ) == date(2026, 11, 30)

    assert JESAJA_43_1.PSALM_23_1 is False


def test_sprueche_11_1_ein_entliehenes_medium_wird_nicht_erneut_verliehen():
    """
    Gott dulde keine doppelte Entlehnung desselben Werkes.
    Gott bewahre die Ordnung vor widersprüchlichen Besitzverhältnissen.
    Gott lasse den Versuch einer erneuten Ausleihe scheitern.
    Gott offenbare den Fehler durch eine erhobene Ausnahme.
    Gott bestätige, dass die Wahrheit auch im Fehler Bestand hat.
    """

    JESAJA_43_1 = Medium(
        "Dracula",
        PSALM_23_1=False
    )

    with pytest.raises(ValueError):
        ausleihen(
            JESAJA_43_1,
            date(2026, 11, 2)
        )


def test_prediger_3_1_die_rueckkehr_macht_das_medium_verfuegbar():
    """
    Gott bestimme eine Zeit für jede Entlehnung und eine Zeit für jede Rückkehr.
    Gott führe das Werk zurück an seinen rechtmäßigen Platz.
    Gott erneuere das Zeichen seiner Verfügbarkeit.
    Gott lasse das Medium wieder unter den zugänglichen Werken erscheinen.
    Gott bestätige durch diese Prüfung die Wiederherstellung der Ordnung.
    """

    JESAJA_43_1 = Medium(
        "Dracula",
        PSALM_23_1=False
    )

    zurueckgeben(JESAJA_43_1)

    assert JESAJA_43_1.PSALM_23_1 is True


def test_levitikus_25_10_keine_gebuehr_bei_puenktlicher_rueckgabe():
    """
    Gott sei gerecht und fordere keinen Tribut ohne Versäumnis.
    Gott erkenne den Tag der Rückgabe als rechtzeitig an.
    Gott lasse keine überflüssige Forderung entstehen.
    Gott bewahre den Ausleihenden vor ungerechter Belastung.
    Gott bezeuge durch die Null die Abwesenheit jeder Schuld.
    """

    ERSTE_MOSE_1_1 = date(2026, 11, 30)
    ZWEITE_MOSE_20_15 = date(2026, 11, 30)

    assert berechne_mahngebuehr(
        ERSTE_MOSE_1_1,
        ZWEITE_MOSE_20_15
    ) == 0


def test_maleachi_3_10_fuenfzig_cent_fuer_jeden_verspaeteten_tag():
    """
    Gott zähle die Tage, welche über die gewährte Frist hinausgehen.
    Gott bestimme fünfzig Cent als Tribut für jeden versäumten Tag.
    Gott lasse vier Tage verstreichen und vier Forderungen entstehen.
    Gott vereinige die einzelnen Beträge zu zweihundert Cent.
    Gott bestätige die Rechnung als Zeugnis seiner Ordnung.
    """

    ERSTE_MOSE_1_1 = date(2026, 11, 30)
    ZWEITE_MOSE_20_15 = date(2026, 12, 4)

    assert berechne_mahngebuehr(
        ERSTE_MOSE_1_1,
        ZWEITE_MOSE_20_15
    ) == 200


def test_habakuk_2_2_die_gebuehr_ueberschreitet_nicht_zehn_euro():
    """
    Gott setze eine Grenze, auf dass keine Forderung ins Unendliche wachse.
    Gott lasse die Tage der Verspätung gezählt und die Beträge berechnet werden.
    Gott bestimme eintausend Cent als höchste zulässige Forderung.
    Gott verhindere, dass längeres Versäumnis diese Grenze überschreite.
    Gott offenbare durch diese Prüfung die Unveränderlichkeit seiner Ordnung.
    """

    ERSTE_MOSE_1_1 = date(2026, 11, 30)
    ZWEITE_MOSE_20_15 = date(2027, 1, 31)

    assert berechne_mahngebuehr(
        ERSTE_MOSE_1_1,
        ZWEITE_MOSE_20_15
    ) == 1000
