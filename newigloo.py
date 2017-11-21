from mcpi.minecraft import Minecraft
import shapes
from math import ceil

def main(place):
 mc=Minecraft.create(place,4711)
 x,y,z=mc.player.getPos()
 mc.setBlocks(x-5,y,z-20,x+5,y+5,z-8,0)
 shapes.sphere(mc,x,y,z-15,5,5,5,80,0,4,4,4,0.5,1)
 shapes.cylinder(mc,x,y,z-10,3,3,1,shapes.XY,80)
 shapes.cylinder(mc,x,y,z-10,2,2,1,shapes.XY,0)
 height=0
 nx,ny,nz=x,y-1,z-15
 clear=True
 while clear:
  height+=1
  clearpos=0
  pos=[(0,0),(5,5),(-5,5),(-5,-5),(5,-5)]
  for xmod,zmod in pos:
   if mc.getBlock(xmod+nx,ny-height,zmod+nz) in [0,8,9,10,11,31,37,38,39,40,65,78,102,107,]:
    clearpos+=1
  if clearpos==0:
   clear=False
 shapes.cylinder(mc,x,y-1-ceil(height/2),z-15,5,ceil(height/2),5,shapes.XZ,80)
 mc.setBlocks(x-2,y-1-height,z-11,x+2,y-1,z-9,80)
 #mc.setBlocks(x-5,y-1,z-20,x+5,y-1,z-8,80)

if __name__=='__main__':
 main("127.0.0.1")
