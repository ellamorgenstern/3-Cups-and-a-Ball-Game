# “I hereby certify that this program is solely the result of my own work and
# is in compliance with the Academic Integrity policy of the course syllabus.”
import Draw
import math
import random
import time


#Set the trial’s increased speed and the trial’s number of swaps as global variables
TRIAL_SPEEDUP = 1.175
TRIAL_SWAP_INCREASE = 2


#Create the main function:
def main():
    
    #Create the canvas
    Draw.setCanvasSize(800,500)
    
    highScore = 0 #high score starts at 0
    firstTime = True #only show welcome when its first time playing
    
    #Loop game forever:
    while True:
        
        #“playRound” function takes the high score and returns the new score.
        score = playRound(highScore,firstTime)
        firstTime = False #dont show welcome again
        
        #If the new score is higher than it replaces the high score
        if score>highScore: highScore = score
        

#round loops the trial, if user wins trial gets harder, loses round restarts
def playRound(highScore,firstTime):
    
    #start first round w/ these scores, # of swaps, and speed
    score = 0
    swaps = 4
    speed = 5
    
    #Loop forever:
    while True:
        
        #start the cups trial 
        t = trial(score, highScore, swaps, speed,firstTime)
        firstTime = False
        
        #If user chose wrong, return score
        if t == False: return score
        
        #If the user chose the right cup than the game gets harder
        else:
            score+=1 #their score goes up one on screen
            speed = speed*TRIAL_SPEEDUP #speed increases
            swaps += TRIAL_SWAP_INCREASE #swap increases
            

#the cups swap a certain amt of times and then user guesses which cup ball is in
def trial(score, highScore, swaps, speed,firstTime):
    
    choice = "" #keeping choice an empty string for now 
    nums = [0,1,2] #Create list nums to shuffle cups
    ballPos = nums[1] #ballPos starts at middle cup
    
    #2D list of cups positions
    ogcups = [[150,150],[150+250,150],[150+500,150]]
    
    #copy of cups
    cups=[[ogcups[j][i] for i in range(len(ogcups[0]))]for j in range(len(ogcups))]
    
    #only show "Welcome!" the first time you play
    if firstTime == True: speak="welcome"
    else: speak="none"
    
    #when round starts, lift cup and show ball
    showBall(ogcups,ballPos,score,highScore,cups,speak,choice)
    
    #swap the cups 
    for i in range(swaps):
        
        #randomly pick which two cups to swap
        random.shuffle(nums)
        
        #animate the cups swap
        ballPos = animateSwap(nums[0],nums[1], speed, ogcups, score, highScore,ballPos,cups,nums,speak,choice)
        
        #Keep ball position at the correct cup
        if ballPos == nums[0]: ballPos = nums[1]
        elif ballPos==nums[1]: ballPos = nums[0]
        
    #show "choose A, B, or C”
    speak = "choose"
    drawBoard (ogcups, score, highScore, ballPos,cups,speak,choice)
    
    #Set ans automatically to false
    ans = False
    
    # Keep looping until the user types "a""b"or"c"
    while True:
        
        # if the user typed a key...
        if Draw.hasNextKeyTyped(): 
            choice = Draw.nextKeyTyped()
            
            #only continues if user types a, b, or c
            if choice == 'a' or choice == 'b' or choice == 'c': 
            
                #if ball is at first cup -> answer is correct
                if choice == 'a' and ballPos == 0: ans = True 
                
                #if ball is at second cup -> answer is correct 
                elif choice == 'b' and ballPos == 1: ans = True 
                
                #if ball is at third cup -> answer is correct
                elif choice == 'c' and ballPos ==2: ans = True
                
                #display if answer was right or wrong and show where the ball was
                if ans: speak = "right"
                else: speak = "wrong"
                showBall(ogcups,ballPos,score,highScore,cups,speak,choice)
                return ans


