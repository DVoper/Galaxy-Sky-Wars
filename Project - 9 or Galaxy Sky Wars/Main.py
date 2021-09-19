import pygame
import sys
import random
import time
import math
from pygame import mixer
#C:\Users\Krithik\Desktop\IDLE\Pygame\Project - 9 or Galaxy Sky Wars

pygame.init()

mixer.music.load('background.wav')
mixer.music.play(-1)

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Galaxy Sky Wars')

bg = pygame.image.load('Background.png').convert_alpha()

playerImg = pygame.image.load('player.png').convert_alpha()
pr = playerImg.get_rect(topleft = (370,480))

m_killed = 0

bulletImg = pygame.image.load('bullet.png').convert_alpha()
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 7
bullet_state = "ready"

pbulletImg = pygame.image.load('bullet.png').convert_alpha()
pbulletX = 0
pbulletY = 480
pbulletX_change = 0
pbulletY_change = 5
pbullet_state = "ready"

with open('Level.txt','r') as f:
    text = f.read()
    level = int(text)
    
m_enemies = level

b_spd = 1

m_enemyImg = []
mer = []
m_spd = []
enemy_bulletImg1 = []
enemy_bulletImg = []
enemy_bulletX = []
enemy_bulletY = []
enemy_bulletX_change = []
enemy_bulletY_change = []
enemy_bullet_state = []
for i in range(m_enemies):
    m_enemyImg.append(pygame.image.load('mini enemy2.png').convert_alpha())
    #m_enemyImg.append(pygame.transform.flip(m_enemyImg[i], False, True))
    mer.append(m_enemyImg[i].get_rect(topleft = (random.randint(5,763),190)))
    m_spd.append(-2)
    enemy_bulletImg1.append(pygame.image.load('bullet.png').convert_alpha())
    enemy_bulletImg.append(pygame.transform.flip(enemy_bulletImg1[i], False, True))
    enemy_bulletX.append(0)
    enemy_bulletY.append(mer[i].y)
    enemy_bulletX_change.append(0)
    enemy_bulletY_change.append(7)
    enemy_bullet_state.append("ready")
    
##m_enemyImg = pygame.image.load('mini enemy.png').convert_alpha()
##m_enemyImg = pygame.transform.flip(m_enemyImg, False, True)
##mer = m_enemyImg.get_rect(topleft = (random.randint(5,763),190))
##
##enemy_bulletImg1 = pygame.image.load('bullet.png').convert_alpha()
##enemy_bulletImg = pygame.transform.flip(enemy_bulletImg1, False, True)
##enemy_bulletX = 0
##enemy_bulletY = mer.y
##enemy_bulletX_change = 0
##enemy_bulletY_change = 7
##enemy_bullet_state = "ready"

enemyImg = pygame.image.load('enemy.png').convert_alpha()
enemy_rect = enemyImg.get_rect(center = (400,190))

clock = pygame.time.Clock()

bbullet1 = pygame.image.load('bullet.png').convert_alpha()
bbullet1 = pygame.transform.flip(bbullet1, False, True)
bbullet1X  = 0
bbullet1Y = enemy_rect.y + 100
bbullet1X_change = 0
bbullet1Y_change = 7
bbullet1_state = "ready"

bbullet2 = pygame.image.load('bullet2.png').convert_alpha()
bbullet2X  = 0
bbullet2Y = enemy_rect.y + 100
bbullet2X_change = 0
bbullet2Y_change = 7
bbullet2_state = "ready"

bbullet3 = pygame.image.load('bullet3.png').convert_alpha()
bbullet3X  = 0
bbullet3Y = enemy_rect.y + 100
bbullet3X_change = 0
bbullet3Y_change = 7
bbullet3_state = "ready"

