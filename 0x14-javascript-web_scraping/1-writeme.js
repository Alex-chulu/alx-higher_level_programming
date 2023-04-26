#!/usr/bin/node
// import fs module
const fs = require('fs');

if (process.argv.length !== 4) {
  console.log('Usage: Python is cool');
  process.exit(1);
}

const filePath = process.argv[2];
const string = process.argv[3];

fs.writeFile(filePath, string, { encoding: 'utf-8' }, err => {
  if (err) {
    console.error(err);
  }
});
