from flask import Flask

app = Flask ("Olá")
@app.route('/')
def Olá():
    return"Olá mundo!"
