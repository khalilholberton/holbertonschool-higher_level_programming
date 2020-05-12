#!/usr/bin/node

const fs = require('fs');

const request = require('request');

const givenURL = process.argv[2];

const file = process.argv[3];

request.get(givenURL, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(file, body, 'utf8');
  }
});
