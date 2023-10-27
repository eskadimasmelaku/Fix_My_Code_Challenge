#!/usr/bin/node
/*
    Print a square with the character #
    
    The size of the square must be the first argument 
    of the program.
*/

function printSquare(size) {
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += '#';
    }
    console.log(row);
  }
}

const size = parseInt(process.argv[2]);
if (isNaN(size) || size <= 0) {
  console.log("Please provide a valid positive integer as the size of the square.");
} else {
  printSquare(size);
}

