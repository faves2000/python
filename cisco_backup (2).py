import sys
import time
import paramiko
import os
import cmd
import datetime

now = datetime.datetime.now()
# mention username and password
user = backup
password = e!P3@Gp2Tc-L
#enable_password = 5qGwEtCBB62PgTf
# mention username and password
port=22
f0 = open('homeuserpythoncisco_routerswitch.txt')
for ip in f0.readlines()
      ip = ip.strip()
      filename_prefix ='homeuserpythonbackup' + ip
      ssh = paramiko.SSHClient()
      ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
      ssh.connect(ip,port, user, password, look_for_keys=False)
      chan = ssh.invoke_shell()
      time.sleep(2)
      #chan.send('enablen')
      #chan.send(enable_password +'n')
      #time.sleep(1)
      chan.send('term len 0n')
      time.sleep(1)
      chan.send('sh runn')
      time.sleep(20)
      output = chan.recv(999999)
      #filename = %s_%.2i%.2i%i_%.2i%.2i%.2i % (ip,now.year,now.month,now.day,now.hour,now.minute,now.second)
      filename = %s_%.2i-%.2i-%i_%.2i-%.2i-%.2i % (filename_prefix,now.day,now.month,now.year,now.hour,now.minute,now.second)
      f1 = open(filename, 'a')
      f1.write(output.decode(utf-8) )
      f1.close()
      ssh.close()
      f0.close()
