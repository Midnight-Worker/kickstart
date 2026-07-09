const statusText = document.querySelector("#status");
const messageInput = document.querySelector("#messageInput");
const sendBtn = document.querySelector("#sendBtn");
const log = document.querySelector("#log");

const socket = new WebSocket("ws://localhost:3000");

function writeLog(text) {
  log.textContent += text + "\n";
}

socket.addEventListener("open", () => {
  statusText.textContent = "Verbunden.";
  writeLog("✓ Verbindung geöffnet");
});

socket.addEventListener("message", (event) => {
  writeLog("< " + event.data);
});

socket.addEventListener("close", () => {
  statusText.textContent = "Getrennt.";
  writeLog("✗ Verbindung geschlossen");
});

socket.addEventListener("error", () => {
  writeLog("! WebSocket-Fehler");
});

sendBtn.addEventListener("click", () => {
  const text = messageInput.value;

  socket.send(text);
  writeLog("> " + text);
});
