#!/usr/bin/node
'use strict';
const args = process.argv.slice(2);
if (args.length >= 4) {
  args.sort();
  console.log(args[args.length - 2]);
} else {
  console.log(0);
}
