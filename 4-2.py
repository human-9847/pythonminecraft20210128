from mcpi.minecraft import Minecraft
we = Minecraft.create()
x,y,z = we.player.getTilePos()
for i in range(20):
    r = random.randrange(1,7)
    if r == 1:
        we.setBlocks(x,y,z,x,y,z+4,41)
        z = z+4
    if r == 2:
        we.setBlocks(x,y,z,x,y,z-4,41)
        z = z-4
    if r == 3:
        we.setBlocks(x,y,z,x+4,y,z,41)
        x = x+4
    if r == 4:
        we.setBlocks(x,y,z,x-4,y,z,41)
        x = x-4
    if r == 5:
        we.setBlocks(x,y,z,x,y+4,z,41)
        y = y+4
    if r == 6:
        we.setBlocks(x,y,z,x,y-4,z,41)
        y = y-4
    