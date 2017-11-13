from mcpi.minecraft import Minecraft
import math

XY=0
XZ=1
YZ=2

def cwm(x,xrad,yrad):
 return round(yrad*(1-(x/xrad)**2)**0.5-0.5)

def order(inx,iny,inz,axis):
 facings=[(inx,iny,inz),(inx,inz,iny),(iny,inz,inx)]
 return facings[axis]

def cylinder(X,Y,Z,axis,block):
 x,y,z=order(X+1,Y+1,Z+1,axis)
 mc=Minecraft.create("127.0.0.1",4711)
 px,py,pz=mc.player.getPos()
 for i in range(-x+1,x):
  mc.setBlocks(px+i,py-cwm(i,x,y),pz-z+1,px+i,py+cwm(i,x,y),pz+z-1,block)
 mc.player.setPos(px,py+y,pz)
