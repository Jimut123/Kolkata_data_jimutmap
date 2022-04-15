import os

for i in range(10):
    command = "git add Kolkata_00"+str(i)
    os.system(command)
    command = "Kolkata_00"+str(i)
    os.system("git commit -m {}".format(command))
    os.system("git push")


for i in range(10,100):
    command = "git add Kolkata_0"+str(i)
    os.system(command)
    command = "Kolkata_0"+str(i)
    os.system("git commit -m {}".format(command))
    os.system("git push")

