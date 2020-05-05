#!/usr/bin/node

let res = 0;

const myarg = process.argv.slice(2);

const lenarg = myarg.length

if (lenarg  >  1) {
  myarg.sort((a, b)  =>  a - b);
  res  =  myarg[myarg.length - 2];
}

console.log(res);
