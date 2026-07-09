const db = require("../config/db");

async function findAll() {
  const [rows] = await db.query(
    "SELECT id, name, email, created_at FROM users ORDER BY id DESC"
  );

  return rows;
}

async function findById(id) {
  const [rows] = await db.query(
    "SELECT id, name, email, created_at FROM users WHERE id = ?",
    [id]
  );

  return rows[0] || null;
}

async function create(user) {
  const [result] = await db.query(
    "INSERT INTO users (name, email) VALUES (?, ?)",
    [user.name, user.email]
  );

  return {
    id: result.insertId,
    name: user.name,
    email: user.email
  };
}

module.exports = {
  findAll,
  findById,
  create
};
