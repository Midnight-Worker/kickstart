const { WebSocketServer } = require("ws");

const port = 8765;
const wss = new WebSocketServer({ port });

wss.on("connection", (socket) => {
  console.log("Client verbunden");

  socket.send("Willkommen vom Node.js WebSocket Server!");

  socket.on("message", (message) => {
    const text = message.toString();

    console.log("Nachricht:", text);

    socket.send("Echo: " + text);
  });

  socket.on("close", () => {
    console.log("Client getrennt");
  });

  socket.on("error", (error) => {
    console.error("WebSocket Fehler:", error.message);
  });
});

console.log(`WebSocket Server läuft auf ws://localhost:${port}`);
