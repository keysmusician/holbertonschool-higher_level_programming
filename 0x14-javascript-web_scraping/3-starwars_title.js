#!/usr/bin/node
// Print the title of a Star Wars movie where the episode number matches a
// given integer.
const request = require('request');
const n = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/'.concat(n);
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  console.log(JSON.parse(body).title);
});
