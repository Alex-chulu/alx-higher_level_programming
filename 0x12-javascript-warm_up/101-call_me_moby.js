#!/usr/bin/node

exports.callfunction = function (x, theFunction) {
  for (let y = 0; y < x; y++) theFunction();
};
