#!/usr/bin/node
// Write content to a file.
const file = process.argv[2];
const text = process.argv[3];
const fs = require('fs');
fs.writeFile(file, text, err => {
  if (err) {
    console.error(err);
  }
});
