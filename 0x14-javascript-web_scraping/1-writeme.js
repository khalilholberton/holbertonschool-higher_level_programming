#!/usr/bin/node

const givenFile = process.argv[2];

const texttoadd = process.argv[3];

const fs = require('fs');

fs.writeFile(givenFile, texttoadd, 'utf-8', function (err) {
  if (err) {
    console.log(err);
  }
});
