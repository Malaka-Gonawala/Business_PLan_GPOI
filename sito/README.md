# Sito web (MVP)

Versione minima funzionante della piattaforma descritta in [IDEA.md](../IDEA.md): stanze, studi e appartamenti da affittare a ore. Cosa entra nel sito e cosa resta fuori è scritto in [CHECKLIST.md](../CHECKLIST.md).

## Lo stack scelto: Python + Flask + SQLite

Lo *stack* è l'insieme dei programmi e dei linguaggi con cui è costruito il sito.

| Parte | Strumento | Perché |
|---|---|---|
| Backend (il server) | **Python** con **Flask** | Python si studia a scuola ed è facile da leggere; Flask è un *framework* (una base già pronta per costruire siti) piccolo, con una sola libreria da installare. |
| Database | **SQLite** | È già incluso in Python: tutto il database sta in un unico file, senza server da installare o configurare. |
| Frontend (le pagine) | **HTML, CSS e JavaScript** senza librerie | Nessuno strumento in più da imparare: le pagine chiedono i dati al server tramite le API. |

Rispetto all'alternativa Node.js + Express + SQLite, questa scelta evita librerie da compilare per SQLite e richiede un solo pacchetto (`Flask`).

## Come avviare il sito

Serve **Python 3.10 o successivo** ([python.org](https://www.python.org/downloads/)). Dalla cartella `sito/`:

```bash
# 1. Una sola volta: creare l'ambiente virtuale e installare Flask
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS / Linux:
source venv/bin/activate
pip install -r requirements.txt

# 2. Ogni volta: avviare il server
python app.py
```

Poi aprite **http://127.0.0.1:5000** nel browser. Se la pagina mostra "Server: ok · Database: ok", tutto funziona.

L'*ambiente virtuale* (`venv`) è una cartella che contiene le librerie solo per questo progetto, senza toccare il resto del computer. Su macOS e Linux potrebbe servire `python3` al posto di `python`.

## Struttura della cartella

| File | Cosa contiene | Ruolo |
|---|---|---|
| `app.py` | Avvio del server e API (indirizzi `/api/...` che rispondono in JSON) | C |
| `database.py` | Collegamento al database SQLite (`spazi.db`, creato all'avvio) | C |
| `requirements.txt` | Librerie Python da installare | C |
| `static/index.html` | Pagina principale | D |
| `static/stile.css` | Stile delle pagine | D |
| `static/app.js` | Codice JavaScript delle pagine, che chiama le API | D |

Il file `spazi.db` non va nel repository (è escluso da `.gitignore`): ognuno ha il proprio database locale.

## API disponibili

| Metodo | Indirizzo | Cosa fa |
|---|---|---|
| GET | `/api/stato` | Dice se server e database rispondono |

Le altre API (registrazione, login, spazi, prenotazioni) arrivano con i compiti successivi della checklist.

## Nota sul nome

"Spazi a ore" nel titolo della pagina è un nome provvisorio: il nome della startup è ancora da decidere.
