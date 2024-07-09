#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/'

request(url + process.argv[2], function (err, res, body) {
  if (err) throw err;
  const character = JSON.parse(body).characters;
  exactOrder(character, 0);
});
const exactOrder = (character, x) => {
  if (x === character.length) return;
  request(character[x], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    exactOrder(actors, x + 1);
  });
};
