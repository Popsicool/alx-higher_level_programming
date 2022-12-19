#!/usr/bin/node
const process = require('process');
const all = process.argv;
if (all.length < 4) {
  console.log(0);
} else {
  let highest = 0;
  let second = 0;
  for (let i = 2; all[i]; i++) {
    if (i === 2) {
      highest = all[i];
      second = all[i];
    } else if (all[i] >= highest) {
      highest = all[i];
    } else if (all[i] > second) {
      second = all[i];
    }
  }
  console.log(second);
}
