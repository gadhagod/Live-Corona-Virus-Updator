const http = require('http');

const request = require('request')
request('https://www.worldometers.info/coronavirus/', function (
  error,
  response,
  body
) {
  var strbody = String(body);
  var strbody = strbody.substring(368, 407);
  var casestart = strbody.indexOf("): ") + 3;
  var caseend = strbody.indexOf(" and ");
  var cases = strbody.slice(casestart, caseend);

  var deathstart = caseend;
  var deathend = strbody.indexOf(" from");
  var deaths = strbody.slice(caseend, deathend);
  var deaths = deaths.replace(" and ", "");

  const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html');
    res.end('<h1><center>Live Covid Updater</center></h1>' + deaths + ' and ' + cases);
  });

  server.listen(3000, () => {});
})
