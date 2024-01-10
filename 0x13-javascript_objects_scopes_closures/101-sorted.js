#!/usr/bin/node
const dict = require('./101-data').dict;
const nKeys = Object.keys(dict);
const values = Object.values(dict);
let matched;
const result = {};
// loop over the values
for (let i = 0; i < values.length; i++) {
  result[JSON.stringify(values[i])] = [];
  matched = nKeys.filter(key => dict[key] === values[i]);
  matched.forEach(item => result[JSON.stringify(values[i])].push(item));
}
console.log(result);
