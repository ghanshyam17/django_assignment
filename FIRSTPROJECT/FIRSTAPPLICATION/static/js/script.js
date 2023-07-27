function convertText() {
    const elementsToConvert = document.querySelectorAll(".textToConvert");

    const color = prompt("Enter the color (e.g., 'red', 'blue', 'green'):");
    const font = prompt("Enter the font (e.g., 'Arial', 'Helvetica', 'Verdana'):");

    elementsToConvert.forEach(element => {
        element.style.color = color;
        element.style.fontFamily = font;
    });
}
