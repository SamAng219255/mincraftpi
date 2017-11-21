from mcpi.minecraft import Minecraft
import sys
import time

mc=Minecraft.create(sys.argv[1],4711)
f=open("sos.txt","r")
for line in f:
 mc.postToChat(line)
 time.sleep(1)
f.close()
