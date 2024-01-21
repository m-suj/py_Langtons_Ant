## Projekt symulacji Mrówki Langtona, napisany w języku Python z użyciem biblioteki arcade.
Projekt powstał na zaliczenie przedmiotu Programowanie w Pythonie podczas I semestru informatyki na Uniwersytecie Dolnośląskim DSW we Wrocławiu.

---

### Opis projektu:
Program symuluje zachowanie automatu komórkowego znanego jako problem Mrówki Langtona. Automat jest skonstruowany następująco::
 - Dana jest nieskończona plansza, podzielona na kwadratowe komórki, z których każda jest w jednym z dwóch możliwych kolorów - białym lub czarnym.
 - Plansza jest oczywiście dwuwymiarowa, a umieszczony na niej obiekt będący mrówką może być zwrócony w jednym z czterech kierunków - góra, dół, prawo, lewo - 
oraz wie, w jaki sposób przejść na komórkę sąsiadującą z tą, na której w danej chwili znajduje się mrówka, zależnie od kierunku tej mrówki. 

Wspomniana mrówka jest obiektem, który początkowo znajduje się w pewnej komórce na planszy, realizującym pewien algorytm (jest kilka wersji tych algorytmów, które jednak dają analogiczne efekty) 
mający określać jej zachowanie na planszy:
 - Mrówka sprawdza, na jakim polu się znajduje 
 - Gdy pole jest czarne wtedy obraca się w prawo o 90°, natomiast gdy jest białe obraca się w lewo o 90°
 - Mrówka zmienia kolor pola, na którym obecnie się znajduje, na przeciwny, po czym przechodzi do kolejnej komórki robiąc krok do przodu
 - Cały proces powtarza się

Mając tak skonstruowany automat, można dokonać pewnych ciekawych obserwacji - od pewnego momentu ruch mrówki zaczyna być schematyczny, generujący wzór powtarzający się w nieskończoność: 
mrówka wpada w pewien cykl. Z pozornego chaosu, trwającego dość długi czas, dyktowanego przez kilku bardzo prostych i schematycznych reguł, nagle wyłania się porządek. 
Co ciekawsze, przy pewnych skończonych rozmieszczeniach czarnych komórek na planszy przed rozpoczęciem działania automatu, mrówka i tak prędzej czy później wpadnie w dokładnie ten sam schemat,
jednak nie udowodniono że jest to prawdą dla dowolnego skończonego stanu początkowego. Ciekawe są również obserwacje działania mrówki rozszerzone na więcej niż tylko 2 kolory, lub kilku mrówek jednocześnie - co również 
jest możliwe do zasymulowania w tym projekcie. 


---
### Skład projektu:
Projekt podzielony jest na 3 pliki źródłowe:
- main.py, gdzie uruchamiane jest okno gry z użyciem biblioteki arcade.py
- langtons_ant.py, w której znajdują się 3 klasy: Ant, Map, oraz klasa zarządzająca symulacją. Symulacja ta natomiast jest odpowiednio obsługiwana przez klasę MyWindow w main.py
- sim_settings.py, zawierający ustawienia i konfiguracje projektu, takie jak rozmiary okna i domyślna prędkość symulacji

---
**Autor projektu:**
Mateusz Sujewicz, student I semestru Informatyki na Uniwersytecie Dolnośląskim DSW we Wrocławiu