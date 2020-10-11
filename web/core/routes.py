from flask import Flask, session, redirect, render_template, request, flash
from paramiko import SSHClient, AutoAddPolicy
from database import *
from main import App as app
from base64 import encode, decode

@app.route('/')
@app.route('/index')
def login():
    method = request.method
    if method = request.method:
        username = request.form["username"]
        password = request.form["user_pass"]
        Users.query.filter_by(user=username, password=)
	return render_template("index.html")

@app.route("/register", methods=["GET","POST"])
def register():
	method = request.method
    if method == "POST":
    	username = request.form["username"]
    	password = request.form["user_pass"]
    	conf = request.form["conf_pass"]
        if conf == password:
            register = Users(name=username, passwd=password)
            db.session.add(register)
            db.session.commit()
            return redirect(url_for("login"))
        message = flash(f"Login Fialed, check credentials and try again.")

    return render_template("register.html")

@app.route('/new_ssh', methods=["GET","POST"])
def new_SSH(user, password, port, ip_address):
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy)
    ssh(ip_address, port=port, username=user, password=password)
    device_hash = encode(ip_address+str(port)+user+password)
    try:
        Devices.query.filter_by(ip=ip_address).first()
        ssh.connect()
    except:
        new_device = Devices(ip=ip_address, username=user, password=password, device_hash=device_hash)
        ssh.connect()
    stdin, stdout, stderr = ssh.exec_command('whoami')
    
