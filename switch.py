import getpass
import telnetlib

HOST = ["eng-blr-switch-037","]

user = ""
password = ""

for i in HOST:
    tn = telnetlib.Telnet(i.strip())
    tn.write(b"\n")
    tn.read_until(b"Username: ")
    usr=f"{user}"
    tn.write(usr.encode('ascii')+b"\n") 
    tn.read_until(b"Password: ")
    new=f"{password}"
    tn.write(new.encode('ascii')+b"\n") 
    tn.write(b"\n")
    bk=f"upload config 10.197.1.20 {i}.xsf vr vr-mgmt\n"
    tn.write(bk.encode('ascii')+b"\n") 
    tn.write(b"\n")
    tn.write(b"save\n")
    tn.write(b"\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))
    
print("The end")
