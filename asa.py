import pygame, sys
from pygame.locals import *
from time import sleep
import os
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((920, 300))
pygame.display.set_caption('CRUSH CÓ YÊU BẠN KHÔNG?')
Trang=(255,255,255)
Den=(0,0,0)
Xanhla=(0,255,0)
Do=(255,0,0)
Xanhduong=(0,178,191)


def hamchu(chu, mau, ngang, doc, cochu):
    font = pygame.font.SysFont('Calibri', cochu)
    chu_ra = font.render(chu, True, mau)
    window.blit(chu_ra, [ngang, doc])

while True:
    pygame.display.flip()
    clock.tick(15)
    event_list = pygame.event.get()

    mouse_x, mouse_y = pygame.mouse.get_pos()


    for event in event_list:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    window.fill(Den)
    mouse = pygame.mouse.get_pos() 
    if event.type == pygame.MOUSEBUTTONDOWN:
        if 50 <= mouse[0] <= 350 and 150 <= mouse[1] <= 250:
            os.startfile(r'THONGBAO.exe')
            sleep(1)
            pygame.quit()
            sys.exit()
    hamchu("CRUSH CÓ THÍCH BẠN KHÔNG ", Trang, 20,20, 60)
    pygame.draw.rect(window, Trang, (50, 150, 300, 100))
    pygame.draw.rect(window, Trang, (570, 150, 300, 100))

    if 50 <= mouse_x <= 350 and 150 <= mouse_y <= 250: 
        hamchu("KHÔNG ", Den, 110, 170, 60)
    else:
        hamchu("CÓ", Den, 150, 170, 60)
    hamchu("KHÔNG", Den, 630, 170, 60)

    pygame.display.update()
pygame.quit()
exit()
# # Code Chương trình 2

# # import pygame, sys
# # from pygame.locals import *
# # from time import strftime

# # pygame.init()
# # clock = pygame.time.Clock()
# window = pygame.display.set_mode((900, 80))
# # pygame.display.set_caption('T_T')
# # Trang=(255,255,255)
# # Den=(0,0,0)
# # Xanhla=(0,255,0)
# # Do=(255,0,0)
# # Xanhduong=(0,178,191)


# # def hamchu(chu, mau, ngang, doc, cochu):
# #     font = pygame.font.SysFont('Calibri', cochu)
# #     chu_ra = font.render(chu, True, mau)
# #     window.blit(chu_ra, [ngang, doc])

# # text=""
# # input_active = True

# # while True:
# #     pygame.display.flip()
# #     clock.tick(15)
# #     event_list = pygame.event.get()


# #     for event in event_list:
# #         if event.type == QUIT:
# #             pygame.quit()
# #             sys.exit()
# #     window.fill(Den)
# #     hamchu("ĐÓ LÀ LỰA CHỌN THÔNG MINH T_T", Trang, 10,10,60)
 
# #     pygame.display.update()
# pygame.quit()
# # exit()