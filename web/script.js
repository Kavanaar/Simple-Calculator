let firstNumber = "";
let secondNumber = "";
let operator = "";
let isSecond = false;

const display = document.getElementById("display");

// Update display
function updateDisplay(value) {
    display.value = value;
}

// Button press handler
function press(value) {
    if ("+-*/".includes(value)) {
        if (firstNumber === "") return;
        operator = value;
        isSecond = true;
        updateDisplay(operator);
    } else {
        if (!isSecond) {
            firstNumber += value;
            updateDisplay(firstNumber);
        } else {
            secondNumber += value;
            updateDisplay(secondNumber);
        }
    }
}

// Clear calculator
function clearDisplay() {
    firstNumber = "";
    secondNumber = "";
    operator = "";
    isSecond = false;
    updateDisplay("");
}

// Perform calculation
function calculate() {
    let a = parseFloat(firstNumber);
    let b = parseFloat(secondNumber);
    let result;

    if (isNaN(a) || isNaN(b)) {
        updateDisplay("Error");
        return;
    }

    switch (operator) {
        case "+":
            result = a + b;
            break;
        case "-":
            result = a - b;
            break;
        case "*":
            result = a * b;
            break;
        case "/":
            if (b === 0) {
                updateDisplay("Error");
                return;
            }
            result = a / b;
            break;
        default:
            return;
    }

    updateDisplay(result);
    firstNumber = result.toString();
    secondNumber = "";
    operator = "";
    isSecond = false;
}

// Dark mode toggle
function toggleDarkMode() {
    document.body.classList.toggle("dark");
}

// Keyboard support
document.addEventListener("keydown", function (event) {
    const key = event.key;

    if (!isNaN(key) || key === ".") {
        press(key);
    } else if ("+-*/".includes(key)) {
        press(key);
    } else if (key === "Enter") {
        calculate();
    } else if (key === "Backspace") {
        clearDisplay();
    }
});
