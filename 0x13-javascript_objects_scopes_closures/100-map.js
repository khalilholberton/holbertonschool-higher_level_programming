#!/usr/bin/node

const mylist = require('./100-data.js').list;

console.log(mylist);
console.log(mylist.map((idx, num) => idx * num));