#function to show where the ball is by raising cup:
def showBall(ogcups,ballPos,score,highScore,cups,speak,choice):
    
    #show cups at rest
    drawBoard(ogcups, score, highScore, ballPos,cups,speak,choice)
    time.sleep (1)
    
    #lift the cup with the ball
    cups[ballPos][1]-=100
    drawBoard(ogcups, score, highScore, ballPos,cups,speak,choice)
    time.sleep (1)
    
    #put cup back at rest
    cups[ballPos][1]+=100
    drawBoard(ogcups, score, highScore, ballPos,cups,speak,choice)
    time.sleep (1)
    
    
#Animate the cups swapping using arc motion
def animateSwap (a,b,speed, ogcups, score, highScore,ballPos,cups,nums,speak,choice):
    
    speak = "shuffle" #display shuffling...
    temp,ballPos = ballPos,-1 #cover ball during shuffle
    
    #speed is the difference between the two cups x's
    dx = cups[a][0]-cups[b][0]
    offset = 0 
    
    while offset<abs(dx):
        
        #If a is to the right of b
        if dx>0 and cups[a]>=ogcups[b]:
            #Subtract speed from the first
            cups[a][0]-=speed 
            #Add speed to the other
            cups[b][0]+=speed
            
        #if b is to the right of a
        elif dx<0 and cups[a]<=ogcups[b]:
            #Add speed from first cup
            cups[a][0]+=speed
            #Subtract speed from other
            cups[b][0]-=speed
            
        #find the dy to move cups in a projectile motion
        yScale = 50 
        dy = yScale * math.sin(math.radians(offset/abs(dx)*180))
        
        #add the speed of y to cup[a]'s y and subtract it from cups[b]'s y
        cups[a][1] = ogcups[a][1]+dy
        cups[b][1] = ogcups[b][1]-dy
        offset += speed
        
        #animate
        drawBoard(ogcups, score, highScore, ballPos,cups,speak,choice)
        
        #set cups back to resting points
        cups[a][1],cups[b][1]=ogcups[a][1],ogcups[b][1]
        
    #swap cups
    cups[a], cups[b] = cups[b], cups[a]  

    return temp


#create drawBoard:
def drawBoard (ogcups, score, highScore, ballPos,cups,speak,choice):
    
    #Clear the canvas
    Draw.clear()   
    
    #set background with rectangular dimensions
    sizeX = 800
    sizeY = 500
    
    #different background colors
    cabinBrown = Draw.color(128, 101, 84) #background
    greenPool = Draw.color(21,88,67) #pool table color
    wineBrown = Draw.color(114, 47, 55) #pool table border
    greenDarker = Draw.color(21,78,67) #dark pool table color    
    
    #brown cabin background
    Draw.setBackground(cabinBrown)

    
    #cabin lines
    wall = 0
    for i in range(10):
        Draw.setColor(Draw.BLACK)
        Draw.line(0,50+wall,sizeX,50+wall)
        wall+=50

    #pool table background
    poolTable(sizeX,sizeY,greenPool,wineBrown,greenDarker)
    
    #texts on screen
    text(speak,cups,ballPos,choice,score,highScore,greenDarker)
    
    #shadows of each cup using their x,y coords
    for cup in cups:
        shadow(cup[0],cup[1])
    
    #if the cups aren't moving show the ball at it’s position
    if ballPos>=0:
        drawBall(ballPos,cups)
        
    #show each of the cups using their x,y coords
    for cup in cups:
        drawCup(cup[0],cup[1])
    
    Draw.show()
       
       
def poolTable(sizeX,sizeY,greenPool,wineBrown,greenDarker): 
    
    #pool table/floor background
    Draw.setColor(greenPool)
    Draw.filledRect(0,sizeY/2,sizeX,sizeY)
    Draw.setColor(wineBrown)
    Draw.filledRect(0,sizeY/2-10,sizeX,20)
    
    #table edges / dots:
    Draw.setColor(Draw.BLACK)
    dot = 100
    for i in range(4):
        Draw.filledOval(dot,sizeY/2-6,12,12)
        dot+=200
    
    #pool table felt edge 
    Draw.setColor(greenDarker)
    Draw.filledRect(0,sizeY/2+20,sizeX,25)
    
    #pool table ball pocket
    pocketRim = Draw.color(50,20,20)
    pocket = Draw.color(30,12,10)
    Draw.setColor(pocketRim)
    Draw.filledOval(sizeX/2-5,sizeY/2+5,70,48)
    Draw.setColor(pocket)
    Draw.filledOval(sizeX/2,sizeY/2+10,60,56)
    
    