###12 Hearts
##heart1 = pygame.image.load('heart.png').convert_alpha()
##heart2 = pygame.transform.flip(heart1,True,False)
##heart3 = pygame.image.load('heart.png').convert_alpha()
##heart4 = pygame.transform.flip(heart1,True,False)
##heart5 = pygame.image.load('heart.png').convert_alpha()
##heart6 = pygame.transform.flip(heart1,True,False)
##heart7 = pygame.image.load('heart.png').convert_alpha()
##heart8 = pygame.transform.flip(heart1,True,False)
##heart9 = pygame.image.load('heart.png').convert_alpha()
##heart10 = pygame.transform.flip(heart1,True,False)
heart1 = pygame.image.load('heart.png').convert_alpha()
heart2 = pygame.transform.flip(heart1,True,False)
heart3 = pygame.image.load('heart.png').convert_alpha()
heart4 = pygame.transform.flip(heart1,True,False)
heart5 = pygame.image.load('heart.png').convert_alpha()
heart6 = pygame.transform.flip(heart1,True,False)
heart7 = pygame.image.load('heart.png').convert_alpha()
heart8 = pygame.transform.flip(heart1,True,False)
heart9 = pygame.image.load('heart.png').convert_alpha()
heart10 = pygame.transform.flip(heart1,True,False)
hearts = [heart1,heart2,heart3,heart4,heart5,heart6,heart7,heart8,heart9,heart10]
heart_rl = []
heart_num = 10
for i in range(heart_num):    
    heart_rl.append(hearts[i].get_rect(topleft = (i*16,20)))
##print(heart_rl)
#=============================================================================================================

score = 0

boss_shoot = 0

explosion_music = pygame.mixer.Sound('explosion.wav')
bullet_music = pygame.mixer.Sound('laser.wav')

#b_move = False

font = pygame.font.Font('1.ttf',132)

s_text = font.render("Level "+str(level),True,(255,255,255))
s_text_rect = s_text.get_rect(center = (400,300))

bw_text = font.render("Warning BOSS",True,(255, 0, 20))
bw_text_rect = bw_text.get_rect(center = (400,300))

currentTime2 = time.time()

gm_ovr_font = pygame.font.Font('1.ttf',132)

gm_ovr_txt = gm_ovr_font.render('Game Over',True,(255,255,255))
gm_ovr_rect = gm_ovr_txt.get_rect(center = (400,266))

gg_font = pygame.font.Font('1.ttf',75)
gg_text = gg_font.render('Press SPACE to restart',True,(255,255,255))
gg_rect = gg_text.get_rect(center = (400,500))


def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x+16,y))

def player_fire_bullet(x,y):
    global pbullet_state
    pbullet_state = "fire"
    screen.blit(pbulletImg,(x+16,y))

def boss_fire_bullet1(x,y):
    global bbullet1_state
    bbullet1_state = "fire"
    screen.blit(bbullet1,(x+16,y))

def boss_fire_bullet2(x,y):
    global bbullet2_state
    bbullet2_state = "fire"
    screen.blit(bbullet2,(x+16,y))

def boss_fire_bullet3(x,y):
    global bbullet3_state
    bbullet3_state = "fire"
    screen.blit(bbullet3,(x+16,y))
    
def enemy_fire_bullet(x,y,i):
    global enemy_bullet_state
    enemy_bullet_state[i] = "fire"
    screen.blit(enemy_bulletImg[i],(x[i]+15,y[i]+50))

def isCollision(enemy,bulletX,bulletY,i):
    distance = math.sqrt((math.pow(enemy[i].x-bulletX,2)) + (math.pow(enemy[i].y-bulletY,2)))
    if distance < 27:#64 = 27,32 = 14,128 = 54
        return True
    else:
        return False

def isCollision2(enemy,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemy.x-bulletX,2)) + (math.pow(enemy.y-bulletY,2)))
    if distance < 80:#64 = 27,32 = 14,128 = 54
        return True
    else:
        return False
    
