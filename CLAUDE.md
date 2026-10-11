# Mini-trans by ŁL — instrukcje dla Claude

Gra kolejowa w jednym pliku `index.html` (HTML + CSS + JS, bez budowania). To jest jedyne źródło gry.
Strona: https://lukasz306.github.io/mini-trans/ (GitHub Pages z gałęzi `main`, katalog główny).

## Zasady pracy
- Odpowiadaj po polsku, zwięźle: co zmienione, dlaczego, wyniki testów.
- Przed zmianą funkcji lub zasad gry zadaj pytania doprecyzowujące (do 4, z opcją polecaną na pierwszym miejscu). Czyste poprawki błędów — bez pytań.
- Wersjonowanie: drobna zmiana → podbij ostatnią cyfrę (np. 0.926 → 0.927). Większy zestaw funkcji → nowy numer i krótki, powściągliwy wpis w `CHANGELOG` (w pliku, przy `GAME_VER`). Bez wpisów o easter eggach i nieodkrytych liniach.
- Numer wersji jest w trzech miejscach: `const GAME_VER=`, `<title>` oraz napis w logo (`by ŁL · v… ·`).
- Tryb Test jest ukryty: uruchamia go hasło wpisane w pole „Kod zapisu” (funkcja `testKey`, w kodzie tylko skrót SHA-256). Nie wpisuj hasła do repozytorium.

## Testy
`pip install playwright` (Chromium), potem `python3 regress.py` — 3 tryby gry, scenariusz Test i zapisy `save_*.txt`. Wynik musi być „BŁĘDY: 0”.
Przy poprawkach symulacji odtwórz problem na zapisie gracza (kod `MT1:…` wczytywany przez `parseSave` + `loadSaveData`), porównaj przed/po.

## Publikacja (po każdej wersji, automatycznie)
1. Commit i push `index.html` na `main` (GitHub Pages odświeży się w 1–2 min).
2. Artefakt claude.ai: https://claude.ai/artifact/JvjHnWWbaGVUmBenq9ddES — najpierw `Artifact` z `action: "read"` tego URL (wymóg przy pierwszej publikacji z nowej rozmowy), potem publikuj `index.html` z `url` tego artefaktu i `label: "v0.XXX"`. Bez `capabilities` (zostają zapisane: downloads, db, user — zapisy na koncie claude.ai).
3. Jeśli publikacja zostanie odrzucona z powodu nowszej wersji — scal zmiany z wersją live, nie nadpisuj.
