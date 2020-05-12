#!/usr/bin/node

const myFile = process.argv[2];

const fs = require('fs');

fs.readFile(myFile, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
