
import pygame
import random
import time
pygame.init()
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
(width,height) = (1600 , 900)
screen = pygame.display.set_mode((width, height))


def Cards():
    Cards = {'Rock':[10,25], 'Paper': [5,5], 'Scissors': [30, 5], 'Shovel': [20,20], 'Gun': [100,0], 'Stick': [15,15], 'Pipe': [30,30], 'Fist':[25,25]}
    return Cards
    
def aiDeal():
    numCards = 5
    aiCards = []
    for i in range(numCards):
        pick = random.choice(list(Cards()))
        aiCards.append(pick)

    return aiCards

def playerDeal():
    numCards = 5
    pCards = []
    for i in range(numCards):
        pick = random.choice(list(Cards()))
        pCards.append(pick)

    return pCards

def aiSelection(aiCards):
    selection = random.choice(aiCards)
    return selection

def drawScreen():
    screen.fill(black)
    pygame.display.set_caption('Rock, Paper, Scissors, OTHER!')

def drawCards(pCards):
    cWidth = 100
    cHeight = 200
    ch = 600
    card1 = pygame.Rect(400,ch,cWidth,cHeight)
    card2 = pygame.Rect(575,ch,cWidth,cHeight)
    card3 = pygame.Rect(750,ch,cWidth,cHeight)
    card4 = pygame.Rect(925,ch,cWidth,cHeight)
    card5 = pygame.Rect(1100,ch,cWidth,cHeight)
    if len(pCards) >= 1:
        pygame.draw.rect(screen, red, card1)
    if len(pCards) >= 2:
        pygame.draw.rect(screen, red, card2)
    if len(pCards) >= 3:
        pygame.draw.rect(screen, red, card3)
    if len(pCards) >= 4:
        pygame.draw.rect(screen, red, card4)
    if len(pCards) >= 5:
        pygame.draw.rect(screen, red, card5)
    allcards = [card1,card2,card3,card4,card5]
    return allcards

def mouseHover(allCards):
 
    (c1,c2,c3,c4,c5) = (allCards[0],allCards[1],allCards[2],allCards[3],allCards[4])
    if c1.collidepoint(mx,my):
        pygame.draw.rect(screen, green, c1)
        return c1
    if c2.collidepoint(mx,my):
        pygame.draw.rect(screen, green, c2)
        return c2
    if c3.collidepoint(mx,my):
        pygame.draw.rect(screen, green, c3)
        return c3
    if c4.collidepoint(mx,my):
        pygame.draw.rect(screen, green, c4)
        return c4
    if c5.collidepoint(mx,my):
        pygame.draw.rect(screen, green, c5)
        return c5

def playerPick(allCards, pCards):
    (c1,c2,c3,c4,c5) = (allCards[0],allCards[1],allCards[2],allCards[3],allCards[4])
    cardHover = mouseHover(allCards)
    if cardHover == c1 and pygame.mouse.get_pressed()[0]:
        return pCards[0]
    if cardHover == c2 and pygame.mouse.get_pressed()[0]:
        return pCards[1]
    if cardHover == c3 and pygame.mouse.get_pressed()[0]:
        return pCards[2]
    if cardHover == c4 and pygame.mouse.get_pressed()[0]:
        return pCards[3]
    if cardHover == c5 and pygame.mouse.get_pressed()[0]:
        return pCards[4]

def pickedCard(pPick, allCards):
        p = []
        iScale = 80
        rock = pygame.image.load('rock.jpg')
        paper = pygame.image.load('paper.jpg')
        scissors = pygame.image.load('scissors.png')
        shovel = pygame.image.load('shovel.png')
        gun = pygame.image.load('gun.png')
        stick = pygame.image.load('stick.png')
        pipe = pygame.image.load('pipe.jpg')
        fist = pygame.image.load('fist.png')
        picDic = {'Rock': pygame.transform.scale(rock, (iScale, iScale) ), 'Paper':pygame.transform.scale(paper, (iScale,iScale)), 'Scissors':pygame.transform.scale(scissors, (iScale,iScale)), 
              'Shovel': pygame.transform.scale(shovel, (iScale,iScale)), 'Gun':pygame.transform.scale(gun, (iScale,iScale)), 'Stick':pygame.transform.scale(stick, (iScale,iScale)), 
              'Pipe':pygame.transform.scale(pipe, (iScale,iScale)), 'Fist':pygame.transform.scale(fist, (iScale,iScale))}
        p.insert(0,pPick)

        startPoint = (1000,250,100,200)

       
        newRect = pygame.Rect(startPoint)
        pygame.draw.rect(screen, red,newRect)
           
           
        if p[0] != None:
            screen.blit(picDic[p[0]], (1000 +10,250+25))
