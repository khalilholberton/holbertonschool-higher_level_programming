#!/usr/bin/node

const request = require('request');

const fs = require('fs');

request(process.argv[2], function (err, response, body) {
  if (err) throw err;
  else if (response.statusCode === 200) {
    fs.writeFile(process.argv[3], body, 'utf-8', function (err) {
      if (err) throw err;
    });
  } else {
    throw err;
  }
});
