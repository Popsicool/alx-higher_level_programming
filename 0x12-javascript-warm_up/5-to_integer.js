#!/usr/bin/node

const process = require('process');
const arg1 = parseInt(process.argv[2]);
if (isNaN(arg1)) {
  console.log('Not a number');
} else {
  console.log('My number: %s', arg1);
}
