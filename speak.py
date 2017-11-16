import sys
from mcpi.minecraft import Minecraft

knownnames=["Jeremiah","Ryan","Sam","BrianW","Anton","Cynthia","BryanH","Front","Carlos"]
knownips=["10.183.4.123","10.183.4.134","10.183.4.133","10.183.4.121","10.183.4.120","10.183.4.129","10.183.4.126","10.183.13.13","10.183.4.137"]

if sys.argv[1] in knownnames:
 mc=Minecraft.create(knownips[knownnames.index(sys.argv[1])])
else:
 mc=Minecraft.create(sys.argv[1],4711)
#txt=""
#for i in range(2,len(sys.argv)):
# txt+=sys.argv[i]
# txt+=" "
mc.postToChat(sys.argv[2])

"""
Jeremiah: 123
Ryan: 134
Sam: 133
Brian W: 121
ALex: 120
Cynthia: 129
Bryan H: 126
"""
