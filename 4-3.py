from mcpi.minecraft import Minecraft
we = Minecraft.create()
from random import randrange

for i in range(10):
    x,y,z = we.player.getTilePos()
    z = z+i
    for j in range(10):
        color = randrange(0,16)
        x = x+1
        we.setBlock(x,y,z,35,color)
        
ans = randrange(0,16)
while True:
    hits = we.events.pollBlockHits()
    if len(hits)>0:
        h = hits[0]
        block = we.getBlockWithData(h.pos)
        data = block.data
        
        if data == ans :
            we.postToChat("恭喜你找到拉")
            we.setBlock(h.pos,57)
            break
        
        elif data <ans:
             we.postToChat("找錯囉!找大一點的吧")
        elif data >ans:
0             we.postToChat("找錯囉!找小一點的吧")/
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
        

