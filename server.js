const express = require("express");

const app = express();
const port = 3000;

app.use(express.static("public"));

app.get("/api/status", (req, res) => {
  res.json({
    ok: true,
    message: "Express läuft."
  });
});

app.listen(port, () => {
  console.log(`Server läuft auf http://localhost:${port}`);
});
