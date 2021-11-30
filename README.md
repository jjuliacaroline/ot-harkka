# News scraper
Ohjelma mahdollistaa datan keräyksen annetuista uutislähteistä. Data voidaan tallentaa tietokantaan josta sitä voi hakea ja jatkojalostaa erinäisiin tarpeisiin.

## Asennus ja kirjastot
Sovellus on rakennettu Python versiolla 3.8 
Käytetyt kirjastot: Beautifulsoup ja requests

## Komentorivitoiminnot
Ohjelman suoritus:
```poetry run invoke start```
Ohjelman testaus:
```poetry run invoke test```
Testikattavuusraportin muodostus
```poetry run invoke coverage_report```

## Pylint
Ohjelmiston rakenne voidaan kuvata komennolla:
```poetry run invoke lint```

# Dokumentaatio
-[Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
-[Tuntiaikakirjanpito](dokumentaatio/tuntikirjanpito.md)