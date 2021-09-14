#!/usr/bin/node
// Display the status code of a GET request.
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  console.log('code:', response && response.statusCode); // Print the response status code if a response was received
});
