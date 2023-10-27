#!/usr/bin/node
/*
    Print a square with the character #
    The size of the square must be the first argument 
    of the program.
*/

const size = parseInt(process.argv[2]);

if (isNaN(size)) {
  console.log("Please provide a valid number as the size.");
} else {
  for (let i = 0; i < size; i++) {
    let row = "";
    for (let j = 0; j < size; j++) {
      row += "#";
    }
    console.log(row);
  }
}

