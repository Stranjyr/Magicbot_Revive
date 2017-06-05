const http = require('http');
var fs = require('fs');

const hostname = '0.0.0.0';
const port = 5000;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  //res.setHeader('Content-Type', 'text/plain');
  fs.createReadStream("index.html").pipe(res);
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
