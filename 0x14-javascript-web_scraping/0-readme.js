#!/usr/bin/node
const fs = require('fs');

function read_file_content(file_path) {
    fs.readFile(file_path, 'utf8', function(err, data) {
        if (err) {
            console.log(err);
        } else {
            console.log(data);
        }
    });
}

