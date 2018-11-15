using System.IO;
using System.Net.Sockets;
using System.Threading.Tasks;

namespace SomeServerApplication
{    class Example
    {
        public void Start()
        {
            var port = 2424;
            var listener = TcpListener.Create(port);
            listener.Start();
            while (true)
            {
                var client = listener.AcceptTcpClient();
                // handle new client connection
                Task.Run(() =>
                {
                    using (var stream = client.GetStream())
                    using (var reader = new StreamReader(stream))
                    using (var writer = new StreamWriter(stream) { AutoFlush = true })
                        while (client.Connected)
                        {
                            try
                            {
                                var line = reader.ReadLine();
                                // process command
                                writer.WriteLine(line);
                            }
                            catch (IOException)
                            {
                                if (client.Connected) throw;
                            }
                        }
                });
            }
        }
    }
}