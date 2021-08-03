#!/usr/bin/node
'use strict';
let secBig = 0;
let args = process.argv.slice(2);
if (args.length > 1) {
  args.sort();
  secBig = args[args.length - 2];
}
console.log(secBig);
