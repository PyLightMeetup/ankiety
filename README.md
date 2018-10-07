# Ankiety uczestników PyLight

Amatorska analiza wyników ankiet uczestników spotkań PyLight.

By zobaczyć naszą analizę, otwórz plik Jupyter Notebook [feedback.ipynb](feedback.ipynb). GitHub renderuje pliki .ipynb bez problemu. Jeśli używasz urządzenia mobilnego, włącz wersję strony dla komputerów.

Możesz też pobrać nasze dane i przeprowadzić własną analizę. Musisz mieć jednak zainstalowanego Pythona i odpowiednie pakiety. Patrz: [Jupyter Notebook – wymagania](#jupyter-notebook-wymagania).

Folder [forms](forms) zawiera poszczególne formularze ankiet. Pytania lub możliwe odpowiedzi zmieniały w miarę jak lepiej poznawaliśmy naszych uczestników.

Plik [responses_merged.csv](responses_merged.csv) zawiera plik CSV z odpowiedziami.

## Czyszczenie danych

Zrobione:
- zmienić etykiety kolumn na brzmiące jak zmienne i spisać gdzieś pytania
- odwrócić wartości odpowiedzi pytań o przystępność prezentacji w formularzu nr 1. Oryginalnie wartość `1` znaczyła "łatwa w zrozumieniu", a `5` – "trudna".
- usunąć sygnaturę czasową
- dodać kolumnę `meetup` i wpisać wartość (`000`) równą numerowi spotkania
- połączyć pliki CSV w jeden, uzupełniany po każdej ankiecie
- usunąć dodatkowe komentarze dla prowadzących i sugestie nowych tematów

Dodawanie wyników kolejnych ankiet:
- TBD (poskładać z powyższych kroków)

## Pytania (legenda)

Oto jak poszczególne pytania zostały zakodowane w wynikach. Cyfry w nawiasach oznaczają w której ankiecie to pytanie się pojawiło, jeśli nie zostało zadane we wszystkich ankietach.

Spotkanie nr 6 miało postać panelu, więc pytania nieco się różniły.

Pytania oryginalnie zawierały zarówno formy męskie i żeńskie. Tu dla wygody zostawiono formy żeńskie.

| Zmienna | Brzmienie pytania | Numer ankiety | Uwagi |
|---------|-------------------|---------------|-------|
| `meetup`  | "Numer meetupu" | N/A |  |
| `skad`  | "Gdzie usłyszałaś o PyLight?"" |  |  |
| `sex`   | "Twoja płeć to:" |  |  |
| `wiek1` | "Ile masz lat?" | 1-2 | 18-30 stanowi jedną grupę wiekową |
| `wiek2` | "Ile masz lat?" | 3- | grupa 18-30 została rozbita na 18-24 i 25-30 |
| `freq1` | "W ilu spotkaniach PyLight uczestniczyłaś przed tym spotkaniem?" | 6 | możliwe odpowiedzi: 5, 4, 3, 2, 1, "To mój pierwszy raz na PyLight!" |
| `freq2` | "W ilu spotkaniach PyLight uczestniczyłaś przed tym spotkaniem?" | 8- | możliwe odpowiedzi: "To moje pierwsze!", "1-3", "więcej niż 3" |
| `cel` | "Python jest używany do różnych zadań. W jakich obszarach chciałabyś wykorzystywać Pythona?" | 1 |  |
| `widz` | "Czy widziałaś prezentacje z ostatniego spotkania?" |  | możliwe odpowiedzi: "Tak, na żywo", "Tak, na YouTube", "Nie" (później w wersji "Nie, ale lubię ankiety") |
| `prez1-przyst` | "Jak oceniasz przystępność prezentacji nr 1" |  |  |
| `prez1-przyd` | "Jak oceniasz przydatność prezentacji nr 1 na Twoim poziomie i dla Twoich potrzeb?" |  |  |
| `prez2-przyst` | "Jak oceniasz przystępność prezentacji nr 2" |  |  |
| `prez2-przyd` | "Jak oceniasz przydatność prezentacji nr 2 na Twoim poziomie i dla Twoich potrzeb?" |  |  |
| `panel-przyst` | "Jak oceniasz przystępność wypowiedzi panelistów?" | 6 |  |
| `panel-przyd` | "Jak oceniasz przydatność wypowiedzi panelistów na Twoim poziomie i dla Twoich potrzeb?" | 6 |  |
| `panel-future` | "Rozważamy organizację panelu dyskusyjnego ponownie za kilka spotkań. Jak podoba Ci się ten pomysł?" | 6 | Odpowiedzi w skali 1 ("Nie podoba mi się. Trzymajcie się dotychczasowego formatu – krótkie prezentacje") do 5 ("Super!") |
| `znajomosc` | "Jaka jest Twoja znajomość Pythona?" | 1 | Możliwe wiele odpowiedzi |
| `ang` | "Dopuszczamy możliwość wygłaszania prezentacji po angielsku. Czy jesteś w stanie korzystać z materiałów w tym języku?" | 1 |  |
| `druk` | "Co myślisz o drukowanych prezentacjach rozdawanych w trakcie spotkania?" | 3-4 |  |
| `temat` | "Zasugeruj temat na kolejne spotkania" | 3- | pytanie otwarte |

## Jupyter Notebook – wymagania

Wymagane pakiety:

- Python 3 (użyto 3.7)
- `jupyter`
- `pandas`
