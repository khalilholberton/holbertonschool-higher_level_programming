#!/usr/bin/node

const myarg = process.argv[2];

if (isNaN(myarg)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myarg);
}