def drawAiCard():
    startPoint = (500,250,100,200)
    newRect = pygame.Rect(startPoint)
    pygame.draw.rect(screen, blue,newRect)
def aiPicked(aiPick):
        iScale = 80
        rock = pygame.image.load('rock.jpg')
        paper = pygame.image.load('paper.jpg')
        scissors = pygame.image.load('scissors.png')
        shovel = pygame.image.load('shovel.png')
        gun = pygame.image.load('gun.png')
        stick = pygame.image.load('stick.png')
        pipe = pygame.image.load('pipe.jpg')
        fist = pygame.image.load('fist.png')
        picDic = {'Rock': pygame.transform.scale(rock, (iScale, iScale) ), 'Paper':pygame.transform.scale(paper, (iScale,iScale)), 'Scissors':pygame.transform.scale(scissors, (iScale,iScale)), 
              'Shovel': pygame.transform.scale(shovel, (iScale,iScale)), 'Gun':pygame.transform.scale(gun, (iScale,iScale)), 'Stick':pygame.transform.scale(stick, (iScale,iScale)), 
              'Pipe':pygame.transform.scale(pipe, (iScale,iScale)), 'Fist':pygame.transform.scale(fist, (iScale,iScale))}

        if aiPick != None:
            screen.blit(picDic[aiPick], (500 +10,250+25))


def removeCard(pCards, pPick,allCards, times ):
        index = pCards.index(pPick)
        end = len(allCards)- times
        allCards.pop(end)
        allCards.append(pygame.Rect(0,0,0,0))
        pCards.pop(index)
        return pCards
    
