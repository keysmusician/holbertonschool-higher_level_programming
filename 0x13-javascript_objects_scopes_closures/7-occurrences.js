#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const n of list) {
    if (n === searchElement) ++count;
  }
  return count;
};
