const WebSocket = require("ws");
const readline = require("readline");

const url = "ws://localhost:8765";
const socket = new WebSocket(url);

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

socket.on("open", () => {
  console.log(`Verbunden mit ${url}`);
});

socket.on("message", (message) => {
  console.log("< " + message.toString());

  rl.question("> ", (text) => {
    if (["q", "quit", "exit"].includes(text.toLowerCase())) {
      socket.close();
      rl.close();
      return;
    }

    socket.send(text);
  });
});

socket.on("close", () => {
  console.log("Verbindung geschlossen");
  rl.close();
});

socket.on("error", (error) => {
  console.error("WebSocket Fehler:", error.message);
  rl.close();
});
