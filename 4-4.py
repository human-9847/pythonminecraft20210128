from mcpi.minecraft import Minecraft
we = Minecraft.create()
list2 = [[12,41,14],[35,73,86]]

myID = we.getPlayerEntityId("ravishingrice12")
x,y,z = we.entity.getTilePos(myID)

startX = x

for i in list2:
    for j in i:
        
        we.setBlock(x,y,z,j)
        x = x+1
    x = startX
    z = z-1
