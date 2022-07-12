from flask import Flask
from flask import redirect

app = Flask(__name__)
@app.route('/')
def hello_world():
	return 'Hello World'

@app.route('/rv')
def rvce():
	return'RVITM ROCKS'
app.add_url_rule('/' , 'rvce' , rvce)	

@app.route('/hello')
def hello():
	return redirect("http://www.rvce.edu.in", code=302)

@app.route('/hello/<name>')
def hello_name(name):
	return 'Hello %s!' % name

@app.route('/rev/<float:revno>')
def revision(revno):
	return 'Revision number %f' % revno


if __name__ == '__main__':
	app.run()
