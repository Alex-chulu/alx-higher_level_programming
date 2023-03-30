#!/usr/bin/node

const list = require('./100-data.js').list;

const new_list = list.map((x, y) => x * y);
console.log(list);
console.log(new_list);
