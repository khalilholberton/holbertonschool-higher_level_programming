#!/usr/bin/node

const myarg = process.argv[2];

if (isNaN(myarg)) {
  console.log('Missing size');
} else {
  for (let count = 0; count < myarg; count++) {
    console.log('X'.repeat(myarg));
  }
}
