from mcpi import Minecraft,block,event,vec3
import sys
import random

def psuetrig(x):
 direcs=[(1,0),(0,1),(-1,0),(0,-1)]
 return direcs[x%4]

def addToTuple(tup,num):
 total=[0]*len(tup)
 for i in range(len(tup)):
  total[i]=tup[i]+num
 return tuple(total)

def chooseStruct(x,y,Map,count,direc,facing):
 structProb=[0.2,0.8,0,0.8]
 xmod,ymod=psuetrig(facing)
 sxmod,symod=psuetrig(facing+1)
 gridBase=[[0,0],[xmod,ymod],[sxmod,symod],[xmod+sxmod,ymod+symod]]
 buildSpace=True
 for pos in gridBase:
  if Map[x+pos[0]][y+pos[1]]!=-1:
   buildSpace=False
 if buildSpace:
  if random.random()>0.1:
   if random.random()>structProb[(direc-facing)%4] or count<=1:
    return 0
   else:
    return random.randInt(2,count)
  else:
   return -1
 else:
  return -1*int(random.random()<structProb[(direc-facing)%4])

def buildingabuilding(pos,building,Map,facing):
 mc=Minecraft.create()
 plpos=mc.player.getPos()
 x,z=addToTuple(pos,-apothem)
 x,z=5*x,5*z
 x+=plpos.x
 y=plpos.y
 z+=plpos.z
 mc.setBlocks(x-2,y,z-2,x+2,y+4,z+2,0)
 mc.setBlocks(x-2,y-1,z-2,x+2,y-1,z+2,2)
 if building>0:
  f=open("buildings/"+building+".mcbuild","r")
  for piece in f:
   data=piece.split(";")
   data=data[0].split(",")
   flatdata=[data[0],data[2],data[3],data[5]]
   mc.setBlocks(int(flatdata[(0-facing)%4])+x,int(data[1]),int(flatdata[(1-facing)%4])+z,int(flatdata[(2-facing)%4])+x,int(data[4]),int(flatdata[(3-facing)%4])+z,int(data[6]))
 elif building==0:
  mc.setBlocks(x-1,y-1,z-1,x+1,y-1,x+1,4)
  direcs=[(1,0,0),(0,1,1),(-1,0,2),(0,-1,3)]
  placements=[[2,-1,3,1],[-1,2,1,3],[-3,-1,-2,1],[-1,-2,1,-3]]
  for xmod,zmod,i in direcs:
   if Map[pos[0]+xmod][pos[1]+zmod]==0:
    mc.setBlocks(x+placements[i][0],y-1,z+placements[i][1],x+placements[i][2],y-1,x+placements[i][3],4)

def build(structCount,apothem):
 buildMap=[[-1]*(apothem*2+1)]*(apothem*2+1)
 buildList=[[(apothem,apothem),1,0]]
 activityList=[]
 buildMap[apothem][apothem]=1
 buildDirecs=[(1,0,0),(0,1,1),(-1,0,2),(0,-1,3)]
 for xmod,ymod,i in buildDirecs:
  activityList.append([(apothem+xmod,apothem+ymod),i])
  buildMap[apothem+xmod][apothem+ymod]=0
  buildList.append([(apothem+xmod,apothem+ymod),0,i])
 for act in activityList:
  herex,herey=act[0]
  for xmod,ymod,i in buildDirecs:
   if buildMap[herex+xmod][herey+ymod]==-1
    building=chooseStruct(herex+xmod,herey+ymod,buildMap,structCount,act[1],i)
    buildMap[herex+xmod][herey+ymod]=[building]
    buildList.append([(herex+xmod,herey+ymod),building,i])
    if building>1:
     sxmod,symod,si=buildDirecs[(i+1)%4]
     buildMap[herex+xmod+sxmod][herey+ymod+symod]=building
     buildMap[herex+xmod*2][herey+ymod*2]=building
     buildMap[herex+xmod*2+sxmod][herey+ymod*2+symod]=building
    else:
     activityList.append([(herex+xmod,herey+ymod),i])
  activityList.remove(act)
 for data in buildList:
  buildingabuilding(data[0],data[1],buildMap,data[2])
if __name__=='__main__':
 build(sys.argv[1],sys.argv[2])