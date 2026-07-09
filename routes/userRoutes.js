const express = require("express");
const userController = require("../controller/userController");

const router = express.Router();

router.get("/", userController.index);
router.get("/:id", userController.show);
router.post("/", userController.store);

module.exports = router;
