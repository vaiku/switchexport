import getpass
import telnetlib

HOST = ["eng-blr-switch-037","eng-blr-switch-126","eng-blr-switch-137"]

user = ""
password = ""

for i in HOST:
    tn = telnetlib.Telnet(i.strip())
    tn.write(b"\n")
    tn.read_until(b"login: ")
    usr=f"{user}"
    tn.write(usr.encode('ascii')+b"\n") 
    tn.read_until(b"Password: ")
    new=f"{password}"
    tn.write(new.encode('ascii')+b"\n") 
    tn.write(b"\n")
    tn.write(b"copy running-config startup-config\n\n")
    cm=f"copy running-config tftp://10.197.1.120/{i}\n"
    tn.write(vm.encode('ascii')+b"\n") 
    tn.write(b"\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))
    
print("The end")
