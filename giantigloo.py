from mcpi.minecraft import Minecraft
import shapes

size=32

def main(place):
 mc=Minecraft.create(place,4711)
 x,y,z=mc.player.getPos()
 shapes.sphere(mc,x,y,z,size,size,size,80)
 shapes.sphere(mc,x,y,z,size-1,size-1,size-1,0)
 shapes.cylinder(mc,x,y,z-(size+(size-1)/2-1)-size/6,(size-1)/2+1,(size-1)/2+1,int((size-1)/2),shapes.XY,80)
 shapes.cylinder(mc,x,y,z-(size+(size-1)/2-1),(size-1)/2,(size-1)/2,int((size-1)/2),shapes.XY,0)
 mc.setBlocks(x-size,y-size,z-size-(size+(size-1)/2-1)-((size-1)/2+1),x+size,y-1,z+size,80)

if __name__=='__main__':
 main("127.0.0.1")
