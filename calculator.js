// Calculator.js
// This program defines four functions: multiply, add, subtract, and divide.
// Each functions takes two arguments and return the operator's arithmetric result
// (no output is printed to the screen).

// multiply - this function multiplies two numbers and returns the result.
// Input  : a, b
// Returns: a * b
function multiply(a, b) {
	return a * b
}

// add - this function adds two numbers and returns the result.
// Input  : a, b
// Returns: a + b
function add(a, b) {
	return a + b
}

// subtract - this function subtracts two numbers and returns the result.
// Input  : a, b
// Returns: a - b
function subtract(a, b) {
	return a - b
}

// divide - this function divides two numbers and returns the result.
// Input  : a, b
// Returns: a / b
function divide(a, b) {
	return a / b
}

// The program will start running from here
// Call the multiply function defined above with the numbers 5 and 6 and return the results
console.log("I'm going use the calculator functions to multiply 5 and 6")
var x = multiply(5,6)
console.log(x)
