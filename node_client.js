const net = require("net");
const readline = require("readline");

const client = net.createConnection(
  {
    host: "127.0.0.1",
    port: 9000
  },
  () => {
    console.log("Verbunden mit C Server");
  }
);

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

client.on("data", (data) => {
  console.log("< " + data.toString().trim());

  rl.question("> ", (text) => {
    client.write(text + "\n");

    if (text === "quit") {
      rl.close();
    }
  });
});

client.on("end", () => {
  console.log("Verbindung beendet");
});
