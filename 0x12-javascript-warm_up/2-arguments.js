#!/usr/bin/node

const myarg = process.argv.length;

if (myarg <= 2) {
    console.log('No argument');
} else if (myarg === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
