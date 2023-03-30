#!/usr/bin/node

const num_1 = process.argv[2];
const num_2 = process.argv[3];

if (isNaN(num_1) || isNaN(num_2)) {
  console.log('NaN');
} else {
  console.log(addtn(parseInt(num_1), parseInt(num_2)));
}

function add(a, b) {
  return a + b;
}
