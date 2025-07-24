function animarCarta() {
  const card = document.getElementById("card");
  card.style.transform = "rotateY(360deg)";
  setTimeout(() => {
    card.style.transform = "rotateY(0)";
  }, 500);
}

const frases = [
  "Cada pequeño cambio cuenta",
  "Vos podés ser la diferencia",
  "Cuidar el planeta es cuidar tu casa",
  "Actuá ahora, mañana puede ser tarde",
  "El futuro es verde si lo hacemos hoy"
];

window.onload = () => {
  const frase = frases[Math.floor(Math.random() * frases.length)];
  document.getElementById("frase-motivacional").textContent = frase;
};