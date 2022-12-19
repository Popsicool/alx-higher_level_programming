#!/usr/bin/node
const process = require('process');
const all = process.argv;
if (all.length < 4) {
  console.log(0);
} else {
  let highest = 0;
  let second = 0;
  for (let i = 2; parseInt(all[i]); i++) {
    if (i === 2) {
      highest = parseInt(all[i]);
      second = parseInt(all[i]);
    } else if (parseInt(all[i]) >= highest) {
      second = highest;
      highest = parseInt(all[i]);
    }
  }
  console.log(second);
}
