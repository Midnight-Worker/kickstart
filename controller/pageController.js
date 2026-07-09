function home(req, res) {
  res.sendFile("index.html", {
    root: "public"
  });
}

module.exports = {
  home
};
