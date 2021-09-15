#!/usr/bin/node
// Print the number of completed tasks per user.
const request = require('request');
const apiUrl = process.argv[2].concat('?completed=true');
request(apiUrl, (error, response) => {
  if (error) {
    console.error(error);
  }

  const tasks = JSON.parse(response.toJSON().body);

  const result = {};
  for (const task of tasks) {
    const key = String(task.userId);
    if (result[key]) {
      result[key]++;
    } else {
      result[key] = 1;
    }
  }
  console.log(result);
});
