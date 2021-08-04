#!/usr/bin/node
let COUNT = 0;
exports.logMe = function (item) {
  console.log(String(COUNT++) + ': ' + String(item));
};
