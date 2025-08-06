const structureEl = document.getElementById("structure");
const inputEl = document.getElementById("inputValue");
const visualArea = document.getElementById("visualArea");

async function updateDisplay() {
  const structure = structureEl.value;
  const res = await fetch(`/get/${structure}`);
  const data = await res.json();

  visualArea.innerHTML = "";
  data.forEach((item) => {
    const div = document.createElement("div");
    div.className = "box";
    div.textContent = item;
    visualArea.appendChild(div);
  });
}

async function handleInsert() {
  const value = inputEl.value.trim();
  if (!value) return alert("Enter a value");

  const structure = structureEl.value;
  await fetch(`/insert/${structure}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ value }),
  });
  inputEl.value = "";
  updateDisplay();
}

async function handleRemove() {
  const structure = structureEl.value;
  await fetch(`/remove/${structure}`, { method: "POST" });
  updateDisplay();
}

updateDisplay();
