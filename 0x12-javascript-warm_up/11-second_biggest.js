#!/usr/bin/node

const args = process.argv;
if (args.length <= 3) {
  console.log('0');
} else {
  args.splice(0, 2);
  const scd = scdBiggest(args);
  console.log(scd);
}

function scdBiggest (list) {
  const mux = list.sort((b, c) => b - c);
  return mux[mux.length - 2];
}
