#!/usr/bin/node

const fs = require('fs');

const fText = process.argv[2];
const firstText = fs.readFileSync(fText);

const sText = process.argv[3];
const secondText = fs.readFileSync(sText);

const res = process.argv[4];
fs.writeFileSync(res, firstText + secondText);
