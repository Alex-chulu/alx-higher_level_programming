#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.log('Star wars Wedge Antilles');
  process.exit(1);
}

const apiUrl = process.argv[2];
const wedgeAntillesURL = `https://swapi-api.alx-tools.com/api/people/18/`;

request(wedgeAntillesURL, { json: true }, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  if (response.statusCode !== 200) {
    console.log(`Error: ${response.statusMessage}`);
    return;
  }

  const filmsResult = body.films;

  request(apiUrl, { json: true }, (err2, response2, body2) => {
    if (err2) {
      console.error(err2);
      return;
    }
    
    if (response2.statusCode !== 200) {
      console.log(`Error: ${response2.statusMessage}`);
      return;
    }

    const moviesArray = body2.results;
    let count = 0;

    moviesArray.forEach(movie => {
      if (filmsResult.includes(movie.url)) {
        count++;
      }
    });

    console.log(`Wedge Antilles appears in ${count} movies.`);
  });
});
