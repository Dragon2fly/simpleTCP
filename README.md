# simpleTCP
a simple tcp server and client, serve as a basic for chat programs

These are a very basic server and client base on tcp tunnel run on custom port.

The **server** will listen for up to *backlog* connection on the line. 

The **client** waits for user input message, then makes connection to the server, sends the message to the server and close connection. Then *repeat* again untill user inputs an empty message.
