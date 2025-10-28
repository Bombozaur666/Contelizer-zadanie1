# Zadanie 2: Walidator PESEL w Aplikacji Django
Cel: Utwórz aplikację Django, która pozwala użytkownikowi wprowadzić numer PESEL do formularza. Aplikacja powinna zweryfikować numer PESEL zgodnie z oficjalną specyfikacją i wyświetlić użytkownikowi informację o poprawności numeru.

Funkcjonalności:
Strona główna zawiera formularz do wprowadzania numeru PESEL.
Po wprowadzeniu numeru, aplikacja wyświetla informacje o tym, czy numer PESEL jest poprawny czy nie, a także dodatkowe informacje, takie jak data urodzenia i płeć.

# Wymagania

* Do popranego uruchomiania aplikacji należy utworzyć folder `static` w folderze `src`


# Uruchomienie aplikcaji

```bash
docker compose build
```

```bash
docker compose up -d
```

# Pierwsze uruchomienie
 Po uruchomieniu contenera wejść do kontenera `django` komendą:
```bash
docker compose run -it django /bin/sh
```

następnie zrobić migracje komendą:
```bash
python manage.py migrate
```
wyjście z kontenera
```bash
exit
```

# Zamknięcie aplikacji
```bash
docker compose down
```