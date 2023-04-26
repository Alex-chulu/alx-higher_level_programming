#!/usr/bin/node
// Include fs module
const fs = require("fs");

if (process.argv.length !== 3) {
  console.log("Usage: node cisfun");
  process.exit(1);
}

const filePath = process.argv[2];

fs.readFile(filePath, { encoding: "utf-8" }, (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
