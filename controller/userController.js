const User = require("../models/userModel");

async function index(req, res) {
  try {
    const users = await User.findAll();

    res.json({
      ok: true,
      data: users
    });
  } catch (error) {
    res.status(500).json({
      ok: false,
      message: "Benutzer konnten nicht geladen werden."
    });
  }
}

async function show(req, res) {
  try {
    const user = await User.findById(req.params.id);

    if (!user) {
      return res.status(404).json({
        ok: false,
        message: "Benutzer nicht gefunden."
      });
    }

    res.json({
      ok: true,
      data: user
    });
  } catch (error) {
    res.status(500).json({
      ok: false,
      message: "Benutzer konnte nicht geladen werden."
    });
  }
}

async function store(req, res) {
  try {
    const { name, email } = req.body;

    if (!name || !email) {
      return res.status(400).json({
        ok: false,
        message: "Name und E-Mail sind erforderlich."
      });
    }

    const user = await User.create({ name, email });

    res.status(201).json({
      ok: true,
      data: user
    });
  } catch (error) {
    res.status(500).json({
      ok: false,
      message: "Benutzer konnte nicht gespeichert werden."
    });
  }
}

module.exports = {
  index,
  show,
  store
};
