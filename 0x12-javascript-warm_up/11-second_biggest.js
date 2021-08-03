#!/usr/bin/node
if (process.argv.length < 4) {
  console.log('0');
} else {
  const v = process.argv.slice(2);
  v.sort((a, b) => b - a);
  console.log(v[1]);
}
