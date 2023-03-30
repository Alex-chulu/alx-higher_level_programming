#!/usr/bin/node

const dict = require('./101-data.js').dict;

const new_dict = {};

Object.getOwnPropertyNames(dict).forEach(occurences => {
  if (new_dict[dict[occurences]] === undefined) {
    new_dict[dict[occurences]] = [occurences];
  } else {
    new_dict[dict[occurences]].push(occurences);
  }
});
console.log(new_dict);
