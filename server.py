import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# AF_INET       --> ipv4
# SOCK_STREAM   --> tcp/ip protocol 
print("<+> Socket created successfully")

port = 2728 # This is the port that bind to the socket

# bind to the port into the socket  |   127.0.0.1 because accept to any request
s.bind(('127.0.0.1', port))

print("<+> socket binded to %s" % (port))  
s.listen(5)  # socket -> listening mode
print("<+> socket is listening")
print(">----------------------------<")

# This is never ending loop because server should be alive all the time
#       and server should respond to the clients more than one times
while True:

    conn, addr = s.accept()
    # accept the connection with client

    print('\tGot connection from', addr)
    # this is a sample console output about connection

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

    convReq = req.split(' ')
    # Here I splitted the server request into parts from spaces and put that array into 'convReq' variable
    # the convReq[0] is the Request method (GET | POST)
    # the convReq[1] is the url routing path ex:-(/, /users, /login)

    filePath = convReq[1] # get the route as file path
    file = ''  # declaring variable for read pages

    if (convReq[1] == '/'):   # this is the default route '/' | default route responding with the index.html file
        filePath = '/index.html'
    
    # use try-exept because we should catch the errors
    try :
        file = open('htdocs'+filePath,'r') 
        conn.send(bytes('HTTP/1.x 200 OK', 'utf8')) # This is the success respond status 
        conn.send(bytes(' Content-Type : text/html\r\n', 'utf8')) # The response content type is text/html
        conn.send((bytes('\r\n', 'utf8')))
        conn.send(bytes(file.read(), 'utf8'))
        # Read the content of file variable and encode it to "utf8" and send to client
        file.close()
    except :
        conn.send(bytes('HTTP/1.x 404 Not Found', 'utf8'))
        # If the file is not available sent the 404 not found response
        conn.send(bytes(' Content-Type : text/html\r\n', 'utf8')) # The response content type is text/html
        conn.send((bytes('\r\n', 'utf8')))
        conn.send(bytes("<center><p>Oops! Page not found <br> 404 error</p></center>", 'utf8')) 
        # send a response that page not found

    conn.close()
    # Close the connection with the client
