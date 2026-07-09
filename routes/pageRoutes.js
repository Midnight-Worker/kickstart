const express = require("express");
const pageController = require("../controller/pageController");

const router = express.Router();

router.get("/", pageController.home);

module.exports = router;
