"""Collegamento al database SQLite.

SQLite salva tutto il database in un unico file (`spazi.db`) nella cartella
del sito: non serve installare un server di database a parte.

Le tabelle (utenti, spazi, prenotazioni) e gli spazi di esempio verranno
aggiunti nel passo successivo della checklist (ruolo C).
"""

import sqlite3
from pathlib import Path

PERCORSO_DB = Path(__file__).with_name("spazi.db")


def connessione():
    """Apre una connessione al database; le righe si leggono come dizionari."""
    conn = sqlite3.connect(PERCORSO_DB)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def inizializza():
    """Crea il file del database se non esiste ancora.

    Per ora non crea tabelle: lo schema arriva con il compito "Database".
    """
    with connessione() as conn:
        conn.execute("SELECT 1")
