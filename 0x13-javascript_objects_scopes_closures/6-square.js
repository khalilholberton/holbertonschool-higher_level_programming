#!/usr/bin/node

const newSquare = require('./5-square');

class Square extends newSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let idx = 0; idx < this.width; idx++) {
        console.log(c.repeat(this.height));
      }
    }
  }
}

module.exports = Square;