def enemy_isCollision(playerX,playerY,enemy_bulletX,enemy_bulletY,i):
    distance = math.sqrt((math.pow(playerX-enemy_bulletX[i],2)) + (math.pow(playerY-enemy_bulletY[i],2)))
    if distance < 27:#64 = 27,32 = 14,128 = 54
        return True
    else:
        return False

def boss_isCollision1(playerX,playerY,bulletX,bulletY):
    distance = math.sqrt((math.pow(playerX-bulletX,2)) + (math.pow(playerY-bulletY,2)))
    if distance < 27:#64 = 27,32 = 14,128 = 54
        return True
    else:
        return False

def boss_isCollision2(playerX,playerY,bulletX,bulletY):
    distance = math.sqrt((math.pow(playerX-bulletX,2)) + (math.pow(playerY-bulletY,2)))
    if distance < 27:#64 = 27,32 = 14,128 = 54
        return True
    else:
        return False

def boss_isCollision3(playerX,playerY,bulletX,bulletY):
    distance = math.sqrt((math.pow(playerX-bulletX,2)) + (math.pow(playerY-bulletY,2)))
    if distance < 27:#64 = 27,32 = 14,128 = 54
        return True
    else:
        return False
    
currentTime = time.time()

run = True

stage = "START"
currentTime3 = time.time()

inc2 = 0

x = 0

hb_val = 74

while run:
    #Vars and BG
    screen.blit(bg,(0,0))
    if stage != "INCREMENT LEVEL":
        for i in range(heart_num):
            screen.blit(hearts[i],heart_rl[i])
    if heart_num <= 0:
        stage = "GAME OVER"
    #====================================================
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if stage == "GAME":
        if m_killed == level:
            stage = "BOSS"
            currentTime3 = time.time()
        keys = pygame.key.get_pressed()
        shoottime = (currentTime2 - time.time()) * -1
        if int(6-shoottime) >= 1:
##            print(int(6-shoottime))
            if int(6-shoottime) == 1:
                for i in range(m_enemies):
                    if enemy_bullet_state[i] == "ready":
                        enemy_bulletX[i] = mer[i].x
                        enemy_fire_bullet(enemy_bulletX,enemy_bulletY,i)
                        currentTime2 = time.time()
    

        if keys[pygame.K_RIGHT]:
            pr.x += 2
        if keys[pygame.K_LEFT]:
            pr.x -= 2
            
        if keys[pygame.K_SPACE]:
            if bullet_state == "ready":
                bulletX = pr.x
                fire_bullet(bulletX,bulletY)
                bullet_music.play()

        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"

        for i in range(m_enemies):
            if enemy_bulletY[i] >= 800:
                enemy_bulletY[i] = mer[i].y
                enemy_bullet_state[i] = "ready"
            
        if bullet_state == "fire":
            fire_bullet(bulletX,bulletY)
            bulletY -= bulletY_change

        for i in range(m_enemies):
            if enemy_bullet_state[i] == "fire":
                enemy_fire_bullet(enemy_bulletX,enemy_bulletY,i)
                enemy_bulletY[i] += enemy_bulletY_change[i]

        if x == m_enemies:
            m_killed = 0
            x = 0
            
        while x < m_enemies:
            if mer[x].x < -10:
                m_killed += 1
            x += 1
            
        for i in range(m_enemies):
            collision = isCollision(mer,bulletX,bulletY,i)
            if collision:
                bulletY = 480
                bullet_state = "ready"
                score += 1
                mer[i].x = -100000000
                mer[i].y = -100000000
                m_spd[i] = 0
                explosion_music.play()
