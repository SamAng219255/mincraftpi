import sys
from mcpi.minecraft import Minecraft

knownnames=["Jeremiah","Ryan","Sam","BrianW","Anton","Cynthia","BryanH","Front","Carlos"]
knownips=["10.183.4.123","10.183.4.134","10.183.4.133","10.183.4.121","10.183.4.120","10.183.4.129","10.183.4.126","10.183.13.13","10.183.4.137"]

pos=[]
if len(sys.argv)<5:
 mc=Minecraft.create("127.0.0.1",4711)
 pos.extend(sys.argv[1].split(" "))
elif sys.argv[1] in knownnames:
 mc=Minecraft.create(knownips[knownnames.index(sys.argv[1])],4711)
 pos.extend(sys.argv[2].split(" "))
else:
 mc=Minecraft.create(sys.argv[1],4711)
 pos.extend(sys.argv[2].split(" "))

truepos=[]
ppos=[0,0,0]
ppos[0],ppos[1],ppos[2]=mc.player.getPos()
for i in range(len(pos)):
 if pos[i][0]=="~":
  truepos.append(int(pos[i][1:])+ppos[i])
 else:
  truepos.append(int(pos[i]))
mc.player.setPos(truepos[0],truepos[1],truepos[2])
