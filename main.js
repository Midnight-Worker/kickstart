$(function () {
  let count = 0;

  $("#btnClick").on("click", function () {
    count++;

    $("#output").text("✓ Klick " + count);

    $(".alert")
      .removeClass("alert-info alert-warning alert-success")
      .addClass("alert-success")
      .text("jQuery hat den Text geändert.");
  });

  $("#btnReset").on("click", function () {
    count = 0;

    $("#output").text("Bereit.");

    $(".alert")
      .removeClass("alert-info alert-warning alert-success")
      .addClass("alert-info")
      .text("Klassischer Web-Kickstart: HTML, CSS, jQuery, Bootstrap 4.");
  });
});