##                m_enemyImg.pop(i)
##                mer.pop(i)
##                m_spd.pop(i)
##                enemy_bulletImg1.pop(i)
##                enemy_bulletImg.pop(i)
##                enemy_bulletX.pop(i)
##                enemy_bulletY.pop(i)
##                enemy_bulletX_change.pop(i)
##                enemy_bulletY_change.pop(i)
##                enemy_bullet_state.pop(i)
##                try:
##                    m_enemies -= 1
##                except:
##                    print('error')
##                mer[i] = m_enemyImg[i].get_rect(topleft = (random.randint(5,763),190))
                i -= 1

        for i in range(m_enemies):
            enemy_collision = enemy_isCollision(pr.x,pr.y,enemy_bulletX,enemy_bulletY,i)
            if enemy_collision:
                enemy_bulletY[i] = mer[i].y
                enemy_bullet_state[i] = "ready"
                heart_num -= 1
                explosion_music.play()
    ##            pr = playerImg.get_rect(topleft = (370,480))
            
        if pr.x <= 5:
            pr.x = 5

        for i in range(m_enemies):
            if mer[i].x <= 0:
                m_spd[i] = 2
            
            if mer[i].x >= 755:
                m_spd[i] = -2
                
            mer[i].x += m_spd[i]
            
        if pr.x >= 731:
            pr.x = 731

        for i in range(m_enemies):
            screen.blit(m_enemyImg[i],mer[i])
        screen.blit(playerImg,pr)
    elif stage == "START":
        screen.blit(s_text,s_text_rect)
        timenow = (currentTime - time.time()) * -1
        if int(6-timenow) >= 1:
            if int(6-timenow) == 1:
                stage = "GAME"
                currentTime2 = time.time()

    elif stage == "BOSS":
        timenow3 = (currentTime3 - time.time()) * -1
        if int(6-timenow3) >= 1:
            screen.blit(bw_text,bw_text_rect)
            bossTime = time.time()
        else:
            keys = pygame.key.get_pressed()
            if hb_val != 74:
                hb_val += 0.005
            
            if keys[pygame.K_RIGHT]:
                pr.x += 2
                
            if keys[pygame.K_LEFT]:
                pr.x -= 2

            if keys[pygame.K_SPACE]:
                if pbullet_state == "ready":
                    pbulletX = pr.x
                    player_fire_bullet(pbulletX,pbulletY)
                    bullet_music.play()

            bhoot_time = (bossTime - time.time()) * -1
            if int(6-bhoot_time) >= 1:
                if int(6-bhoot_time) == 3:
                    if bbullet1_state == "ready":
                        bbullet1X = enemy_rect.x + 35
                        boss_fire_bullet1(bbullet1X,bbullet1Y + 100)
                    if bbullet2_state == "ready":
                        bbullet2X = enemy_rect.x + 35
                        boss_fire_bullet2(bbullet2X,bbullet2Y + 100)

                    if bbullet3_state == "ready":
                        bbullet3X = enemy_rect.x + 35
                        boss_fire_bullet3(bbullet3X,bbullet3Y + 100)
                    bossTime = time.time()

            if bbullet1_state == "fire":
                boss_fire_bullet1(bbullet1X,bbullet1Y + 100)
                bbullet1Y += bbullet1Y_change
                
            if bbullet2_state == "fire":
                inc2 += 1.5
                boss_fire_bullet2(bbullet2X + inc2,bbullet2Y + 100)
                bbullet2Y += bbullet2Y_change

            if bbullet3_state == "fire":
                inc2 += 1.5
                boss_fire_bullet3(bbullet3X - inc2,bbullet3Y + 100)
                bbullet3Y += bbullet3Y_change

            if pbullet_state == "fire":
                player_fire_bullet(pbulletX,pbulletY)
                pbulletY -= pbulletY_change

            if pbulletY <= 0:
                pbulletY = 480
                pbullet_state = "ready"
                
            
            if bbullet1Y >= 800:
                bbullet1Y = enemy_rect.y
                bbullet1_state = "ready"

            if bbullet2Y >= 800:
                inc2 = 0
                bbullet2Y = enemy_rect.y
                bbullet2_state = "ready"

            if bbullet3Y >= 800:
                inc2 = 0
                bbullet3Y = enemy_rect.y
                bbullet3_state = "ready"
                
            if pr.x >= 731:
                pr.x = 731
                
            if pr.x <= 0:
                pr.x = 0

            pcollision = isCollision2(enemy_rect,pbulletX,pbulletY)
            if pcollision:
                pbulletY = 480
                pbullet_state = "ready"
                hb_val -= 7.4
                explosion_music.play()

            if hb_val <= 0:
                stage = "INCREMENT LEVEL"
                
            collision1 = boss_isCollision1(pr.x,pr.y,bbullet1X,bbullet1Y)
            
            if collision1:
                bbullet1Y = enemy_rect.y
                bbullet1_state = "ready"
                bbullet2Y = enemy_rect.y
                bbullet2_state = "ready"
                bbullet3Y = enemy_rect.y
                bbullet3_state = "ready"
                boss_shoot += 1
                heart_num -= 2
                explosion_music.play()
                inc2 = 0
                bossTime = time.time()

            distance2 = math.sqrt((math.pow(pr.x-bbullet2X,2)) + (math.pow(pr.y-bbullet2Y,2)))
            #print(distance2)
            if 100 < distance2 < 150:
                bbullet1Y = enemy_rect.y
                bbullet1_state = "ready"
                bbullet2Y = enemy_rect.y
                bbullet2_state = "ready"
                bbullet3Y = enemy_rect.y
                bbullet3_state = "ready"
                boss_shoot += 1
                inc2 = 0
                heart_num -= 2
                explosion_music.play()
                bossTime = time.time()

            p_c = pr.center
            e_c = enemy_rect.center

            if p_c[0] < e_c[0]:
                enemy_rect.x -= b_spd

            if p_c[0] > e_c[0]:
                enemy_rect.x += b_spd
                
            pygame.draw.rect(screen,(0,0,0), pygame.Rect(enemy_rect.left - 11,enemy_rect.top - 50,150,40),  2)
            pygame.draw.rect(screen,(255,0,0),pygame.Rect(enemy_rect.left - 9,enemy_rect.top - 48,hb_val * 2,38))
                
            screen.blit(playerImg,pr)  
            screen.blit(enemyImg,enemy_rect)
