function generateRandomString() {
  fetch("codes.txt")
    .then((response) => response.text())
    .then((data) => {
      const stringsArray = data.split("\n");

      const randomIndex = Math.floor(Math.random() * stringsArray.length);

      document.getElementById("randomString").innerText =
        stringsArray[randomIndex];
    })
    .catch((error) => console.error("Error fetching random strings:", error));
}
