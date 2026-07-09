const output = document.querySelector("#output");
const userList = document.querySelector("#userList");
const btnLoad = document.querySelector("#btnLoad");
const btnCreate = document.querySelector("#btnCreate");

async function loadUsers() {
  output.textContent = "Lade Benutzer...";

  const response = await fetch("/api/users");
  const result = await response.json();

  userList.innerHTML = "";

  if (!result.ok) {
    output.textContent = result.message;
    return;
  }

  result.data.forEach((user) => {
    const li = document.createElement("li");
    li.textContent = `${user.name} <${user.email}>`;
    userList.appendChild(li);
  });

  output.textContent = `✓ ${result.data.length} Benutzer geladen`;
}

async function createDemoUser() {
  output.textContent = "Speichere Benutzer...";

  const random = Date.now();

  const response = await fetch("/api/users", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      name: "Demo",
      email: `demo-${random}@example.com`
    })
  });

  const result = await response.json();

  if (!result.ok) {
    output.textContent = result.message;
    return;
  }

  output.textContent = `✓ Benutzer angelegt: ${result.data.name}`;
  await loadUsers();
}

btnLoad.addEventListener("click", loadUsers);
btnCreate.addEventListener("click", createDemoUser);
