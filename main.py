from flask import Flask,render_template,request
from flask_cors import CORS
import json
import subprocess #this is to call the cmd line inside python

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template("front.html")

@app.route('/main',methods=['POST'])  
def main():
    print(request.method)                 
    data=request.data                               
    my_data = json.loads(data.decode("utf-8"))
    item = my_data['ii_text']
    #return ('%s' %(item))
    return_code = subprocess.getoutput("sumy edmundson --length=2 --url=%s" %(item))
    return ('%s' %(return_code))

if __name__ == '__main__':
    app.run(debug=True)
"""
def run_command(command):
    p = subprocess.Popen(command,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')
command = 'mysqladmin create test -uroot -pmysqladmin12'.split()
for line in run_command(command):
    print(line)
"""
