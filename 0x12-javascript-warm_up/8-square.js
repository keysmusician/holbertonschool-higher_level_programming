#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (!size) {
  console.log('Missing size');
}

for (let row = size; row > 0; row--) {
  console.log('X'.repeat(size));
}
