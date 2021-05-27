user = "mohammed.afzal"
pwd = "Pur5*arg"

fread = open('cdsa_devices.txt', 'r')
lines = fread.readlines()

fcmd = open('command.txt', 'r')
clines = fcmd.readlines()
fwrite = open("temp_inband_logins.txt", 'a')
temp = ''
for i in lines:
for c in clines:
p = paramiko.SSHClient()
p.set_missing_host_key_policy(paramiko.AutoAddPolicy())
p.connect(i.strip(), port=22, username=user, password=pwd, allow_agent=False,look_for_keys=False)
stdin, stdout, stderr = p.exec_command(c)
opt = stdout.readlines()
opt = "".join(opt) + "\n"
print(opt)
i = i.rstrip('\n')
i = i.strip()
temp = temp + i+'# '+ c + opt
#fwrite.writelines(i+'# '+c)
#fwrite.writelines(opt)
p.close()
temp = temp.replace('Error: AAA authorization failed AAA_AUTHOR_STATUS_METHOD=16(0x10)', '')
fwrite.write(temp)
fwrite.close()