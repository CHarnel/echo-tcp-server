require 'socket'
 
Socket.tcp_server_loop(2424) do |conn, addr|
  Thread.new do
    client = "#{addr.ip_address}:#{addr.ip_port}"
    puts "#{client} is connected"
    begin
      loop do
        line = conn.readline
        puts line
        conn.puts(line)
      end
    rescue EOFError
      conn.close
      puts "#{client} has disconnected"
    end
  end
end