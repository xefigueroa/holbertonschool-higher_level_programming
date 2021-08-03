#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let ocurr = 0;
  for (const i in list) {
    if (list[i] === searchElement) {
      ocurr++;
    }
  }
  return ocurr;
};
