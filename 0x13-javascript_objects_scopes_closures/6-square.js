#!/usr/bin/node
const Square5 = require('./5-square')

class Square extends Square5 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let rows = this.height; rows; rows--) {
      console.log(c.repeat(this.width));
    }
  }
}
