from flask import Flask, render_template, request
import os

web_server = Flask(__name__, template_folder='dashboard')

@web_server.route('/')
def index():
    return render_template('index.html')

import subprocess

@web_server.route('/run_command', methods=['POST'])
def run_command():
    command = request.form.get('command')
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()
    
    if process.returncode == 0:
        return f"PayForBlob transactions execution complete.\n\nResult:\n{stdout.decode('utf-8')}"
    else:
        return f"PayForBlob transactions execution failed.\nError:\n{stderr.decode('utf-8')}", 500


if __name__ == '__main__':
    web_server.run(host='0.0.0.0', debug=True)
