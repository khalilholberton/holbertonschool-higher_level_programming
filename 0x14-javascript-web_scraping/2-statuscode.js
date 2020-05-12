#!/usr/bin/node

const givenURL = process.argv[2];

const request = require('request');

request(givenURL, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
