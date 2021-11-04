#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (err, res, content) {
  if (err) {
    console.error(err);
  }
  console.log(JSON.parse(content).title);
});
