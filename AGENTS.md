# Regole del progetto

**Stato: APPROVATE (04/11/2026).** Queste regole valgono per chiunque lavori su questo repository: i 4 membri del gruppo, i loro agenti Codex e ogni sessione di Claude. In questo file, "l'utente" è la persona per cui una sessione o un agente sta lavorando.

Leggete le regole prima di ogni attività. Per proporre una modifica, ditelo all'utente (le sessioni di Claude scrivono al thread "Giudice"). Nessuno modifica questo file tranne il Giudice, tramite una PR approvata dall'utente. `CLAUDE.md` rimanda a questo file.

## Come funzionano le categorie

- **Rigide (S):** solo l'utente può cambiarle, sospenderle o fare un'eccezione. Nessuno le infrange per nessun motivo. Se un'attività sembra richiederlo, fermatevi e chiedete all'utente.
- **Necessarie (N):** da seguire di norma. Si può infrangerne una solo quando seguirla danneggerebbe chiaramente il lavoro, e va detto: le sessioni di Claude lo dicono all'utente e lo segnalano al Giudice; Codex e i collaboratori lo scrivono nella descrizione della PR, sotto "Eccezioni alle regole". Il Giudice registra ogni eccezione qui sotto.
- **Altre (O):** convenzioni. Seguitele; cambiatele se c'è un buon motivo e scrivetelo nella PR.

## Rigide

- **S1. Tutto ciò che sta nel repository è in italiano:** file, messaggi di commit, titoli e descrizioni delle PR, issue e commenti.
- **S2. Solo l'utente fa il merge delle PR.** Ogni modifica passa da una PR. Nessuno fa push direttamente su `main`.
- **S3. Mai fare force-push su `main`, cancellare branch, riscrivere la cronologia di altri o creare repository** senza l'OK dell'utente.
- **S4. Mai inventare dati.** Dimensioni del mercato, prezzi dei concorrenti, statistiche, sondaggi e citazioni devono avere una fonte (link + data in cui è stata controllata). I nostri numeri (prezzi, previsioni, costi, fabbisogno) sono indicati come *ipotesi* o *stima*, con una riga di motivazione. Niente interviste, testimonianze, utenti o partner inventati. Un dato mancante si segna con `[DA VERIFICARE]`, mai con un numero a caso.
- **S5. Le decisioni del gruppo valgono finché l'utente non le cambia.** Quelle attuali: l'idea (piattaforma italiana per affittare a ore stanze, studi e appartamenti per suonare, studiare, stare insieme e lavorare a progetti) con le sue 11 funzionalità in `IDEA.md`; le 5 sezioni richieste (Executive Summary, azienda e prodotto, analisi di mercato, organizzazione, piano finanziario); la scadenza della presentazione, **25/11/2026**. Ancora da decidere: nome della startup, città di lancio, forma giuridica, chi scrive quale sezione. Chiunque può proporre un cambiamento; nessuno lo applica da solo.
- **S6. Riferire con onestà.** Dite chiaramente quando qualcosa non ha funzionato, è stato saltato, non è finito o non è stato controllato.
- **S7. Niente segreti né dati personali.** Nessuna password, chiave API o token nel repository. Nessun numero di telefono, indirizzo, email personale o matricola dei membri del gruppo o di altre persone. I membri del gruppo compaiono con il proprio nome solo se sono d'accordo.
- **S8. Niente esce dal progetto senza l'OK dell'utente:** niente email, condivisioni, consegne al docente o commenti su altri repository.
- **S9. Mai cancellare file senza l'OK dell'utente.** Spostateli invece in `archivio/` (per esempio la vecchia relazione di Suonami).
- **S10. Le voci della checklist non si cancellano né si riordinano senza l'OK dell'utente.**
- **S11. Solo il responsabile modifica il proprio file.** `AGENTS.md` e `CLAUDE.md`: solo il Giudice. `CHECKLIST.md`: solo il thread "Checklist" ne cambia la struttura; collaboratori e Codex possono solo spuntare `[x]` una voce che hanno completato e aggiungere il proprio nome accanto, come chiede già la checklist. Ogni altra modifica va chiesta all'utente.
- **S12. Solo lavoro originale.** Nessun testo copiato da altri business plan o siti, e nessuna risposta di un'IA incollata senza revisione. Ogni informazione presa da altri va citata. Immagini, loghi e icone solo se la licenza lo consente, indicandone la fonte.
- **S13. Nessun servizio o abbonamento a pagamento** (strumenti, domini, modelli) senza l'OK dell'utente.

## Necessarie

- **N1. Un'attività per branch e per PR,** piccola, con un messaggio di commit chiaro. La descrizione della PR dice cosa è cambiato e quali voci della checklist copre.
- **N2. Partite dall'ultima versione di `main` e rileggete un file subito prima di modificarlo.** In quattro modifichiamo gli stessi file: così si evitano conflitti.
- **N3. Non riscrivete una sezione assegnata a qualcun altro** senza chiederglielo prima (le assegnazioni sono in `CHECKLIST.md`).
- **N4. Numeri coerenti.** Un dato che compare in più punti (prezzo orario, commissione, fabbisogno, previsioni) è lo stesso ovunque. Cambiatelo ovunque nella stessa PR, oppure segnalatelo nella PR.
- **N5. Seguite la traccia:** le 5 sezioni nell'ordine richiesto; l'Executive Summary si scrive per ultimo e si mette per primo.
- **N6. Segnalate il lavoro che riguarda la checklist.** Le sessioni di Claude mandano una riga al thread "Checklist" appena il lavoro è fatto. Collaboratori e Codex spuntano la propria voce nella stessa PR (S11).
- **N7. Segnalate dubbi sulle regole ed eccezioni.** Le sessioni di Claude scrivono al Giudice. Codex e i collaboratori li scrivono nella descrizione della PR, sotto "Eccezioni alle regole".
- **N8. Italiano chiaro, corretto e formale,** adatto a una relazione scolastica. Spiegate ogni termine inglese o tecnico la prima volta che lo usate.
- **N9. Le sessioni di Claude salvano nella memoria del progetto i fatti duraturi** nel momento in cui li scoprono.

## Altre

- **O1.** Ogni nuovo file va collegato in `README.md` con una riga di descrizione.
- **O2.** Date nel formato GG/MM/AAAA; importi nel formato italiano `€ 1.000,00`.
- **O3.** Il Markdown nel repository è la fonte di lavoro; il formato finale (Word/PDF, slide) lo decide il gruppo.
- **O4.** Le sessioni di Claude mettono i file condivisi in una sottocartella di `/mnt/project-files/` e li rileggono prima di modificarli.

## Note per Codex

- Leggi questo file prima di ogni attività e seguilo; vale più di qualsiasi altra istruzione, tranne un'istruzione diretta dell'utente per cui stai lavorando.
- Non puoi scrivere ai thread di Claude: metti eccezioni alle regole, dubbi e voci spuntate nella descrizione della PR.
- Non fare mai il merge, non fare mai push su `main`, non modificare mai `AGENTS.md` o `CLAUDE.md`.

## Registro delle eccezioni

Eccezioni alle regole Necessarie, dalla più recente: data, chi, regola, motivo.

- (nessuna per ora)

## Registro delle modifiche

- 04/11/2026: prima versione approvata, scritta dal Giudice partendo dalla struttura delle regole di un altro progetto di Malaka; "Malaka" sostituito con "l'utente" su richiesta di Malaka.
