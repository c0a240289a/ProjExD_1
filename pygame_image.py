import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")#背景画像のsurface
    bg_img2 = pg.transform.flip(bg_img,True,False)
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img,True,False)
    kk_rct = kk_img.get_rect()#こうかとん画像のRect
    kk_rct.center = 300,200#こうかとん画像の中心座標
    
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()
        # if key_lst[pg.K_UP]:#上キーが押されたら上に移動
        #     kk_rct.move_ip((0,-1))
        # if key_lst[pg.K_DOWN]:
        #     kk_rct.move_ip((0,1))
        # if key_lst[pg.K_RIGHT]:
        #     kk_rct.move_ip((1,0))
        # else:
        #     kk_rct.move_ip((-1,0))
        # if key_lst[pg.K_LEFT]:
        #     kk_rct.move_ip((-1,0))
            
        move_x = 0
        move_y = 0
        if key_lst[pg.K_UP]:#上キーが押されたら上に移動
            move_y = -1
        if key_lst[pg.K_DOWN]:
            move_y = 1
        if key_lst[pg.K_RIGHT]:
            move_x = 1
        else:
            move_x = -1
        if key_lst[pg.K_LEFT]:
            move_x = -2
        kk_rct.move_ip((move_x,move_y))
        
        
        

        x = tmr%3200
        
        screen.blit(bg_img, [-x, 0])#1枚目
        screen.blit(bg_img2,[-x+1600,0])#2枚目
        screen.blit(bg_img,[-x+3200,0])
        screen.blit(kk_img,kk_rct)
        
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()