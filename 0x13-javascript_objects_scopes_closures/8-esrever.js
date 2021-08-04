#!/usr/bin/node
exports.esrever = function (list) {
  const reverseList = [];
  for (let i = list.length; i; i--) {
    reverseList.push(list.pop());
  }
  return reverseList;
};
