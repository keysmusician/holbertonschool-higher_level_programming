#!/usr/bin/node
// Print all characters of a Star Wars movie
const request = require('request');
const filmId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/'.concat(filmId);
request(url, callbackMain);

function callbackMain (error, response, body) {
  if (error) return console.error(error);

  const characters = JSON.parse(body).characters;
  for (const characterUrl of characters) {
    request(characterUrl, callbackCharacter);
  }
}

function callbackCharacter (error, response, body) {
  if (error) return console.error(error);

  const charater = JSON.parse(body).name;
  console.log(charater);
}
