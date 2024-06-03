#!/usr/bin/node
const args = process.argv.slice(2);
const argnum = args.length;

if (argnum === 0) {
  console.log('No argument');
} else if (argnum === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
