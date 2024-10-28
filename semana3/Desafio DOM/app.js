const redSlider = document.getElementById('red');
const greenSlider = document.getElementById('green');
const blueSlider = document.getElementById('blue');
const redValue = document.getElementById('red-value');
const greenValue = document.getElementById('green-value');
const blueValue = document.getElementById('blue-value');
const colorBox = document.querySelector('.color-box');
const colorPreview = document.getElementById('color-preview');

function updateColor() {
    const red = redSlider.value;
    const green = greenSlider.value;
    const blue = blueSlider.value;

    redValue.textContent = `${red} (${Math.round((red / 255) * 100)}%)`;
    greenValue.textContent = `${green} (${Math.round((green / 255) * 100)}%)`;
    blueValue.textContent = `${blue} (${Math.round((blue / 255) * 100)}%)`;

    colorBox.style.backgroundColor = `rgb(${red}, ${green}, ${blue})`;

    colorPreview.style.color = `rgb(${red}, ${green}, ${blue})`;
}

redSlider.addEventListener('input', updateColor);
greenSlider.addEventListener('input', updateColor);
blueSlider.addEventListener('input', updateColor);

updateColor();