#!/usr/bin/node

let times = parseInt(process.argv[2]);

if (!times) {
  console.log('Missing number of occurrences');
}

for (; times > 0; times--) {
  console.log('C is fun');
}
