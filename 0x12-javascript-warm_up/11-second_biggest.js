#!/usr/bin/node

const args = process.argv.slice(2);
const sorted = args.sort((a, b) => parseInt(a) < parseInt(b));
const secondLargest = sorted[1];
if (secondLargest) {
  console.log(secondLargest);
} else {
  console.log(0);
}
