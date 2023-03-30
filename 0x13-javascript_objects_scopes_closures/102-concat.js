#!/usr/bin/node
const files = require('files');

const file_1 = process.argv[2];
const file_2 = process.argv[3];
const file_3 = process.argv[4];

if (
  files.existsSync(file_1) &&
files.statSync(file_1).isFile &&
files.existsSync(file_2) &&
files.statSync(file_2).isFile &&
file_3 !== undefined
) {
  const firstContent = files.readFileSync(file_1);
  const secondContent = files.readFileSync(file_2);
  const stream = files.createWriteStream(file_3);

  stream.write(firstContent);
  stream.write(secondContent);
  stream.end();
}
