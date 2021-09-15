#!/usr/bin/node
// Print the number of completed tasks per user.
const request = require('request');
const apiUrl = process.argv[2];
request(apiUrl, (error, response, body) => {
  if (error) return console.error(error);
  const tasks = JSON.parse(body);
  const result = {};
  for (const task of tasks) {
    if (task.completed) {
      const key = task.userId;
      result[key] ? result[key]++ : result[key] = 1;
    }
  }
  console.log(result);
});
