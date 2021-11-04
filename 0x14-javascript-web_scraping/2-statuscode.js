#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (err, res, content) {
  if (err) {
    console.error(err);
  }
  console.log('code: ' + res.statusCode);
});
