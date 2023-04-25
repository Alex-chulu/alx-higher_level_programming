#!/usr/bin/node
const iconv = require('iconv-lite');

async function readFile(filepath){
	try{
		const data = await fs.readFile(filepath);
		console.log(iconv.decode(data, 'utf-8'));
	} catch (error){
		console.error('Error reading file: ', error);
	}
}
readFile('cisfun');
