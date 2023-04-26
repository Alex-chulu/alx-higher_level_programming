#!/usr/bin/node
//import request module
const request = require('request');

if (process.argv.length !== 3) {
  console.log('Get a status code');
  process.exit(1);
}

const url = process.argv[2];

request(url, (err, response) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(`code: ${response.statusCode}`);
});
