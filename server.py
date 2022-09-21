import socket

s = socket.socket()
print ("<+> Socket created successfully")

port = 2728

# bind to the port into the socket
# keep the empty string because accept to any request
s.bind(('', port))
print("<+> socket binded to %s" %(port))

# socket -> listening mode
s.listen(5)
print("<+> socket is listening")
print(">----------------------------<")

#This is never ending loop because server should be alive all the time
#       and server should respond to the clients more than one times
while True:

  # accept the connection with client
  conn, addr = s.accept()

  print('\tGot connection from', addr ) # this is a sample console output about connection

  req = conn.recv(1024).decode('utf8')
  # print(conn.recv(1024).decode('utf8'))
    # We can get this kind of request from the client (web browser) after client typed 
    #    "http://localhost:2728/" in url of the browser

      # GET / HTTP/1.1
      # Host: localhost:2728
      # Connection: keep-alive
      # Cache-Control: max-age=0
      # Upgrade-Insecure-Requests: 1
      # something more...
    # so we should respond to it by each route

  convReq = req.strip().split(' ')
  # Here I splitted the server request into parts from spaces and put that array into 'convReq' variable
  # the convReq[0] is the Request method (GET | POST)
  # the convReq[1] is the url routing path ex:-(/, /users, /login)

  file = '' # variable for read pages
  if(convReq[1] == '/'):   # this is the default route '/'
    file = open("htdocs/index.html","r") # Get the 'index.html' file from htdocs folder 
    conn.send(bytes('HTTP/1.x 200 OK','utf8')) # sends the success response(status - 200) because server can find this webpage

  elif(convReq[1] == '/profile'): # this is a route '/users'
    file = open("htdocs/users.html","r")
    conn.send(bytes('HTTP/1.x 200 OK','utf8'))

  else :
    file = open("htdocs/404.html","r") # this is page not found page
    conn.send(bytes('HTTP/1.x 404 Not Found','utf8')) # page not found because a wrong url route. 
                                                   # sends a (404 status) response

  conn.send(bytes('Content-Type : text/html\r\n','utf8')) #  The response content type is text/html
  conn.send((bytes('\r\n','utf8'))) 

  conn.send(bytes(file.read(),'utf8')) 
  # Read the content of file variable and encode it to "utf8" and send to client

  conn.close()
  # Close the connection with the client

