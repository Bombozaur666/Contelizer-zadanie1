# Zadanie 1: Aplikacja Django do Przetwarzania Tekstu

Cel: Utwórz aplikację Django, która pozwala użytkownikowi przesłać plik tekstowy. Aplikacja powinna przeczytać plik, przemieszać litery w środku każdego wyrazu (pozostawiając pierwszą i ostatnią literę na swoich miejscach) i wyświetlić zmodyfikowany tekst użytkownikowi.

Funkcjonalności:
Strona główna zawiera formularz do przesyłania pliku tekstowego.
Po przesłaniu pliku, użytkownik jest przekierowywany na stronę z wynikiem, gdzie zmodyfikowany tekst jest wyświetlany.

# Wymagania

* Do popranego uruchomiania aplikacji należy utworzyć folder `static` w folderze `src`

# Uruchomienie aplikcaji

```bash
docker compose build
```

```bash
docker compose up -d
```

# Zamknięcie aplikacji
```bash
docker compose down
```