#!/usr/bin/node
//import request module
const request = require('request');

if (process.argv.length !== 3) {
  console.log('star war movies');
  process.exit(1);
}

const movieId = process.argv[2];
const swapiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(swapiUrl, { json: true }, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  if (response.statusCode !== 200) {
    console.log(`Error: ${response.statusMessage}`);
    return;
  }

  const { title, episode_id } = body;
  
  if (parseInt(episode_id) === parseInt(movieId)) {
    console.log(`Title: ${title}`);
  } else {
    console.log(`Movie ID ${movieId} does not match any episode number`);
  }
});
