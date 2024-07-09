#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';

request(url + process.argv[2], function (err, res, body) {
  if (err) throw err;
  const myactors = JSON.parse(body).characters;
  exactOrder(myactors, 0);
});
const exactOrder = (myactors, x) => {
  if (x === myactors.length) return;
  request(myactors[x], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    exactOrder(myactors, x + 1);
  });
};
