# Checklist del Business Plan

**Scadenza: mercoledì 25/11/2026**: presentazione di gruppo del lavoro svolto.

> **Piano ridotto (18/11/2026):** manca una settimana. La checklist è stata ridotta all'essenziale e divisa per giorni. Ci sono due percorsi in parallelo:
> - **Relazione** (le 5 sezioni richieste dalla traccia) e **presentazione**;
> - **Sito web funzionante con backend**: una versione minima (MVP, *Minimum Viable Product*, cioè il prodotto più semplice che funziona davvero) della piattaforma descritta in [IDEA.md](IDEA.md).

Spuntate le voci man mano che vengono completate (`- [x]`) e aggiungete accanto il vostro nome.

**🟢 = senza codice e senza AI:** la voce si può fare con un browser, un foglio di calcolo o un programma di scrittura. Non servono programmazione, strumenti di intelligenza artificiale né un computer potente.

## Divisione dei ruoli

Ognuno scrive il proprio nome accanto al ruolo (giorno 1).

| Ruolo | Chi | Si occupa di |
|---|---|---|
| **A**: relazione, parte 1 | _(nome)_ | Sezioni 1, 2 e 4, coordinamento della relazione |
| **B**: relazione, parte 2 | _(nome)_ | Sezioni 3 e 5 (mercato e numeri) |
| **C**: sito, backend | _(nome)_ | Server, database, API (le "porte" con cui il sito parla con il server), login |
| **D**: sito, frontend | _(nome)_ | Pagine del sito, collegamento al backend, demo |

Le slide si fanno **tutti insieme** (giorni 6 e 7): ognuno prepara le slide della propria parte.

## Cosa entra nel sito (e cosa no)

**Dentro (MVP):** registrazione e login; elenco degli spazi con filtri semplici (città, tipologia, prezzo); scheda dello spazio (disponibilità, tipologia, prezzo, attrezzature, livello di rumore); prenotazione a ore con controllo che la fascia oraria non sia già occupata; area host per pubblicare uno spazio; pagina "Le mie prenotazioni".

**Fuori (solo descritto nella relazione e nelle slide):** pagamenti veri, assicurazione e deposito, verifica dell'identità, mappa, pagamento diviso, abbonamento, sincronizzazione del calendario, eventi della community.

## 🟢 Compiti senza codice e senza AI

Chiunque può prendere queste voci, anche senza saper programmare e senza usare l'AI. Sono segnate con 🟢 nei giorni qui sotto.

- **Decisioni (giorno 1):** ruoli, nome della startup, città di lancio, forma giuridica, numeri chiave.
- **Scrittura della relazione:** sezioni 1, 2, 3, 4 e 5, rischi e contromisure. Per la sezione 3 basta cercare i concorrenti sul web e annotare link e data (regola S4).
- **Numeri e tabelle:** costi, ricavi e punto di pareggio della sezione 5, fatti con Excel, LibreOffice o Fogli Google.
- **Revisione:** controllo dei numeri, rilettura, controllo delle fonti.
- **Presentazione:** slide, esportazione della relazione, prova generale.

**Chi non usa GitHub** può scrivere la propria parte in un documento (Word, Google Docs o simili) e chiedere a un compagno di caricarla nel repository e di spuntare la voce con il suo nome.

---

## Giorno 1 · mercoledì 18/11: decisioni

- [ ] 🟢 Assegnare i ruoli A, B, C, D (tabella sopra)
- [ ] 🟢 Decidere il nome della startup
- [ ] 🟢 Scegliere la città di lancio (Milano, Bologna o Roma)
- [ ] 🟢 Decidere la forma giuridica (consigliata: Start-up Innovativa s.r.l.)
- [ ] 🟢 Fissare i numeri chiave usati ovunque: commissione %, tariffa oraria media, prezzo dell'abbonamento, fabbisogno finanziario (tutti come *ipotesi*) — B
- [x] Scegliere lo stack del sito: **Python + Flask + SQLite**, con pagine in HTML/CSS/JavaScript; creata la cartella `sito/` (si avvia con `python app.py`) — C (PR #7)
- [ ] Spostare la vecchia relazione di Suonami in `archivio/` e creare la nuova relazione vuota con le 5 sezioni — A

## Giorni 2-3 · giovedì 19/11 e venerdì 20/11: prima stesura e base del sito

**Relazione**

- [ ] 🟢 Sezione 2: forma giuridica, descrizione del prodotto, tabella delle 11 funzionalità (indicando quali sono nel sito demo), architettura tecnica (quella del sito vero) — A
- [ ] 🟢 Sezione 4: organigramma, ruoli dei soci fondatori, piano di assunzioni del primo anno — A
- [ ] 🟢 Sezione 3: target (host e ospiti), almeno 2 concorrenti con fonte, matrice di confronto, pricing model — B

**Sito**

- [ ] Database: tabelle utenti, spazi, prenotazioni, con alcuni spazi di esempio — C
- [ ] API: registrazione/login, elenco e dettaglio spazi, creazione di uno spazio, creazione e lista prenotazioni — C
- [ ] Pagine: home con elenco e filtri, scheda dello spazio, login/registrazione — D

## Giorni 4-5 · sabato 21/11 e domenica 22/11: completare

**Relazione**

- [ ] 🟢 Sezione 5: investimenti iniziali (CapEx), costi annuali (OpEx), ricavi per 3 anni, punto di pareggio, almeno una tabella o un grafico — B
- [ ] 🟢 Rischi principali e contromisure (rumore e condomini, affitti brevi e tasse, problema "uovo e gallina") — A

**Sito**

- [ ] Prenotazione a ore con controllo delle sovrapposizioni — C
- [ ] Pagine: prenota, "Le mie prenotazioni", area host per pubblicare uno spazio — D
- [ ] Il sito parte con un solo comando e le istruzioni sono scritte in `sito/README.md` — C
- [ ] Prova completa: registrazione → ricerca → prenotazione → l'host vede la prenotazione — C, D

## Giorno 6 · lunedì 23/11: chiusura della relazione e slide

- [ ] 🟢 Sezione 1, Executive Summary (si scrive per ultimo, si mette per primo): nome, vision, mission, problema, soluzione, fabbisogno — A
- [ ] 🟢 Numeri uguali tra Executive Summary, sezione 3 e sezione 5 — B
- [ ] 🟢 Rilettura completa (italiano, formattazione) e controllo delle fonti; dati mancanti segnati con `[DA VERIFICARE]` — tutti
- [ ] 🟢 Slide: una o due per ogni sezione, più le slide del sito (screenshot e architettura) — tutti
- [ ] Bloccare il sito: da qui solo correzioni di errori, niente funzioni nuove — C, D

## Giorno 7 · martedì 24/11: prova generale

- [ ] 🟢 Esportare la relazione finale (PDF o Word) — A
- [ ] 🟢 Prova generale della presentazione con i tempi, decidendo chi presenta cosa — tutti
- [ ] Prova della demo del sito sul computer che useremo, con un piano B (video o screenshot) se non funziona — D

## Mercoledì 25/11 · presentazione

- [ ] 🟢 Presentazione di gruppo e demo del sito
