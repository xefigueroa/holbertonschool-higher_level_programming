#!/usr/bin/node
function factorial (v) {
  return v === 0 || isNaN(v) ? 1 : v * factorial(v - 1);
}

console.log(factorial(Number(process.argv[2])));
