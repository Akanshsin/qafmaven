const fs = require('fs');

const logFilePath = 'rawlogs.log'; // Replace with the actual path to your log file

fs.readFile(logFilePath, 'utf8', (err, data) => {
  if (err) {
    console.error(`Error reading log file: ${err}`);
    return;
  }

  let captureRequestBody = false;
  let requestBody = '';
  let discoveredItemsList = [];

  const lines = data.split('\n');

  lines.forEach(line => {
    if (line.includes('request body: {')) {
      captureRequestBody = true;
      requestBody += line.substring(line.indexOf('{'));
    } else if (captureRequestBody) {
      requestBody += line;
      if (line.includes('}')) {
        captureRequestBody = false;
        try {
          const json = JSON.parse(requestBody);
          if (json.discoveredItems) {
            discoveredItemsList.push(...json.discoveredItems);
          }
        } catch (parseErr) {
          console.error(`Error parsing JSON: ${parseErr}`);
        }
        requestBody = '';
      }
    }
  });

  if (discoveredItemsList.length > 0) {
    console.log("Discovered Items:");
    discoveredItemsList.forEach((item, index) => {
      console.log(`${index + 1}. ${item}`);
    });
  } else {
    console.log("No discovered items found.");
  }
});
