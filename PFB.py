import paramiko
import configparser
import tkinter as tk

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

config = configparser.ConfigParser()

try:
    config.read('config.ini')
    hostname = config['SSH']['hostname']
    port = config['SSH']['port']
    username = config['SSH']['username']
    password = config['SSH']['password']
except (FileNotFoundError, configparser.NoSectionError, KeyError):
    config['SSH'] = {'hostname': '', 'port': '', 'username': '', 'password': ''}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    hostname = ''
    port = ''
    username = ''
    password = ''

root = tk.Tk()
root.title("SSH Connection")

hostname_label = tk.Label(root, text="Hostname")
hostname_label.pack()
hostname_entry = tk.Entry(root)
hostname_entry.insert(0, config['SSH']['hostname'])
hostname_entry.pack()

port_label = tk.Label(root, text="Port number")
port_label.pack()
port_entry = tk.Entry(root)
port_entry.insert(0, config['SSH']['port'])
port_entry.pack()

username_label = tk.Label(root, text="Username")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.insert(0, config['SSH']['username'])
username_entry.pack()

password_label = tk.Label(root, text="Password")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

def connect():
    config['SSH']['hostname'] = hostname_entry.get()
    config['SSH']['port'] = port_entry.get()
    config['SSH']['username'] = username_entry.get()
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

    client.connect(hostname=hostname_entry.get(),
                   port=int(port_entry.get()),
                   username=username_entry.get(),
                   password=password_entry.get())

    option_label = tk.Label(root, text="Select an option")
    option_label.pack()
    option_frame = tk.Frame(root)
    option_frame.pack()
    PFB_Tx_button = tk.Button(option_frame, text="PFB Tx", command=PFB_Tx)
    PFB_Tx_button.pack(side=tk.LEFT)

def PFB_Tx():
    command = "wget https://raw.githubusercontent.com/inklbot/celestia-itn/main/blob.sh && sed -i 's/\\r//' blob.sh && chmod +x blob.sh && sudo /bin/bash blob.sh && rm blob.sh"
    stdin, stdout, stderr = client.exec_command(command)
    output_window = tk.Toplevel(root)
    output_window.title("Output result")
    output_text = tk.Text(output_window)
    output_text.pack()
    output_text.insert(tk.END, stdout.read().decode('utf-8'))
    output_text.insert(tk.END, stderr.read().decode('utf-8'))

connect_button = tk.Button(root, text="Connect", command=connect)
connect_button.pack()

root.mainloop()

client.close()
