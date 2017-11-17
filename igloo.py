from mcpi.minecraft import Minecraft
import shapes

def main(place):
 mc=Minecraft.create(place,4711)
 x,y,z=mc.player.getPos()
 mc.setBlocks(x-21,y,z-21,x+20,y+20,z+20,0)
 shapes.sphere(mc,x,y,z-15,5,5,5,80)
 shapes.sphere(mc,x,y,z-15,4,4,4,0)
 shapes.cylinder(mc,x,y,z-10,3,3,1,shapes.XY,80)
 shapes.cylinder(mc,x,y,z-10,2,2,1,shapes.XY,0)
 mc.setBlocks(x-21,y-1,z-21,x+20,y-1,z+20,80)

if __name__=='__main__':
 main("127.0.0.1")
