#!/usr/bin/node

const myarg = process.argv[2];

if (!myarg) {
  console.log('Missing number of occurrences');
} else {
  for (let count = 0; count < myarg; count++) {
    console.log('C is fun');
  }
}