##            screen.blit(heart1,(0,20))
##            screen.blit(heart2,(16,20))
    if stage == "GAME OVER":
        screen.blit(gm_ovr_txt,gm_ovr_rect)
        screen.blit(gg_text,gg_rect)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            bg = pygame.image.load('Background.png').convert_alpha()

            playerImg = pygame.image.load('player.png').convert_alpha()
            pr = playerImg.get_rect(topleft = (370,480))

            m_killed = 0

            bulletImg = pygame.image.load('bullet.png').convert_alpha()
            bulletX = 0
            bulletY = 480
            bulletX_change = 0
            bulletY_change = 7
            bullet_state = "ready"

            pbulletImg = pygame.image.load('bullet.png').convert_alpha()
            pbulletX = 0
            pbulletY = 480
            pbulletX_change = 0
            pbulletY_change = 5
            pbullet_state = "ready"

            with open('Level.txt','r') as f:
                text = f.read()
                level = int(text)
                
            m_enemies = level

            b_spd = 1

            m_enemyImg = []
            mer = []
            m_spd = []
            enemy_bulletImg1 = []
            enemy_bulletImg = []
            enemy_bulletX = []
            enemy_bulletY = []
            enemy_bulletX_change = []
            enemy_bulletY_change = []
            enemy_bullet_state = []
            for i in range(m_enemies):
                m_enemyImg.append(pygame.image.load('mini enemy2.png').convert_alpha())
                #m_enemyImg.append(pygame.transform.flip(m_enemyImg[i], False, True))
                mer.append(m_enemyImg[i].get_rect(topleft = (random.randint(5,763),190)))
                m_spd.append(-2)
                enemy_bulletImg1.append(pygame.image.load('bullet.png').convert_alpha())
                enemy_bulletImg.append(pygame.transform.flip(enemy_bulletImg1[i], False, True))
                enemy_bulletX.append(0)
                enemy_bulletY.append(mer[i].y)
                enemy_bulletX_change.append(0)
                enemy_bulletY_change.append(7)
                enemy_bullet_state.append("ready")
                
            ##m_enemyImg = pygame.image.load('mini enemy.png').convert_alpha()
            ##m_enemyImg = pygame.transform.flip(m_enemyImg, False, True)
            ##mer = m_enemyImg.get_rect(topleft = (random.randint(5,763),190))
            ##
            ##enemy_bulletImg1 = pygame.image.load('bullet.png').convert_alpha()
            ##enemy_bulletImg = pygame.transform.flip(enemy_bulletImg1, False, True)
            ##enemy_bulletX = 0
            ##enemy_bulletY = mer.y
            ##enemy_bulletX_change = 0
            ##enemy_bulletY_change = 7
            ##enemy_bullet_state = "ready"

            enemyImg = pygame.image.load('enemy.png').convert_alpha()
            enemy_rect = enemyImg.get_rect(center = (400,190))

            clock = pygame.time.Clock()

            bbullet1 = pygame.image.load('bullet.png').convert_alpha()
            bbullet1 = pygame.transform.flip(bbullet1, False, True)
            bbullet1X  = 0
            bbullet1Y = enemy_rect.y + 100
            bbullet1X_change = 0
            bbullet1Y_change = 7
            bbullet1_state = "ready"

            bbullet2 = pygame.image.load('bullet2.png').convert_alpha()
            bbullet2X  = 0
            bbullet2Y = enemy_rect.y + 100
            bbullet2X_change = 0
            bbullet2Y_change = 7
            bbullet2_state = "ready"

            bbullet3 = pygame.image.load('bullet3.png').convert_alpha()
            bbullet3X  = 0
            bbullet3Y = enemy_rect.y + 100
            bbullet3X_change = 0
            bbullet3Y_change = 7
            bbullet3_state = "ready"

            ###12 Hearts
            ##heart1 = pygame.image.load('heart.png').convert_alpha()
            ##heart2 = pygame.transform.flip(heart1,True,False)
            ##heart3 = pygame.image.load('heart.png').convert_alpha()
            ##heart4 = pygame.transform.flip(heart1,True,False)
            ##heart5 = pygame.image.load('heart.png').convert_alpha()
            ##heart6 = pygame.transform.flip(heart1,True,False)
            ##heart7 = pygame.image.load('heart.png').convert_alpha()
            ##heart8 = pygame.transform.flip(heart1,True,False)
            ##heart9 = pygame.image.load('heart.png').convert_alpha()
            ##heart10 = pygame.transform.flip(heart1,True,False)
            heart1 = pygame.image.load('heart.png').convert_alpha()
            heart2 = pygame.transform.flip(heart1,True,False)
            heart3 = pygame.image.load('heart.png').convert_alpha()
            heart4 = pygame.transform.flip(heart1,True,False)
            heart5 = pygame.image.load('heart.png').convert_alpha()
            heart6 = pygame.transform.flip(heart1,True,False)
            heart7 = pygame.image.load('heart.png').convert_alpha()
            heart8 = pygame.transform.flip(heart1,True,False)
            heart9 = pygame.image.load('heart.png').convert_alpha()
            heart10 = pygame.transform.flip(heart1,True,False)
            hearts = [heart1,heart2,heart3,heart4,heart5,heart6,heart7,heart8,heart9,heart10]
            heart_rl = []
            heart_num = 10
            for i in range(heart_num):    
                heart_rl.append(hearts[i].get_rect(topleft = (i*16,20)))
            ##print(heart_rl)
            #=============================================================================================================

            score = 0

            boss_shoot = 0

            explosion_music = pygame.mixer.Sound('explosion.wav')

            #b_move = False

            font = pygame.font.Font('1.ttf',132)

            s_text = font.render("Level "+str(level),True,(255,255,255))
            s_text_rect = s_text.get_rect(center = (400,300))

            bw_text = font.render("Warning BOSS",True,(255, 0, 20))
            bw_text_rect = bw_text.get_rect(center = (400,300))

            currentTime2 = time.time()

            gm_ovr_font = pygame.font.Font('1.ttf',132)

            gm_ovr_txt = gm_ovr_font.render('Game Over',True,(255,255,255))
            gm_ovr_rect = gm_ovr_txt.get_rect(center = (400,266))

            gg_font = pygame.font.Font('1.ttf',75)
            gg_text = gg_font.render('Press SPACE to restart',True,(255,255,255))
            gg_rect = gg_text.get_rect(center = (400,500))



            currentTime = time.time()

            run = True

            stage = "START"
            currentTime3 = time.time()

            inc2 = 0

            x = 0

            hb_val = 148


    if stage == "INCREMENT LEVEL":
        font1 = pygame.font.Font('1.ttf',100)
        
        text1 = font1.render(f'Boss {level} DEFEATED',True,'White')
        
        rect1 = text1.get_rect(center = (400,200))

        font2 = pygame.font.Font('1.ttf',100)
        text2 = font2.render('Press N to go to next level',True,'White')
        rect2 = text2.get_rect(center = (400,500))

        screen.blit(text1,rect1)
        screen.blit(text2,rect2)
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_n]:
            with open('Level.txt','w') as file:
                print(level + 1,file = file)
                stage = "REFRESH"
                
    if stage == "REFRESH":
            
        playerImg = pygame.image.load('player.png').convert_alpha()
        pr = playerImg.get_rect(topleft = (370,480))

        m_killed = 0

        bulletImg = pygame.image.load('bullet.png').convert_alpha()
        bulletX = 0
        bulletY = 480
        bulletX_change = 0
        bulletY_change = 7
        bullet_state = "ready"

        pbulletImg = pygame.image.load('bullet.png').convert_alpha()
        pbulletX = 0
        pbulletY = 480
        pbulletX_change = 0
        pbulletY_change = 5
        pbullet_state = "ready"

        with open('Level.txt','r') as f:
            text = f.read()
            level = int(text)
            
        m_enemies = level

        b_spd = 1

        m_enemyImg = []
        mer = []
        m_spd = []
        enemy_bulletImg1 = []
        enemy_bulletImg = []
        enemy_bulletX = []
        enemy_bulletY = []
        enemy_bulletX_change = []
        enemy_bulletY_change = []
        enemy_bullet_state = []
        for i in range(m_enemies):
            m_enemyImg.append(pygame.image.load('mini enemy2.png').convert_alpha())
            #m_enemyImg.append(pygame.transform.flip(m_enemyImg[i], False, True))
            mer.append(m_enemyImg[i].get_rect(topleft = (random.randint(5,763),190)))
            m_spd.append(-2)
            enemy_bulletImg1.append(pygame.image.load('bullet.png').convert_alpha())
            enemy_bulletImg.append(pygame.transform.flip(enemy_bulletImg1[i], False, True))
            enemy_bulletX.append(0)
            enemy_bulletY.append(mer[i].y)
            enemy_bulletX_change.append(0)
            enemy_bulletY_change.append(7)
            enemy_bullet_state.append("ready")
            
        ##m_enemyImg = pygame.image.load('mini enemy.png').convert_alpha()
        ##m_enemyImg = pygame.transform.flip(m_enemyImg, False, True)
        ##mer = m_enemyImg.get_rect(topleft = (random.randint(5,763),190))
        ##
        ##enemy_bulletImg1 = pygame.image.load('bullet.png').convert_alpha()
        ##enemy_bulletImg = pygame.transform.flip(enemy_bulletImg1, False, True)
        ##enemy_bulletX = 0
        ##enemy_bulletY = mer.y
        ##enemy_bulletX_change = 0
        ##enemy_bulletY_change = 7
        ##enemy_bullet_state = "ready"

        enemyImg = pygame.image.load('enemy.png').convert_alpha()
        enemy_rect = enemyImg.get_rect(center = (400,190))

        clock = pygame.time.Clock()

        bbullet1 = pygame.image.load('bullet.png').convert_alpha()
        bbullet1 = pygame.transform.flip(bbullet1, False, True)
        bbullet1X  = 0
        bbullet1Y = enemy_rect.y + 100
        bbullet1X_change = 0
        bbullet1Y_change = 7
        bbullet1_state = "ready"

        bbullet2 = pygame.image.load('bullet2.png').convert_alpha()
        bbullet2X  = 0
        bbullet2Y = enemy_rect.y + 100
        bbullet2X_change = 0
        bbullet2Y_change = 7
        bbullet2_state = "ready"

        bbullet3 = pygame.image.load('bullet3.png').convert_alpha()
        bbullet3X  = 0
        bbullet3Y = enemy_rect.y + 100
        bbullet3X_change = 0
        bbullet3Y_change = 7
        bbullet3_state = "ready"

        ###12 Hearts
        ##heart1 = pygame.image.load('heart.png').convert_alpha()
        ##heart2 = pygame.transform.flip(heart1,True,False)
        ##heart3 = pygame.image.load('heart.png').convert_alpha()
        ##heart4 = pygame.transform.flip(heart1,True,False)
        ##heart5 = pygame.image.load('heart.png').convert_alpha()
        ##heart6 = pygame.transform.flip(heart1,True,False)
        ##heart7 = pygame.image.load('heart.png').convert_alpha()
        ##heart8 = pygame.transform.flip(heart1,True,False)
        ##heart9 = pygame.image.load('heart.png').convert_alpha()
        ##heart10 = pygame.transform.flip(heart1,True,False)
        heart1 = pygame.image.load('heart.png').convert_alpha()
        heart2 = pygame.transform.flip(heart1,True,False)
        heart3 = pygame.image.load('heart.png').convert_alpha()
        heart4 = pygame.transform.flip(heart1,True,False)
        heart5 = pygame.image.load('heart.png').convert_alpha()
        heart6 = pygame.transform.flip(heart1,True,False)
        heart7 = pygame.image.load('heart.png').convert_alpha()
        heart8 = pygame.transform.flip(heart1,True,False)
        heart9 = pygame.image.load('heart.png').convert_alpha()
        heart10 = pygame.transform.flip(heart1,True,False)
        hearts = [heart1,heart2,heart3,heart4,heart5,heart6,heart7,heart8,heart9,heart10]
        heart_rl = []
        heart_num = 10
        for i in range(heart_num):    
            heart_rl.append(hearts[i].get_rect(topleft = (i*16,20)))
        ##print(heart_rl)
        #=============================================================================================================

        score = 0

        boss_shoot = 0

        explosion_music = pygame.mixer.Sound('explosion.wav')

        #b_move = False

        font = pygame.font.Font('1.ttf',132)

        s_text = font.render("Level "+str(level),True,(255,255,255))
        s_text_rect = s_text.get_rect(center = (400,300))

        bw_text = font.render("Warning BOSS",True,(255, 0, 20))
        bw_text_rect = bw_text.get_rect(center = (400,300))

        currentTime2 = time.time()

        gm_ovr_font = pygame.font.Font('1.ttf',132)

        gm_ovr_txt = gm_ovr_font.render('Game Over',True,(255,255,255))
        gm_ovr_rect = gm_ovr_txt.get_rect(center = (400,266))

        gg_font = pygame.font.Font('1.ttf',75)
        gg_text = gg_font.render('Press SPACE to restart',True,(255,255,255))
        gg_rect = gg_text.get_rect(center = (400,500))
        currentTime = time.time()

        run = True

        stage = "START"
        currentTime3 = time.time()

        inc2 = 0

        x = 0

        hb_val = 74


        
                                        
    clock.tick(100)
    pygame.display.update()