def text(speak,cups,ballPos,choice,score,highScore,wineBrown):
    
    #Draw the score and High Score
    Draw.setColor(Draw.WHITE)
    Draw.filledRect(540,10,255,30)
    say(wineBrown,True,'Helvetica',24)
    Draw.string(f"{score}   HIGH SCORE: {highScore}",550,12)
    
    #correct and incorrect colors
    green = Draw.color(21,150,67)
    red = Draw.color(160, 32, 49)
    
    #Display game texts
    say(Draw.BLACK,True,'Helvetica',45) #details and location of text
    
    if speak=="welcome": Draw.string("Welcome!",320,50) #first time playing
    
    elif speak=="shuffle": Draw.string("Shuffling...",320,50) #while shuffling cups
    
    elif speak=="choose": 
        Draw.string("Choose A, B, or C:",225,50)  #while choosing cups
        
    #if you get the right answer
    elif speak=="right":
        say(green,True,'Helvetica',45)
        Draw.string(f"{choice.upper()} IS CORRECT!",260,50)
        
    #if you the wrong answer
    elif speak=="wrong":
        say(red,True,'Helvetica',45)
        Draw.string(f"{choice.upper()} IS INCORRECT",250,50)
    
    # A B C under the cups so user knows which is which
    if speak=="choose" or speak== "right" or speak=="wrong":
        say(Draw.WHITE,True,'Helvetica',50)
        Draw.string("A",cups[0][0]+10,425)
        Draw.string("B",cups[1][0]+10,425)
        Draw.string("C",cups[2][0]+10,425)    
    

#make cups
def drawCup(x,y):
    
    # make red solo cups
    soloCup = Draw.color(189, 32, 49) #cup color
    darker = Draw.color(175, 32, 49) 
    darkerMore = Draw.color(130, 32, 49)    
    
    #most of cup / top of cup
    coords = [x-30,y,x+72,y,x+116,y+234,x-68,y+234]
    Draw.setColor(soloCup)
    Draw.filledPolygon(coords)
    
    #top rim
    Draw.filledOval(x-30,y-20,102,40)
    Draw.setColor(darker)
    Draw.filledOval(x-28,y-18,100,36)   
   
    #white line
    Draw.setColor(Draw.WHITE)
    Draw.filledOval(x-68,y+180,186,90)
    Draw.setColor(soloCup)
    Draw.filledOval(x-68,y+176,186,90)
    
    #upper lines on cup
    Draw.setColor(darkerMore)
    Draw.oval(x-53,y+105,152,70)
    Draw.setColor(soloCup)
    Draw.filledOval(x-53,y+103,152,70)
    
    #lower lines on cup
    Draw.setColor(darkerMore)
    Draw.oval(x-40,y+30,123,50)
    Draw.setColor(soloCup)
    Draw.filledOval(x-40,y+28,123,50)
    
def drawBall(ballPos,cups):
    #draw 8 ball
    Draw.setColor(Draw.BLACK)
    Draw.filledOval(cups[ballPos][0]-8,330,80,80)
    Draw.setColor(Draw.WHITE)
    Draw.filledOval(cups[ballPos][0]+15,345,40,40) 
    say(Draw.BLACK,False,'Helvetica',35) # 8 
    Draw.string("8",cups[ballPos][0]+25,345)    
    
#instruction function
def say(c,b,f,s):
    Draw.setColor(c)
    Draw.setFontBold(b)
    Draw.setFontFamily(f)
    Draw.setFontSize(s)  
    
    
#shadow function
def shadow(x,y):
    
    #keep y within range
    y = max(0,(min(350,y)))
    
    #as y goes down shadow gets darker, up gets lighter
    scale = y*.12
    shade = Draw.color(21,88-int(scale),67)
    Draw.setColor(shade)
    
    #shadow only x changes and the size of the shadow is bigger as goes up
    Draw.filledOval(x-30,335,130+scale,68+scale)  
    
main()