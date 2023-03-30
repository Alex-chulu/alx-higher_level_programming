#!/usr/bin/node

let num = 0;
exports.logMe = function (item) {
  if (item) {
    console.log(`${numt}: ${item}`);
    numt++;
  }
};
