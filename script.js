function generateRandomString() {
  fetch("codes.txt")
    .then((response) => response.text())
    .then((data) => {
      const stringsArray = data.split("\n");
      const randomIndex = Math.floor(Math.random() * stringsArray.length);
      const randomString = stringsArray[randomIndex];

      // Create a new anchor element
      const link = document.createElement("a");
      link.href = randomString;
      link.innerText = randomString;
      link.target = "_blank"; // Open the link in a new tab

      // Replace the old paragraph element with the new anchor element
      const oldElement = document.getElementById("randomString");
      oldElement.parentNode.replaceChild(link, oldElement);
      link.id = "randomString"; // Assign the old id to the new element
    })
    .catch((error) => console.error("Error fetching random strings:", error));
}
