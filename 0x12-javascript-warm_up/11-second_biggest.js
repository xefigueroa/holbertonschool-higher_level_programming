#!/usr/bin/node
'use strict';
let secBig = 0;
const args = process.argv.slice(2);
if (args.length > 1) {
	args.sort();
	console.log(args[args.length - 2]);
} else {
	console.log(0);
}
