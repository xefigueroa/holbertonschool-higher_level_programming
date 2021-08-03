#!/usr/bin/node
'use strict';
let v = process.argv.length;
if (v === 2) {
  console.log('No argument');
} else if (v === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
