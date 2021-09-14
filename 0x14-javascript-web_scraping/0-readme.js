#!/usr/bin/node
// Read and print the content of a file.
const file = process.argv[2];
const fs = require('fs');
fs.readFile(file, 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
