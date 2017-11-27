from mcpi.minecraft import Minecraft
import sys,time

mc=Minecraft.create(sys.argv[1])
x,y,z=mc.player.getPos()
while True:
 X,Y,Z=mc.player.getPos()
 mc.player.setPos((X-x)*int(sys.argv[2])+x,Y,(Z-z)*int(sys.argv[2])+z)
 x,y,z=mc.player.getPos()
 #time.sleep(0.05)
