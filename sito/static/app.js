// Chiede al server se è attivo e mostra la risposta nella pagina.
// È un esempio di come le pagine parlano con le API del backend.
fetch("/api/stato")
  .then((risposta) => risposta.json())
  .then((dati) => {
    document.getElementById("stato").textContent =
      "Server: " + dati.server + " · Database: " + dati.database;
  })
  .catch(() => {
    document.getElementById("stato").textContent = "Il server non risponde.";
  });
