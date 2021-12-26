# News scraper
Ohjelma mahdollistaa datan keräyksen annetuista uutislähteistä. Data voidaan tallentaa tietokantaan josta sitä voi hakea ja tarvitaessa jatkojalostaa erinäisiin käyttötarkoituksiin.

## Asennus ja kirjastot
Sovellus on rakennettu Python versiolla 3.8 

Käytetyt kirjastot: Beautifulsoup ja requests

## Komentorivitoiminnot
Ohjelman suoritus:

```poetry run invoke start```

Ohjelman testaus:

```poetry run invoke test```

Testikattavuusraportin muodostus

```poetry run invoke coverage-report```

## Pylint
Ohjelmiston rakenteen tarkastelu:

```poetry run invoke lint```

## Dokumentaatio
-[Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)

-[Tuntiaikakirjanpito](dokumentaatio/tuntikirjanpito.md)

-[Release](https://github.com/jjuliacaroline/ot-harkka/releases/tag/viikko5)

-[Arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)

-[Käyttöohje](dokumentaatio/kauttoohje.md)

-[Testausdokumentti](dokumentaatio/testaus.md)