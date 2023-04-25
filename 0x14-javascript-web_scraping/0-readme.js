#!/usr/bin/node
const fs = require('fs').promises;

async function readFile(filepath){
  try{
    const data = await fs.readFile(filepath);
    console.log(data.toString());
} catch (error){
    console.error('Error reading file: ', error);
  }
}
readFile(cisfun);
