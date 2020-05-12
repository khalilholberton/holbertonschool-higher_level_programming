#!/usr/bin/node

const givenURL = process.argv[2];

const request = require('request');

request.get(givenURL, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  if (response.statusCode === 200) {
    const data = JSON.parse(body);
    const dict = {};

    for (const uTask of data) {
      if (uTask.completed === true) {
        if (uTask.userId in dict) {
          dict[uTask.userId] += 1;
        } else {
          dict[uTask.userId] = 1;
        }
      }
    }
    console.log(dict);
  }
});
