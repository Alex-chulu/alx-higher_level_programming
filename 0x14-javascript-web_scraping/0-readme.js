#!/usr/bin/node
// Include fs module
const fs = require('fs');
const filepath = 'cisfun';
// Calling the readFileSync() method
// to read 'input.txt' file
const data = fs.readFileSync(filepath,{encoding:'utf8', flag:'r'});

// Display the file data
console.log(data);
