from meinheld import server
import sqlite3


con = sqlite3.connect("people.db")



db = con.cursor()
db.execute("SELECT name from people;")
name = db.fetchone()
name = name[0]
db.execute("SELECT age from people;")
age = db.fetchone()
age = age[0]



html = f"""
	<link rel="stylesheet" href="https://unpkg.com/chota@latest">
	<h1> Hello My Name Is: {name}!
	<h2> My age is: {age}! </h2>
"""

dogs = f"""
	<link rel="stylesheet" href="https://unpkg.com/chota@latest">
	<h1> Bunnies are Cool </h1>
"""

notfound = f"""
	<link rel="stylesheet" href="https://unpkg.com/chota@latest">
	<h1> 404 Page Not Found Oh No </h1>
"""

def helloworld(environ, start_response):
	if environ['PATH_INFO'] == "/":
		status = '200 OK'
		res = html.encode("utf-8")
		response_headers = [('content-type', "text/html"), ]
		start_response(status,response_headers)
		return [res]
	if environ['PATH_INFO'] == "/bunnies":
		status = '200 OK'
		res = dogs.encode("utf-8")
		response_headers = [('content-type', "text/html") ]
		start_response(status,response_headers)
		return [res]
	else:
		status = '404 NOT_FOUND'
		res = notfound.encode("utf-8")
		response_headers = [('content-type', "text/html") ]
		start_response(status,response_headers)
		return [res]

server.listen(('0.0.0.0', 7000))
print("Server started on :7000")
server.run(helloworld)