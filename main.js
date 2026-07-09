const output = document.querySelector("#output");
const btn = document.querySelector("#btn");

let count = 0;

btn.addEventListener("click", () => {
  count++;
  output.textContent = `✓ Klick ${count}`;
});
