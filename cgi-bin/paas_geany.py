#!/usr/bin/python36

print("content-type: text/html")
print("")

import subprocess
#import crypt
#import getpass
import cgi

form = cgi.FieldStorage()
usr = form.getvalue('usr')
port = form.getvalue('port')

#usr = input("enter new user you want to add : ")
#port = input("enter a number (1024 - 65000) : ")

#passw = "iuc"
#passw = crypt.crypt(passw)
#a=subprocess.getstatusoutput("sudo useradd -p '"+passw+"' "+usr)
#print("created")
#if a[0] == 0:
b = subprocess.getstatusoutput("sudo docker run -dit -p {1}:22 --name {0} geany_test:v1".format(usr , port))
#b = subprocess.getstatusoutput("docker run -dit --ipc=host --net=host --env=DISPLAY --volume=$HOME/.Xauthority:/root/.Xauthority --name={0} centos_net:v1  geany".format(usr))
if b[0] == 0:
	print("geany is ready, run this script in your terminal !!!!!!!!  \n\n\n")
#print("docker run -dit --ipc=host --net=host --env=DISPLAY --volume=$HOME/.Xauthority:/root/.Xauthority --name={0} centos_net:v1 geany".format(usr))
#print("\n\nssh {0}@192.168.43.7 -t -X 'docker start {0};sleep 5000' ".format(usr))
	print("<br><br> <strong> ssh 192.168.43.7 -p {} -X geany</strong>".format(port))
	print("\n \n YOUR DEFAULT PASSWORD IS 'iuc'")
else:
	print("user name or number already exits, try again!!!")    

#else:
#       print("user name already exits, TRY AGAIN") 
       


#print ("user name for login: geany")
#print("\n \n YOUR DEFAULT PASSWORD IS 'iuc'")




print("""  <style type="text/css">

		#pre {
	background-color: #051e30 ;
    border-color: #289ff4;
    border-style: solid;
    border-width: 1px 1px 1px 4px;
    font-family: 'Cutive Mono', monospace;
    line-height: 19px;
    margin: 30px 0;
    overflow-x: auto;
    overflow-y: hidden;
    padding: 10px 10px 10px 18px;
    word-wrap: break-word;
    border: 1px solid #ddd;
    
    vertical-align: baseline;
	display: block;
	color: #fff;
} 
</style>

""")


	

print("""  <pre id="pre"><strong> For Windows: </strong> 
DOWNLOAD MOBAXTERM FROM HERE!!!!!
<a href="https://download.mobatek.net/1062018041114250/MobaXterm_Installer_v10.6.zip" download>Download Mobaxterm</a>
$ Open Mobaxterm and Click on start local terminal and wait for terminal to arrive
<strong>Copy the following command and execute it!!</strong> </pre>  \n """)

print("\n \n ssh geany@192.168.43.7 -X geany")

print(""" <pre id="pre"> \n
<strong>Type your password</strong>
$ your default password is : iuc
</pre>
""")

