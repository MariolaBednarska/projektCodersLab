Projekt „Katalog Książek” to aplikacja webowa stworzona w frameworku Django, 
służąca do zarządzania zbiorami książek. Aplikacja umożliwia użytkownikom dodawanie, 
ocenianie, kategoryzowanie książek, a także śledzenie ich statusu 
(np. przeczytana, w trakcie czytania, wypożyczona).


Instalacja
Aby zainstalować i uruchomić aplikację, postępuj zgodnie z poniższymi krokami:
1. Sklonuj repozytorium: git clone https://github.com/your-username/katalog-ksiazek.git

2. Zainstaluj zależności:
W katalogu głównym projektu uruchom: pip install -r requirements.txt

3. Utwórz bazę danych:
Uruchom migracje, aby utworzyć odpowiednie tabele w bazie danych: python manage.py migrate

4. Uruchom serwer deweloperski: python manage.py runserver


Technologie
Projekt jest zbudowany z użyciem następujących technologii:
1. Django: Framework do budowania aplikacji webowych w Pythonie.
2. HTML/CSS: Do tworzenia i stylizacji szablonów HTML.
3. SQLite: Wbudowana baza danych dla lokalnego środowiska deweloperskiego (można zmienić na inną bazę danych, np. PostgreSQL).

Aplikacja oferuje następujące funkcjonalności:
1. Zarządzanie książkami: Użytkownicy mogą dodawać nowe książki do katalogu, podając tytuł, autora, rok publikacji, ocenę oraz przypisując książki do półki na regale.
2. Kategorie książek: Użytkownicy mogą przypisać książki do jednej lub więcej kategorii literackich, takich jak fantastyka, kryminał, literatura piękna, biografie itp.
3. Oceny książek: Użytkownicy mogą oceniać książki w skali od 1 do 5 gwiazdek.
4. Status książki: Użytkownicy mogą śledzić status książki, np. czy jest to książka nieprzeczytana, w trakcie czytania, przeczytana, czy wypożyczona.
5. Wyszukiwanie książek: Aplikacja pozwala na wyszukiwanie książek według tytułu, autora lub kategorii.
6. Wyświetlanie książek na regale: Możliwość wyświetlania książek przypisanych do konkretnej półki regału.