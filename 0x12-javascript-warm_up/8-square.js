#!/usr/bin/node

if (process.argv[2] === undefined) {
  console.log('Missing size');
} else if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let y = 1; y <= process.argv[2]; y++) {
    console.log('X'.repeat(process.argv[2]));
  }
}
