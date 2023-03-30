#!/usr/bin/node

const args = process.argv;

if (args[2] === undefined) {
  console.log('1');
} else {
  const rst = my_factorial(parseInt(args[2]));
  console.log(rst);
}

function my_factorial (number) {
  if (number === 1) {
    return number;
  }
  return number * my_factorial(number - 1);
}
