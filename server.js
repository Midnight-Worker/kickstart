require("dotenv").config();

const express = require("express");
const path = require("path");

const pageRoutes = require("./routes/pageRoutes");
const userRoutes = require("./routes/userRoutes");

const app = express();
const port = process.env.PORT || 3000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use(express.static(path.join(__dirname, "public")));

app.use("/", pageRoutes);
app.use("/api/users", userRoutes);

app.listen(port, () => {
  console.log(`Server läuft auf http://localhost:${port}`);
});
