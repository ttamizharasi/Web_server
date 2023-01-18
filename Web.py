from http.server import HTTPServer , BaseHTTPRequestHandler
content = """
<html>
<head>
</head>
<body>
<h1>Welcome to Saveetha Engineering College</h1>
</body>
</html>
"""
class HelloHandler(BaseHTTPRequestHandler):
     def do_GET(self):
         self.send_response(200)
         self.send_header('Content-type', 'text/html; charset=utf-8')
         self.end_headers()
         self.wfile.write(content.encode())
server_address = ('',80)
httpd=HTTPServer(server_address,HelloHandler)
print("The Server is running")
httpd.serve_forever()