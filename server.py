from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''
<!doctype html>
<html>
    <head>
    </head>
    <body bgcolor="cyan">
        <table border="1" align="center" bgcolor="pink" cellpadding="10"
        <caption><h1 align="center">list of protocol</h1></caption>
        <tr>
            <th>s.no</th>
            <th>name of the layer</th>
            <th>name of the protocol</th>
        </tr>
        <tr>
            <td>1</td><td>application layer</td><td>HTTP,FTP</td>
        </tr>
        <tr>
            <td>2</td><td>transport layer</td><td>TCP & UDP</td>
        </tr>
        </table>
    </body>
    </head>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =(' ',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()