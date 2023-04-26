#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.log('completed tasks');
  process.exit(1);
}

const todosApiUrl = process.argv[2];

request(todosApiUrl, { json: true }, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  if (response.statusCode !== 200) {
    console.log(`Error: ${response.statusMessage}`);
    return;
  }

  const completedTasksByUser = {};

  body.forEach(todo => {
    if (todo.completed) {
      if (completedTasksByUser[todo.userId]) {
        completedTasksByUser[todo.userId]++;
      } else {
        completedTasksByUser[todo.userId] = 1;
      }
    }
  });

  for (const userId in completedTasksByUser) {
    console.log(`User ${userId} completed ${completedTasksByUser[userId]} tasks.`);
  }  
});

