#!/usr/bin/node

exports.esrever = function (list) {
  const revList = [];
  let idx = 0;

  while (idx < list.length) {
    revList.unshift(list[idx]);
    idx++;
  }
  return revList;
};
