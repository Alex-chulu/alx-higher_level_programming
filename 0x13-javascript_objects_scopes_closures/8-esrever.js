#!/usr/bin/node

exports.esrever = function (list) {
  const listReverse = [];
  while (list.length) {
    listReverse.push(list.pop());
  }
  return listReverse;
};
