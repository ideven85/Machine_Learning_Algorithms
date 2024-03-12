import pygame
import pygame.camera
import sys
clist = pygame.camera.list_cameras()

webcam=pygame.camera.Camera(0, (1280,720), "RGB")
webcam.start()
img = webcam.get_image()

WIDTH = img.get_width()
HEIGHT = img.get_height()

screen = pygame.display.set_mode( ( WIDTH, HEIGHT ) )
pygame.display.set_caption("pyGame Camera View")

while True :
    for e in pygame.event.get() :
        if e.type == pygame.QUIT :
            sys.exit()



    # draw frame
    screen.blit(img, (0,0))
    pygame.display.flip()
    # grab next frame    
    img = webcam.get_image()
    pygame.image.save( img, "test.png")