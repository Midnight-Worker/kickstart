const http = require("http");
const fs = require("fs");
const path = require("path");
const { WebSocketServer } = require("ws");

const port = 3000;
const publicDir = path.join(__dirname, "public");

const server = http.createServer((req, res) => {
  let filePath = path.join(publicDir, req.url === "/" ? "index.html" : req.url);

  fs.readFile(filePath, (err, data) => {
    if (err) {
      res.writeHead(404);
      res.end("Not found");
      return;
    }

    res.writeHead(200);
    res.end(data);
  });
});

const wss = new WebSocketServer({ server });

wss.on("connection", (socket) => {
  console.log("Client verbunden");

  socket.send("Willkommen vom WebSocket-Server!");

  socket.on("message", (message) => {
    const text = message.toString();

    console.log("Nachricht:", text);

    socket.send("Echo: " + text);
  });

  socket.on("close", () => {
    console.log("Client getrennt");
  });
});

server.listen(port, () => {
  console.log(`Server läuft auf http://localhost:${port}`);
});
