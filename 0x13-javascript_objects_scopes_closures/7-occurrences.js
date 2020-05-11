#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let nbOccur = 0;
  let idx = 0;

  for (idx = 0; idx < list.length; idx++) {
    if (searchElement === list[idx]) {
      nbOccur++;
    }
  }
  return nbOccur;
};
