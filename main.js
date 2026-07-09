const canvas = document.querySelector("#game");
const ctx = canvas.getContext("2d");

const player = {
  x: 100,
  y: 100,
  w: 32,
  h: 32,
  speed: 4
};

const keys = {
  left: false,
  right: false,
  up: false,
  down: false
};

window.addEventListener("keydown", (event) => {
  if (event.key === "ArrowLeft") keys.left = true;
  if (event.key === "ArrowRight") keys.right = true;
  if (event.key === "ArrowUp") keys.up = true;
  if (event.key === "ArrowDown") keys.down = true;
});

window.addEventListener("keyup", (event) => {
  if (event.key === "ArrowLeft") keys.left = false;
  if (event.key === "ArrowRight") keys.right = false;
  if (event.key === "ArrowUp") keys.up = false;
  if (event.key === "ArrowDown") keys.down = false;
});

function update() {
  if (keys.left) player.x -= player.speed;
  if (keys.right) player.x += player.speed;
  if (keys.up) player.y -= player.speed;
  if (keys.down) player.y += player.speed;

  player.x = Math.max(0, Math.min(player.x, canvas.width - player.w));
  player.y = Math.max(0, Math.min(player.y, canvas.height - player.h));
}

function draw() {
  ctx.fillStyle = "#000000";
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  ctx.fillStyle = "#3b82f6";
  ctx.fillRect(player.x, player.y, player.w, player.h);

  ctx.fillStyle = "#ffffff";
  ctx.font = "16px Consolas";
  ctx.fillText("Pfeiltasten bewegen", 20, 30);
}

function loop() {
  update();
  draw();

  requestAnimationFrame(loop);
}

loop()
