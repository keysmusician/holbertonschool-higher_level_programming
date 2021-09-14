#!/usr/bin/node
// Print the number of movies where the character “Wedge Antilles” is present.
const request = require('request');
const filmsUrl = process.argv[2];
request(filmsUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  }

  let count = 0;
  const films = JSON.parse(body).results;
  for (const film of films) {
    for (const characterUrl of film.characters) {
      if (characterUrl.includes('/18/')) {
        count++;
      }
    }
  }
  console.log(count);
});
