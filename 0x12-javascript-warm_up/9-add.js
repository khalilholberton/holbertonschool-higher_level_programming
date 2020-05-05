#!/usr/bin/node
const myfarg = process.argv[2];

const mysarg = process.argv[3];

const firstnum = parseInt(myfarg, 10);

const secondnum = parseInt(mysarg, 10);

console.log(add(firstnum, secondnum));

function add (a, b) {
  return a + b;
}
