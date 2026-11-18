"""Server del sito: avvia Flask, serve le pagine e risponde alle API.

Avvio: `python app.py`, poi aprire http://127.0.0.1:5000 nel browser.

- Le pagine (HTML, CSS, JavaScript) stanno nella cartella `static/` (ruolo D).
- Le API, cioè gli indirizzi che iniziano con `/api/` e rispondono in JSON,
  stanno in questo file (ruolo C).
"""

from flask import Flask, jsonify

import database

app = Flask(__name__, static_folder="static", static_url_path="")


@app.get("/")
def home():
    """Pagina principale del sito."""
    return app.send_static_file("index.html")


@app.get("/api/stato")
def stato():
    """Controllo veloce: dice se il server e il database rispondono."""
    with database.connessione() as conn:
        conn.execute("SELECT 1")
    return jsonify({"server": "ok", "database": "ok"})


if __name__ == "__main__":
    database.inizializza()
    app.run(debug=True)
