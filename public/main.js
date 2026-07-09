const output = document.querySelector("#output");
const btn = document.querySelector("#btn");

btn.addEventListener("click", async () => {
  output.textContent = "Frage Server...";

  const response = await fetch("/api/status");
  const data = await response.json();

  output.textContent = data.message;
});
