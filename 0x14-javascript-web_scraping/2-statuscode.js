#!/usr/bin/node
const request = require('request');
const url = 'https://alx-intranet.hbtn.io/status';
request.get(url, (error, response) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log('code:', response.statusCode);
});

