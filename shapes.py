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

def cylinder(x,y,z,axis,block):
 x,y,z=x+1,y+1,z+1
 mc=Minecraft.create("127.0.0.1",4711)
 px,py,pz=mc.player.getPos()
 if axis==0:
  for i in range(-x+1,x):
   mc.setBlocks(px+i,py-cwm(i,x,y),pz-z+1,px+i,py+cwm(i,x,y),pz+z-1,block)
 elif axis==1:
  for i in range(-x+1,x):
   mc.setBlocks(px+i,py-y+1,pz-cwm(i,x,y),px+i,py+y-1,pz+cwm(i,x,y),block)
 elif axis==2:
  for i in range(-y+1,y):
   mc.setBlocks(px-x+1,py+i,pz-cwm(i,x,y),px+x-1,py+i,pz+cwm(i,x,y),block)
 mc.player.setPos(px,py+y,pz)

def sphere(X,Y,Z,block):
 print("Not yet implemented.")