def showMove(aiPick, pPick):
    font = pygame.font.SysFont('Arial', 36) 
    AIpick_surface = font.render(aiPick, True, red)
    PlayerPick_surface = font.render(pPick, True, green)

    screen.blit(AIpick_surface, (350 - AIpick_surface.get_width()//2, 300 - AIpick_surface.get_height() // 2))
    screen.blit(PlayerPick_surface, (1300- PlayerPick_surface.get_width()//2, 300 - PlayerPick_surface.get_height() // 2))

    Card = Cards()
    pai = ''
    pp = ''
    nai = ''
    np = ''
    aiPlay = Card[aiPick]
    pPlay = Card[pPick]
    ai = aiPlay[0] - pPlay[1]
    p = pPlay[0] - aiPlay[1]
    font = pygame.font.SysFont('Arial', 36) 
    aiPos_surface = font.render(pai, True, green)
    aiNeg_surface = font.render(nai, True, red)
    pPos_surface = font.render(pp, True, green)
    pNeg_surface = font.render(np, True, red)
    Card = Cards()
   

    if ai < 0:
        ai = ai * (-1)
        pai = str(ai)
        screen.blit(aiPos_surface, (300 - aiPos_surface.get_width()//2, 300 - aiPos_surface.get_height() // 2))
        print(pai)
    if ai > 0:
        nai = str(ai)
        screen.blit(aiNeg_surface, (300 - aiNeg_surface.get_width()//2, 300 - aiNeg_surface.get_height() // 2))
        print(nai)
    if p < 0:
        p = p * (-1)
        pp = str(p)
        screen.blit(pPos_surface, (1200 , 300 ))
        
    if p > 0:
        np = str(p)
        screen.blit(pNeg_surface, (1200 , 300 ))


    pygame.display.update()


def plusMinus(aiPick, pPick):
    Card = Cards()
    pai = ''
    pp = ''
    nai = ''
    np = ''
    aiPlay = Card[aiPick]
    pPlay = Card[pPick]
    ai = aiPlay[0] - pPlay[1]
    p = pPlay[0] - aiPlay[1]
    font = pygame.font.SysFont('Arial', 36) 
    aiPos_surface = font.render(pai, True, green)
    aiNeg_surface = font.render(nai, True, red)
    pPos_surface = font.render(pp, True, green)
    pNeg_surface = font.render(np, True, red)
    Card = Cards()
   

    if ai < 0:
        ai = ai * (-1)
        pai = str(ai)
        screen.blit(aiPos_surface, (300 - aiPos_surface.get_width()//2, 300 - aiPos_surface.get_height() // 2))
        print(pai)
    if ai > 0:
        nai = str(ai)
        screen.blit(aiNeg_surface, (300 - aiNeg_surface.get_width()//2, 300 - aiNeg_surface.get_height() // 2))
        print(nai)
    if p < 0:
        p = p * (-1)
        pp = str(p)
        screen.blit(pPos_surface, (1200 , 300 ))
        
    if p > 0:
        np = str(p)
        screen.blit(pNeg_surface, (1200 , 300 ))
    
       
def playerHealth(pPick, aiPick, pHealth):

    c =  Cards()
    aiCard = c[aiPick]
    if pPick != None:
        pCard = c[pPick]
        
        pHealth = pCard[1] - aiCard[0]
        
        return pHealth

def aiHealthy(pPick, aiPick, aiHealth):

    c =  Cards()
    aiCard = c[aiPick]
    if pPick != None:
        pCard = c[pPick]
        
        aiHealth = aiCard[1] - pCard[0]
        
        return aiHealth

def trackHealth(aiHealth, pHealth):
    playerHealth = str(pHealth)
    AIHealth = str(aiHealth)
    font = pygame.font.SysFont('Arial', 36)
    aiHealth_surface = font.render(AIHealth, True, white)
    pHealth_surface = font.render(playerHealth, True, white)

    ai_surface = font.render('Enemy Health: ', True, white)
    player_surface = font.render('Player Health: ', True, white)

    pHealthRect = pygame.Rect(1300, 500, pHealth*2, 20)
    pygame.draw.rect(screen, green, pHealthRect)
    aiHealthRect = pygame.Rect(150, 500, aiHealth*2, 20)
    pygame.draw.rect(screen, red, aiHealthRect)

    screen.blit(aiHealth_surface, (350- aiHealth_surface.get_width()//2, 450 - aiHealth_surface.get_height() // 2))
    screen.blit(pHealth_surface, (1500- pHealth_surface.get_width()//2, 450 - pHealth_surface.get_height() // 2))

    screen.blit(ai_surface, (200- ai_surface.get_width()//2, 450 - ai_surface.get_height() // 2))
    screen.blit(player_surface, (1350- player_surface.get_width()//2, 450 - player_surface.get_height() // 2))

def newHand(pCards):
    if len(pCards) <=0:
        pCards = playerDeal()
        
        return pCards

def drawPics(pCards, allCards, test):
    place = None
    iScale = 80
    test = pCards.copy()
    empty = ['','','','','']
    rock = pygame.image.load('rock.jpg')
    paper = pygame.image.load('paper.jpg')
    scissors = pygame.image.load('scissors.png')
    shovel = pygame.image.load('shovel.png')
    gun = pygame.image.load('gun.png')
    stick = pygame.image.load('stick.png')
    pipe = pygame.image.load('pipe.jpg')
    fist = pygame.image.load('fist.png')
    picDic = {'Rock': pygame.transform.scale(rock, (iScale, iScale) ), 'Paper':pygame.transform.scale(paper, (iScale,iScale)), 'Scissors':pygame.transform.scale(scissors, (iScale,iScale)), 
              'Shovel': pygame.transform.scale(shovel, (iScale,iScale)), 'Gun':pygame.transform.scale(gun, (iScale,iScale)), 'Stick':pygame.transform.scale(stick, (iScale,iScale)), 
              'Pipe':pygame.transform.scale(pipe, (iScale,iScale)), 'Fist':pygame.transform.scale(fist, (iScale,iScale))}

    for i in pCards:
        find = test.index(i)
        place = allCards[find]
        screen.blit(picDic[i], (place[0]+10,place[1]+25))
        test.remove(i)
        test.insert(find, '')



#Old Way of drawing pics
'''
    for i in pCards:
        
        if i == 'Rock':
            
            find = test.index(i)
            place = allCards[find]
            screen.blit(rockSmall, (place[0]+10,place[1]+25))
            test.remove(i)
            test.insert(find, '')
            
        if i == 'Paper':
            
            find = test.index(i)
            place = allCards[find]
            screen.blit(paperSmall, (place[0]+10,place[1]+25))
            test.remove(i)
            test.insert(find, '')
        if i == 'Scissors':
            
            find = test.index(i)
            place = allCards[find]
            screen.blit(scissorsSmall, (place[0]+10,place[1]+25))
            test.remove(i)
            test.insert(find, '')
        if i == 'Shovel':
            
            find = test.index(i)
            place = allCards[find]
            screen.blit(shovelSmall, (place[0]+10,place[1]+25))
            test.remove(i)
            test.insert(find, '')
        if i == 'Gun':
            
            find = test.index(i)
            place = allCards[find]
            screen.blit(gunSmall, (place[0]+10,place[1]+25))
            test.remove(i)
            test.insert(find, '')
        if i == 'Stick':
            
            find = test.index(i)
            place = allCards[find]
            screen.blit(stickSmall, (place[0]+10,place[1]+25))
            test.remove(i)
            test.insert(find, '')
        if i == 'Pipe':
            
            find = test.index(i)
            place = allCards[find]
            screen.blit(pipeSmall, (place[0]+10,place[1]+25))
            test.remove(i)
            test.insert(find, '')
        if i == 'Fist':
            find = test.index(i)
            place = allCards[find]
            screen.blit(fistSmall, (place[0]+10,place[1]+25))
            test.remove(i)
            test.insert(find, '')
   
'''


  
clock = pygame.time.Clock()
square = pygame.Rect(0,0,100,200)
times = 0
pHealth = 100
aiHealth = 100
running = True
pCards = playerDeal()
test = pCards.copy()
aiCards = aiDeal()
print('Player: ',pCards)
print("AI: ",aiCards)
allCards = drawCards(pCards)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        (mx,my) = pygame.mouse.get_pos()
    clock.tick(30)
    drawScreen() 
    
       
    
    drawCards(pCards)
    mouseHover(allCards)
    pPick = playerPick(allCards, pCards)
    pickedCard(pPick, allCards)
    drawAiCard()
    
       
        
        
        
        
    if pPick != None:
            aiPick = aiSelection(aiCards)
            aiPicked(aiPick)

            if pHealth >= 100 and playerHealth(pPick,aiPick, pHealth)> 0:
                None
            else:
                pHealth += playerHealth(pPick,aiPick, pHealth)
            if aiHealth >= 100 and aiHealthy(pPick,aiPick, pHealth)> 0:
                None
            else:
                aiHealth += aiHealthy(pPick,aiPick, aiHealth)
            if pHealth > 100:
                pHealth = 100
            if aiHealth > 100:
                aiHealth = 100
            times +=1
            trackHealth(aiHealth, pHealth)
            plusMinus(aiPick, pPick)
            showMove(aiPick, pPick)
            
            
            
            if len(pCards) ==0:
                pCards = newHand(pCards)
                allCards = drawCards(pCards)
                times = 0
                plusMinus(aiPick, pPick)
                pygame.display.update()
            
            drawPics(pCards, allCards, test)
            removeCard(pCards, pPick, allCards, times)
            
            pygame.display.update()
            time.sleep(1)
        #   continue
    
    if aiHealth <= 0 and pHealth > 0:
        print('You Win!!')
        pCards = playerDeal()
        allCards = drawCards(pCards)
        test = pCards.copy()
        times = 0
        pHealth = 100
        aiHealth = 100
        pygame.display.update()
        time.sleep(1)
        continue
    if pHealth <= 0 and aiHealth > 0:
        print('You Lose!')
        pCards = playerDeal()
        allCards = drawCards(pCards)
        test = pCards.copy()
        times = 0
        pHealth = 100
        aiHealth = 100
        pygame.display.update()
        time.sleep(1)
        continue

    if pHealth <=0 and aiHealth <= 0:
        print("DRAW!!!")
        pCards = playerDeal()
        allCards = drawCards(pCards)
        test = pCards.copy()
        times = 0
        pHealth = 100
        aiHealth = 100
        pygame.display.update()
        time.sleep(1)
        continue
    
    trackHealth(aiHealth, pHealth)
    drawPics(pCards, allCards, test)
  #  moveCard(pPick, allCards)
    pygame.display.update()
