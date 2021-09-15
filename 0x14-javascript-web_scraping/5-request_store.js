#!/usr/bin/node
// Write content to a file.
const url = process.argv[2];
const file = process.argv[3];
const fs = require('fs');
const request = require('request');

request(url, (error, response) => {
  if (error) {
    console.log(error);
  }

  const text = response.toJSON().body;

  fs.writeFile(file, text, err => {
    if (err) {
      console.error(err);
    }
  });
});
