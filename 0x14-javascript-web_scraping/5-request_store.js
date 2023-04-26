#!/usr/bin/node
const request = require('request');
const fs = require('fs');

if (process.argv.length !== 4) {
  console.log('Loripsum');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

request(url, { encoding: 'utf-8' }, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  if (response.statusCode !== 200) {
    console.log(`Error: ${response.statusMessage}`);
    return;
  }

  fs.writeFile(filePath, body, { encoding: 'utf-8' }, err => {
    if (err) {
      console.error(err);
    } else {
      console.log(`File saved to ${filePath}.`);
    }
  });
});
