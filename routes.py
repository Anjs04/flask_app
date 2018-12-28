from flask import Flask, render_template

import ssl
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('certs/server.crt', 'certs/server.key')

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/about")
def about():
  return render_template("about.html")

if __name__ == "__main__":
  app.run(host='127.0.0.1',port='5000', debug = True, ssl_context=context)
  