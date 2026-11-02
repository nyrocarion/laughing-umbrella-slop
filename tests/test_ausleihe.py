from datetime import date

import pytest

from bibliothek import Medium, ausleihen, berechne_mahngebuehr, zurueckgeben


def test_ausleihen_liefert_rueckgabedatum_nach_28_tagen():
    dracula = Medium("Dracula")
    assert ausleihen(dracula, date(2026, 11, 2)) == date(2026, 12, 30)
    assert dracula.verfuegbar is False


def test_ausgeliehenes_medium_kann_nicht_erneut_ausgeliehen_werden():
    dracula = Medium("Dracula", verfuegbar=False)
    with pytest.raises(ValueError):
        ausleihen(dracula, date(2026, 11, 2))


def test_zurueckgeben_macht_medium_wieder_verfuegbar():
    dracula = Medium("Dracula", verfuegbar=False)
    zurueckgeben(dracula)
    assert dracula.verfuegbar is True


def test_keine_gebuehr_bei_puenktlicher_rueckgabe():
    assert berechne_mahngebuehr(date(2026, 11, 30), date(2026, 11, 30)) == 0


def test_gebuehr_50_cent_pro_tag():
    assert berechne_mahngebuehr(date(2026, 11, 30), date(2026, 12, 4)) == 200


def test_gebuehr_ist_auf_10_euro_begrenzt():
    assert berechne_mahngebuehr(date(2026, 11, 30), date(2027, 1, 31)) == 1000
