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

def cylinderold(x,y,z,axis,block):
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

def sphereold(X,Y,Z,block):
 print("X:",X,"Y:",Y,"Z:",Z)
 for i in range(1-Z,Z):
  print("i:",i)
  x,y,z=int(cwm(i,X,Y)+1),int(cwm(i,X,Y)+1),i+1
  print("x:",x,"y:",y,"z:",z)
  px,py,pz=mc.player.getPos()
  px,py,pz=int(px)+0.5,int(py)+0.5,int(pz)+0.5
  for j in range(-x+1,x):
   mc.setBlocks(px+j,py-cwm(j,x,y),pz-z+1,px+j,py+cwm(j,x,y),pz+z-1,block)
 mc.player.setPos(px,py+Y,pz)

def sphere(mc,px,py,pz,X,Y,Z,block):
 mc.player.setPos(px,py+Y,pz)
 for x in range(-X,X):
  for y in range(-Y,Y):
   for z in range(-Z,Z):
    if ((x/X)**2)+((y/Y)**2)+((z/Z)**2)<1:
     mc.setBlock(px+x,py+y,pz+z,block)
 mc.player.setPos(px,py+Y,pz)

def cylinder(mc,px,py,pz,X,Y,Z,axis,block):
 mc.player.setPos(px,py+Y,pz)
 if axis%3==0:
  for x in range(-X,X):
   for y in range(-Y,Y):
    if ((x/X)**2)+((y/Y)**2)<1:
     mc.setBlocks(px+x,py+y,pz-Z,px+x,py+y,pz+Z,block)
 elif axis%3==1:
  for x in range(-X,X):
   for z in range(-Z,Z):
    if ((x/X)**2)+((z/Z)**2)<1:
     mc.setBlocks(px+x,py-Y,pz+z,px+x,py+Y,pz+z,block)
 elif axis%3==2:
  for y in range(-Y,Y):
   for z in range(-Z,Z):
    if ((y/Y)**2)+((z/Z)**2)<1:
     mc.setBlocks(px-X,py+y,pz+z,px+X,py+y,pz+z,block)
 mc.player.setPos(px,py+Y,pz)
