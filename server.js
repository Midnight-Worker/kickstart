const net = require("net");

const HOST = "127.0.0.1";
const PORT = 9000;

const server = net.createServer((socket) => {
  console.log("Client verbunden");

  socket.write("Willkommen vom Node TCP Server\n");

  socket.on("data", (data) => {
    const text = data.toString().trim();

    console.log("Nachricht:", text);

    if (text === "quit") {
      socket.write("bye\n");
      socket.end();
      return;
    }

    socket.write("Echo: " + text + "\n");
  });

  socket.on("end", () => {
    console.log("Client getrennt");
  });
});

server.listen(PORT, HOST, () => {
  console.log(`TCP Server läuft auf ${HOST}:${PORT}`);
});
