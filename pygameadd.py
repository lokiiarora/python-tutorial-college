import pygame

#necessary pygame initializing
pygame.init()

#create a surface that will be seen by the user
screen =  pygame.display.set_mode((400, 400))

#create a varible for degrees pf rotation
degree = 0
while True:
    #clear screen at the start of every frame
    screen.fill((40, 40, 40))

    #create new surface with white BG
    surf =  pygame.Surface((100, 100))
    surf.fill((255, 255, 255))
    #set a color key for blitting
    surf.set_colorkey((255, 0, 0))

    #create shapes so you can tell rotation is happenning
    bigger =  pygame.Rect(0, 0, 100, 50)
    smaller = pygame.Rect(25, 50, 50, 50)

    #draw those two shapes to that surface
    pygame.draw.rect(surf, (100, 0, 0), bigger)
    pygame.draw.rect(surf, (100, 0, 0), smaller)

    ##ORIGINAL UNCHANGED
    #what coordinates will the static image be placed:
    where = 200, 200

    #draw surf to screen and catch the rect that blit returns
    blittedRect = screen.blit(surf, where)

    ##ROTATED
    #get center of surf for later
    oldCenter = blittedRect.center

    #rotate surf by DEGREE amount degrees
    rotatedSurf =  pygame.transform.rotate(surf, degree)

    #get the rect of the rotated surf and set it's center to the oldCenter
    rotRect = rotatedSurf.get_rect()
    rotRect.center = oldCenter

    #draw rotatedSurf with the corrected rect so it gets put in the proper spot
    screen.blit(rotatedSurf, rotRect)

    #change the degree of rotation
    degree += 5
    if degree > 360:
        degree = 0

    #show the screen surface
    pygame.display.flip()

    #wait 60 ms until loop restart
    pygame.time.wait(60)