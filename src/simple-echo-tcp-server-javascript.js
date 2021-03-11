const net = require('net');

const ip = '127.0.0.1';
const port = 2424;

const server = net.createServer(function(socket) {
  socket.write('Welcome!\r\n');
    
  socket.on('data', function (data){
    try {
      let dataString = data.toString();
      console.log('Data Received from client: ' + dataString);
      // process command
      const response = 'Sample response\r\n';
      socket.write(response);
    } catch (err) {
        console.error(err);
    }
  });

  socket.on('error',function(error){
    console.log('Error : ' + error);
  });

  socket.on('end', function (){
    console.log('Closing Connection...');
  });
});
  
server.listen(port, ip);
console.log(`Server listening on port ${port}`);
