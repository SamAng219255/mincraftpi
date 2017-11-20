from mcpi.minecraft import Minecraft
import sys

mc=Minecraft.create()
mc.setBlocks(-128,-64,-128,128,0,128,int(sys.argv[1]))
mc.setBlocks(-128,1,-128,128,64,128,0)
