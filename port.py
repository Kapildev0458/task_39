  
#!/usr/bin/python3
print("Content-Type: text/html")    
print()          
                   

import cgi
import subprocess as sub
cmd = cgi.FieldStorage()
img=cmd.getvalue("x")
cont=cmd.getvalue("y")
st,out=sub.getstatusoutput('sudo docker run -dit --name=' + cont +' '+img)
if st==0:
    print("Your Container Successfully Launch : " +out)
else:
    print("Error Occurred \n" + out)
