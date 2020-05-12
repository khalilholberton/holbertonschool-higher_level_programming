#!/usr/bin/node

const request = require('request');

const givenURL = process.argv[2];

request.get(givenURL, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    let movNUM = 0;
    const movies = JSON.parse(body).results;
    for (const mov of movies) {
      for (const char of mov.characters) {
        if (char.endsWith('18/')) { movNUM++; }
      }
    }
    console.log(movNUM);
  }
});
