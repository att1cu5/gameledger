def wordgame():
    acceptablewords=("axe","are","awe","bad","bag","bed","cry","cue","cup","dad","den","dim","ear","eat","end","fin","fox","fly","guy","got","gym","hot","hox","hug","ice","inn","ivy","job","jab","jug","kid","key","kin","lab","let","lit","mad","mom","mud","nap","new","nut","oak","odd","out","pad","pig","pin","qua","qis","qat","rag","rib","run","sad","she","sin","tab","tie","two","urb","ups","use","van","vet","vow","web","wag","won","xed","xis","yag","yum","yes","zap","zag","zap")
def defineinstantwinconstant(x):
    if(x>0):
        return 2.5*(10**-5)*(10**x)
    else:
        return 2.5*(10**-5)
def welcometogames():
    name=input("Hi what is your name: ")
    print("welcome",name)
    return name
def getip():
    import socket
    hostnamed = socket.gethostname()
    local_ipd = socket.gethostbyname(hostnamed)
    return local_ipd
def rpswithtwist(o,f,usernum):
    game="rps"
    mk=0
    ml=0

    score=0
    while(0==0):
        
        #print("welcome",usernum,"to",game)
        import numpy as np
        import random
        picks=["rock","paper","scissors","God"]
        prob=(1-f)/3
        probb=(1-o)/3
        weights=[prob,prob,prob,o]
        weightsa=[probb,probb,probb,f]
        matrixofprob=np.array([[0,-1,1,-1],[1,0,-1,-1],[-1,1,0,-1],[1,1,1,0]])
        x=random.uniform(0,1)
        cv=random.uniform(0,1)
        if(x<prob):
            mk=0
        if(x>=prob and x<(prob*2)):
            mk=1
        if(x>=(2*prob) and x<(prob*3)):
            mk=2
        if(x>(prob*3)):
            mk=3
        #print(mk)
        if(cv<probb):
            ml=0
        if(cv>=probb and cv<(probb*2)):
            ml=1
        if(cv>=(2*probb) and cv<(probb*3)):
            ml=2
        if(cv>(prob*3)):
            ml=3
        
    
        print("you choose", picks[mk])
        print("computer choose",  picks[ml])
        if(matrixofprob[mk][ml]<0):
            print("you lost")
            score+=int(matrixofprob[mk][ml])
            ukl=input("Do you want to play again? ")
            if(ukl=="no"):
                    return score,usernum,ukl
                    break
        
            
        if(matrixofprob[mk][ml]>0):
            print("you won")
            score+=int(matrixofprob[mk][ml])
            
            ukl=input("Do you want to play again? ")
            if(ukl=="no"):
                    return score,usernum,ukl 
                    break
        
     
    
def XO(usernumb):
  
  game="tic tac toe"
  #print("welcome",usernumb,"to",game)
  import numpy as np
            # Online Python compiler (interpreter) to run Python online.
            # Write Python 3 code in this online editor and run it.
  scoreO=0
  scoreX=0
        
  if(1==1):
            import random
            turnorder=int(input("which player should go first X or O type 1 for X and 2 for O: "))
            
            matrixAns_np=np.array([[0, 0, 0],
                                   [0, 0, 0],
                                   [0, 0, 0]])
            i=0
            a=0
            g=0
            h=0
            b=0
            c=0
            d=0
            e=0
            f=0
            userone=0
            usertwo=0
            while(1==1):
              if(turnorder==1):
                while(1==1):
                    print("x turn")
                    userone=int(input())
            
                    if(userone==usertwo or userone>9 and userone>0):
                        print("X pick another number")
                        userone=int(input())
                    if(userone!=usertwo):    
                        turnorder=2
                        break
               
              elif(turnorder==2):
                  while(1==1):
                  
                    #print("o turn")
                    usertwo=random.randint(1,9)
            
                    if(userone==usertwo or usertwo>9 and usertwo>0):
                        print("processing choice...")
                        usertwo=random.randint(1,9)
                    if(userone!=usertwo):  
                        turnorder=1
                        break
              if(userone!=usertwo and userone!=0 and usertwo!=0):  
                        a=userone
                        b=usertwo
            
                        break
            
            
            if(userone==1 and usertwo==2):
                            print("X | O | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
            
            if(userone==2 and usertwo==1):
                            print("O | X | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==1 and usertwo==3):
                            print("X | - | O")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==3 and usertwo==1):
                            print("O | - | X")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==2 and usertwo==3):
                            print("- | X | O")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==3 and usertwo==2):
                            print("- | O | X")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==4 and usertwo==2):
                            print("- | O | -")
                            print("---------")
                            print("X | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==2 and usertwo==4):
                            print("- | X | -")
                            print("---------")
                            print("O | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==4 and usertwo==3):
                            print("- | - | O")
                            print("---------")
                            print("X | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==3 and usertwo==4):
                            print("- | - | X")
                            print("---------")
                            print("O | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==4 and usertwo==1):
                            print("O | - | -")
                            print("---------")
                            print("X | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==1 and usertwo==4):
                            print("X | - | -")
                            print("---------")
                            print("O | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==5 and usertwo==1):
                            print("O | - | -")
                            print("---------")
                            print("- | X | -")
                            print("---------")
                            print("- | - | -")
            if(userone==1 and usertwo==5):
                            print("X | - | -")
                            print("---------")
                            print("- | O | -")
                            print("---------")
                            print("- | - | -")
            if(userone==5 and usertwo==2):
                            print("- | O | -")
                            print("---------")
                            print("- | X | -")
                            print("---------")
                            print("- | - | -")
            if(userone==2 and usertwo==5):
                            print("- | X | -")
                            print("---------")
                            print("- | O | -")
                            print("---------")
                            print("- | - | -")
            if(userone==5 and usertwo==3):
                            print("- | - | O")
                            print("---------")
                            print("- | X | -")
                            print("---------")
                            print("- | - | -")
            if(userone==3 and usertwo==5):
                            print("- | - | X")
                            print("---------")
                            print("- | O | -")
                            print("---------")
                            print("- | - | -")
            if(userone==5 and usertwo==4):
                            print("- | - | -")
                            print("---------")
                            print("O | X | -")
                            print("---------")
                            print("- | - | -")
            if(userone==4 and usertwo==5):
                            print("- | - | -")
                            print("---------")
                            print("X | O | -")
                            print("---------")
                            print("- | - | -")
            if(userone==6 and usertwo==1):
                            print("O | - | -")
                            print("---------")
                            print("- | - | X")
                            print("---------")
                            print("- | - | -")
            if(userone==1 and usertwo==6):
                            print("X | - | -")
                            print("---------")
                            print("- | - | O")
                            print("---------")
                            print("- | - | -")
            if(userone==6 and usertwo==2):
                            print("- | O | -")
                            print("---------")
                            print("- | - | X")
                            print("---------")
                            print("- | - | -")
            if(userone==2 and usertwo==6):
                            print("- | X | -")
                            print("---------")
                            print("- | - | O")
                            print("---------")
                            print("- | - | -")
            if(userone==6 and usertwo==3):
                            print("- | - | O")
                            print("---------")
                            print("- | - | X")
                            print("---------")
                            print("- | - | -")
            if(userone==3 and usertwo==6):
                            print("- | - | X")
                            print("---------")
                            print("- | - | O")
                            print("---------")
                            print("- | - | -")
            if(userone==6 and usertwo==4):
                            print("- | - | -")
                            print("---------")
                            print("O | - | X")
                            print("---------")
                            print("- | - | -")
            if(userone==4 and usertwo==6):
                            print("- | - | -")
                            print("---------")
                            print("X | - | O")
                            print("---------")
                            print("- | - | -")
            if(userone==6 and usertwo==5):
                            print("- | - | -")
                            print("---------")
                            print("- | O | X")
                            print("---------")
                            print("- | - | -")
            if(userone==5 and usertwo==6):
                            print("- | - | -")
                            print("---------")
                            print("- | X | O")
                            print("---------")
                            print("- | - | -")
            if(userone==7 and usertwo==1):
                            print("O | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("X | - | -")
            if(userone==1 and usertwo==7):
                            print("X | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("O | - | -")
            if(userone==7 and usertwo==2):
                            print("- | O | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("X | - | -")
            if(userone==2 and usertwo==7):
                            print("- | X | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("O | - | -")
            if(userone==7 and usertwo==3):
                            print("- | - | O")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("X | - | -")
            if(userone==3 and usertwo==7):
                            print("- | - | X")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("O | - | -")
            if(userone==7 and usertwo==4):
                            print("- | - | -")
                            print("---------")
                            print("O | - | -")
                            print("---------")
                            print("X | - | -")
            if(userone==4 and usertwo==7):
                            print("- | - | -")
                            print("---------")
                            print("X | - | -")
                            print("---------")
                            print("O | - | -")
            if(userone==7 and usertwo==5):
                            print("- | - | -")
                            print("---------")
                            print("- | O | -")
                            print("---------")
                            print("X | - | -")
            if(userone==5 and usertwo==7):
                            print("- | - | -")
                            print("---------")
                            print("- | X | -")
                            print("---------")
                            print("O | - | -")
            if(userone==7 and usertwo==6):
                            print("- | - | -")
                            print("---------")
                            print("- | - | O")
                            print("---------")
                            print("X | - | -")
            if(userone==6 and usertwo==7):
                            print("- | - | -")
                            print("---------")
                            print("- | - | X")
                            print("---------")
                            print("O | - | -")
            if(userone==8 and usertwo==1):
                            print("O | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | O | -")
            if(userone==1 and usertwo==8):
                            print("X | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | O | -")
            if(userone==8 and usertwo==2):
                            print("- | O | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | X | -")
            if(userone==2 and usertwo==8):
                            print("- | X | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | O | -")
            if(userone==8 and usertwo==3):
                            print("- | - | O")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | X | -")
            if(userone==3 and usertwo==8):
                            print("- | - | X")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | O | -")
            if(userone==8 and usertwo==4):
                            print("- | - | -")
                            print("---------")
                            print("O | - | -")
                            print("---------")
                            print("- | X | -")
            if(userone==4 and usertwo==8):
                            print("- | - | -")
                            print("---------")
                            print("X | - | -")
                            print("---------")
                            print("- | O | -")
            if(userone==8 and usertwo==5):
                            print("- | - | -")
                            print("---------")
                            print("- | O | -")
                            print("---------")
                            print("- | X | -")
            if(userone==5 and usertwo==8):
                            print("- | - | -")
                            print("---------")
                            print("- | X | -")
                            print("---------")
                            print("- | O | -")
            if(userone==8 and usertwo==6):
                            print("- | - | -")
                            print("---------")
                            print("- | - | O")
                            print("---------")
                            print("- | X | -")
            if(userone==6 and usertwo==8):
                            print("- | - | -")
                            print("---------")
                            print("- | - | X")
                            print("---------")
                            print("- | O | -")
            if(userone==8 and usertwo==7):
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("O | X | -")
            if(userone==7 and usertwo==8):
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("X | O | -")
            if(userone==9 and usertwo==1):
                            print("O | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | X")
            if(userone==1 and usertwo==9):
                            print("X | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | O")
            if(userone==9 and usertwo==2):
                            print("- | O | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | X")
            if(userone==2 and usertwo==9):
                            print("- | X | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | O")
            if(userone==9 and usertwo==3):
                            print("- | - | O")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | X")
            if(userone==3 and usertwo==9):
                            print("- | - | X")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | O")
            if(userone==9 and usertwo==4):
                            print("- | - | -")
                            print("---------")
                            print("O | - | -")
                            print("---------")
                            print("- | - | X")
            if(userone==4 and usertwo==9):
                            print("- | - | -")
                            print("---------")
                            print("X | - | -")
                            print("---------")
                            print("- | - | O")
            if(userone==9 and usertwo==5):
                            print("- | - | -")
                            print("---------")
                            print("- | O | -")
                            print("---------")
                            print("- | - | X")
            if(userone==5 and usertwo==9):
                            print("- | - | -")
                            print("---------")
                            print("- | X | -")
                            print("---------")
                            print("- | - | O")
            if(userone==9 and usertwo==6):
                            print("- | - | -")
                            print("---------")
                            print("- | - | O")
                            print("---------")
                            print("- | - | X")
            if(userone==6 and usertwo==9):
                            print("- | - | -")
                            print("---------")
                            print("- | - | X")
                            print("---------")
                            print("- | - | O")
            if(userone==9 and usertwo==7):
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("O | - | X")
            if(userone==7 and usertwo==9):
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("X | - | O")
            if(userone==9 and usertwo==8):
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | O | X")
            if(userone==8 and usertwo==9):
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | X | O")
            
            
            usertwo=0
            userone=0
            while(1==1):
                if(turnorder==1):
                    while(1==1):
                        print("x turn")
                        userone=int(input())
                
                        if(userone==usertwo or usertwo>9 or usertwo>0 or userone==b or userone==a):
                            
                            print("X pick another number")
                            
                        if(userone!=usertwo and userone!=a and userone!=b):    
                            turnorder=2
                            break
            
                elif(turnorder==2):
                    while(1==1):
                        
                        usertwo=random.randint(1,9)
                
                        if(userone==usertwo or usertwo>9 or usertwo>0 or usertwo==b or usertwo==a):
                            
                            print("processing choice...")
            
                
                        if(userone!=usertwo and usertwo!=a and usertwo!=b):
                            turnorder=1
                            break
                if(userone!=usertwo and usertwo!=0 and userone!=0):  
                        d=usertwo
                        c=userone
                        break
              
            if(userone==1 and usertwo==2):
                            print("X | O | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==2 and usertwo==1):
                            print("O | X | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==1 and usertwo==3):
                            print("X | - | O")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==3 and usertwo==1):
                            print("O | - | X")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==2 and usertwo==3):
                            print("- | X | O")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==3 and usertwo==2):
                            print("- | O | X")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==4 and usertwo==2):
                            print("- | O | -")
                            print("---------")
                            print("X | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==2 and usertwo==4):
                            print("- | X | -")
                            print("---------")
                            print("O | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==4 and usertwo==3):
                            print("- | - | O")
                            print("---------")
                            print("X | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==3 and usertwo==4):
                            print("- | - | X")
                            print("---------")
                            print("O | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==4 and usertwo==1):
                            print("O | - | -")
                            print("---------")
                            print("X | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==1 and usertwo==4):
                            print("X | - | -")
                            print("---------")
                            print("O | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==5 and usertwo==1):
                            print("O | - | -")
                            print("---------")
                            print("- | X | -")
                            print("---------")
                            print("- | - | -")
            if(userone==1 and usertwo==5):
                            print("X | - | -")
                            print("---------")
                            print("- | O | -")
                            print("---------")
                            print("- | - | -")
            if(userone==5 and usertwo==2):
                            print("- | O | -")
                            print("---------")
                            print("- | X | -")
                            print("---------")
                            print("- | - | -")
            if(userone==2 and usertwo==5):
                            print("- | X | -")
                            print("---------")
                            print("- | O | -")
                            print("---------")
                            print("- | - | -")
            if(userone==5 and usertwo==3):
                            print("- | - | O")
                            print("---------")
                            print("- | X | -")
                            print("---------")
                            print("- | - | -")
            if(userone==3 and usertwo==5):
                            print("- | - | X")
                            print("---------")
                            print("- | O | -")
                            print("---------")
                            print("- | - | -")
            if(userone==5 and usertwo==4):
                            print("- | - | -")
                            print("---------")
                            print("O | X | -")
                            print("---------")
                            print("- | - | -")
            if(userone==4 and usertwo==5):
                            print("- | - | -")
                            print("---------")
                            print("X | O | -")
                            print("---------")
                            print("- | - | -")
            if(userone==6 and usertwo==1):
                            print("O | - | -")
                            print("---------")
                            print("- | - | X")
                            print("---------")
                            print("- | - | -")
            if(userone==1 and usertwo==6):
                            print("X | - | -")
                            print("---------")
                            print("- | - | O")
                            print("---------")
                            print("- | - | -")
            if(userone==6 and usertwo==2):
                            print("- | O | -")
                            print("---------")
                            print("- | - | X")
                            print("---------")
                            print("- | - | -")
            if(userone==2 and usertwo==6):
                            print("- | X | -")
                            print("---------")
                            print("- | - | O")
                            print("---------")
                            print("- | - | -")
            if(userone==6 and usertwo==3):
                            print("- | - | O")
                            print("---------")
                            print("- | - | X")
                            print("---------")
                            print("- | - | -")
            if(userone==3 and usertwo==6):
                            print("- | - | X")
                            print("---------")
                            print("- | - | O")
                            print("---------")
                            print("- | - | -")
            if(userone==6 and usertwo==4):
                            print("- | - | -")
                            print("---------")
                            print("O | - | X")
                            print("---------")
                            print("- | - | -")
            if(userone==4 and usertwo==6):
                            print("- | - | -")
                            print("---------")
                            print("X | - | O")
                            print("---------")
                            print("- | - | -")
            if(userone==6 and usertwo==5):
                            print("- | - | -")
                            print("---------")
                            print("- | O | X")
                            print("---------")
                            print("- | - | -")
            if(userone==5 and usertwo==6):
                            print("- | - | -")
                            print("---------")
                            print("- | X | O")
                            print("---------")
                            print("- | - | -")
            if(userone==7 and usertwo==1):
                            print("O | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("X | - | -")
            if(userone==1 and usertwo==7):
                            print("X | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("O | - | -")
            if(userone==7 and usertwo==2):
                            print("- | O | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("X | - | -")
            if(userone==2 and usertwo==7):
                            print("- | X | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("O | - | -")
            if(userone==7 and usertwo==3):
                            print("- | - | O")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("X | - | -")
            if(userone==3 and usertwo==7):
                            print("- | - | X")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("O | - | -")
            if(userone==7 and usertwo==4):
                            print("- | - | -")
                            print("---------")
                            print("O | - | -")
                            print("---------")
                            print("X | - | -")
            if(userone==4 and usertwo==7):
                            print("- | - | -")
                            print("---------")
                            print("X | - | -")
                            print("---------")
                            print("O | - | -")
            if(userone==7 and usertwo==5):
                            print("- | - | -")
                            print("---------")
                            print("- | O | -")
                            print("---------")
                            print("X | - | -")
            if(userone==5 and usertwo==7):
                            print("- | - | -")
                            print("---------")
                            print("- | X | -")
                            print("---------")
                            print("O | - | -")
            if(userone==7 and usertwo==6):
                            print("- | - | -")
                            print("---------")
                            print("- | - | O")
                            print("---------")
                            print("X | - | -")
            if(userone==6 and usertwo==7):
                            print("- | - | -")
                            print("---------")
                            print("- | - | X")
                            print("---------")
                            print("O | - | -")
            if(userone==8 and usertwo==1):
                            print("O | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | O | -")
            if(userone==1 and usertwo==8):
                            print("X | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | O | -")
            if(userone==8 and usertwo==2):
                            print("- | O | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | X | -")
            if(userone==2 and usertwo==8):
                            print("- | X | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | O | -")
            if(userone==8 and usertwo==3):
                            print("- | - | O")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | X | -")
            if(userone==3 and usertwo==8):
                            print("- | - | X")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | O | -")
            if(userone==8 and usertwo==4):
                            print("- | - | -")
                            print("---------")
                            print("O | - | -")
                            print("---------")
                            print("- | X | -")
            if(userone==4 and usertwo==8):
                            print("- | - | -")
                            print("---------")
                            print("X | - | -")
                            print("---------")
                            print("- | O | -")
            if(userone==8 and usertwo==5):
                            print("- | - | -")
                            print("---------")
                            print("- | O | -")
                            print("---------")
                            print("- | X | -")
            if(userone==5 and usertwo==8):
                            print("- | - | -")
                            print("---------")
                            print("- | X | -")
                            print("---------")
                            print("- | O | -")
            if(userone==8 and usertwo==6):
                            print("- | - | -")
                            print("---------")
                            print("- | - | O")
                            print("---------")
                            print("- | X | -")
            if(userone==6 and usertwo==8):
                            print("- | - | -")
                            print("---------")
                            print("- | - | X")
                            print("---------")
                            print("- | O | -")
            if(userone==8 and usertwo==7):
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("O | X | -")
            if(userone==7 and usertwo==8):
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("X | O | -")
            if(userone==9 and usertwo==1):
                            print("O | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | X")
            if(userone==1 and usertwo==9):
                            print("X | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | O")
            if(userone==9 and usertwo==2):
                            print("- | O | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | X")
            if(userone==2 and usertwo==9):
                            print("- | X | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | O")
            if(userone==9 and usertwo==3):
                            print("- | - | O")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | X")
            if(userone==3 and usertwo==9):
                            print("- | - | X")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | O")
            if(userone==9 and usertwo==4):
                            print("- | - | -")
                            print("---------")
                            print("O | - | -")
                            print("---------")
                            print("- | - | X")
            if(userone==4 and usertwo==9):
                            print("- | - | -")
                            print("---------")
                            print("X | - | -")
                            print("---------")
                            print("- | - | O")
            if(userone==9 and usertwo==5):
                            print("- | - | -")
                            print("---------")
                            print("- | O | -")
                            print("---------")
                            print("- | - | X")
            if(userone==5 and usertwo==9):
                            print("- | - | -")
                            print("---------")
                            print("- | X | -")
                            print("---------")
                            print("- | - | O")
            if(userone==9 and usertwo==6):
                            print("- | - | -")
                            print("---------")
                            print("- | - | O")
                            print("---------")
                            print("- | - | X")
            if(userone==6 and usertwo==9):
                            print("- | - | -")
                            print("---------")
                            print("- | - | X")
                            print("---------")
                            print("- | - | O")
            if(userone==9 and usertwo==7):
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("O | - | X")
            if(userone==7 and usertwo==9):
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("X | - | O")
            if(userone==9 and usertwo==8):
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | O | X")
            if(userone==8 and usertwo==9):
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | X | O")
            usertwo=0
            userone=0
            while(1==1):
                if(turnorder==1):
                    while(1==1):
                        print("x turns")
                        userone=int(input())
                
                        if(userone==usertwo or usertwo>9 or usertwo>0 or userone==d or userone==c or userone==a or userone==b):
                            
                            print("X pick another number")
                            
                        if(userone!=usertwo and userone!=a and userone!=b and userone!=d and userone!=c):    
                            turnorder=2
                            break
                  
                elif(turnorder==2):
                    while(1==1):
                        print("o turns")
                        usertwo=random.randint(1,9)
                
                        if(userone==usertwo or usertwo>9 or usertwo>0 or usertwo==b or usertwo==a or usertwo==c or usertwo==d):
                            print("processing choice...")
                            
            
                
                        if(userone!=usertwo and usertwo!=a and usertwo!=b and usertwo!=d and usertwo!=c):
                            turnorder=1
                            break
                if(userone!=usertwo and userone!=0 and usertwo!=0):  
                        e=usertwo
                        f=userone
                        break
              
            if(userone==1 and usertwo==2):
                            print("X | O | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==2 and usertwo==1):
                            print("O | X | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==1 and usertwo==3):
                            print("X | - | O")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==3 and usertwo==1):
                            print("O | - | X")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==2 and usertwo==3):
                            print("- | X | O")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==3 and usertwo==2):
                            print("- | O | X")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==4 and usertwo==2):
                            print("- | O | -")
                            print("---------")
                            print("X | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==2 and usertwo==4):
                            print("- | X | -")
                            print("---------")
                            print("O | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==4 and usertwo==3):
                            print("- | - | O")
                            print("---------")
                            print("X | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==3 and usertwo==4):
                            print("- | - | X")
                            print("---------")
                            print("O | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==4 and usertwo==1):
                            print("O | - | -")
                            print("---------")
                            print("X | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==1 and usertwo==4):
                            print("X | - | -")
                            print("---------")
                            print("O | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==5 and usertwo==1):
                            print("O | - | -")
                            print("---------")
                            print("- | X | -")
                            print("---------")
                            print("- | - | -")
            if(userone==1 and usertwo==5):
                            print("X | - | -")
                            print("---------")
                            print("- | O | -")
                            print("---------")
                            print("- | - | -")
            if(userone==5 and usertwo==2):
                            print("- | O | -")
                            print("---------")
                            print("- | X | -")
                            print("---------")
                            print("- | - | -")
            if(userone==2 and usertwo==5):
                            print("- | X | -")
                            print("---------")
                            print("- | O | -")
                            print("---------")
                            print("- | - | -")
            if(userone==5 and usertwo==3):
                            print("- | - | O")
                            print("---------")
                            print("- | X | -")
                            print("---------")
                            print("- | - | -")
            if(userone==3 and usertwo==5):
                            print("- | - | X")
                            print("---------")
                            print("- | O | -")
                            print("---------")
                            print("- | - | -")
            if(userone==5 and usertwo==4):
                            print("- | - | -")
                            print("---------")
                            print("O | X | -")
                            print("---------")
                            print("- | - | -")
            if(userone==4 and usertwo==5):
                            print("- | - | -")
                            print("---------")
                            print("X | O | -")
                            print("---------")
                            print("- | - | -")
            if(userone==6 and usertwo==1):
                            print("O | - | -")
                            print("---------")
                            print("- | - | X")
                            print("---------")
                            print("- | - | -")
            if(userone==1 and usertwo==6):
                            print("X | - | -")
                            print("---------")
                            print("- | - | O")
                            print("---------")
                            print("- | - | -")
            if(userone==6 and usertwo==2):
                            print("- | O | -")
                            print("---------")
                            print("- | - | X")
                            print("---------")
                            print("- | - | -")
            if(userone==2 and usertwo==6):
                            print("- | X | -")
                            print("---------")
                            print("- | - | O")
                            print("---------")
                            print("- | - | -")
            if(userone==6 and usertwo==3):
                            print("- | - | O")
                            print("---------")
                            print("- | - | X")
                            print("---------")
                            print("- | - | -")
            if(userone==3 and usertwo==6):
                            print("- | - | X")
                            print("---------")
                            print("- | - | O")
                            print("---------")
                            print("- | - | -")
            if(userone==6 and usertwo==4):
                            print("- | - | -")
                            print("---------")
                            print("O | - | X")
                            print("---------")
                            print("- | - | -")
            if(userone==4 and usertwo==6):
                            print("- | - | -")
                            print("---------")
                            print("X | - | O")
                            print("---------")
                            print("- | - | -")
            if(userone==6 and usertwo==5):
                            print("- | - | -")
                            print("---------")
                            print("- | O | X")
                            print("---------")
                            print("- | - | -")
            if(userone==5 and usertwo==6):
                            print("- | - | -")
                            print("---------")
                            print("- | X | O")
                            print("---------")
                            print("- | - | -")
            if(userone==7 and usertwo==1):
                            print("O | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("X | - | -")
            if(userone==1 and usertwo==7):
                            print("X | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("O | - | -")
            if(userone==7 and usertwo==2):
                            print("- | O | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("X | - | -")
            if(userone==2 and usertwo==7):
                            print("- | X | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("O | - | -")
            if(userone==7 and usertwo==3):
                            print("- | - | O")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("X | - | -")
            if(userone==3 and usertwo==7):
                            print("- | - | X")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("O | - | -")
            if(userone==7 and usertwo==4):
                            print("- | - | -")
                            print("---------")
                            print("O | - | -")
                            print("---------")
                            print("X | - | -")
            if(userone==4 and usertwo==7):
                            print("- | - | -")
                            print("---------")
                            print("X | - | -")
                            print("---------")
                            print("O | - | -")
            if(userone==7 and usertwo==5):
                            print("- | - | -")
                            print("---------")
                            print("- | O | -")
                            print("---------")
                            print("X | - | -")
            if(userone==5 and usertwo==7):
                            print("- | - | -")
                            print("---------")
                            print("- | X | -")
                            print("---------")
                            print("O | - | -")
            if(userone==7 and usertwo==6):
                            print("- | - | -")
                            print("---------")
                            print("- | - | O")
                            print("---------")
                            print("X | - | -")
            if(userone==6 and usertwo==7):
                            print("- | - | -")
                            print("---------")
                            print("- | - | X")
                            print("---------")
                            print("O | - | -")
            if(userone==8 and usertwo==1):
                            print("O | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | O | -")
            if(userone==1 and usertwo==8):
                            print("X | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | O | -")
            if(userone==8 and usertwo==2):
                            print("- | O | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | X | -")
            if(userone==2 and usertwo==8):
                            print("- | X | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | O | -")
            if(userone==8 and usertwo==3):
                            print("- | - | O")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | X | -")
            if(userone==3 and usertwo==8):
                            print("- | - | X")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | O | -")
            if(userone==8 and usertwo==4):
                            print("- | - | -")
                            print("---------")
                            print("O | - | -")
                            print("---------")
                            print("- | X | -")
            if(userone==4 and usertwo==8):
                            print("- | - | -")
                            print("---------")
                            print("X | - | -")
                            print("---------")
                            print("- | O | -")
            if(userone==8 and usertwo==5):
                            print("- | - | -")
                            print("---------")
                            print("- | O | -")
                            print("---------")
                            print("- | X | -")
            if(userone==5 and usertwo==8):
                            print("- | - | -")
                            print("---------")
                            print("- | X | -")
                            print("---------")
                            print("- | O | -")
            if(userone==8 and usertwo==6):
                            print("- | - | -")
                            print("---------")
                            print("- | - | O")
                            print("---------")
                            print("- | X | -")
            if(userone==6 and usertwo==8):
                            print("- | - | -")
                            print("---------")
                            print("- | - | X")
                            print("---------")
                            print("- | O | -")
            if(userone==8 and usertwo==7):
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("O | X | -")
            if(userone==7 and usertwo==8):
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("X | O | -")
            if(userone==9 and usertwo==1):
                            print("O | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | X")
            if(userone==1 and usertwo==9):
                            print("X | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | O")
            if(userone==9 and usertwo==2):
                            print("- | O | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | X")
            if(userone==2 and usertwo==9):
                            print("- | X | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | O")
            if(userone==9 and usertwo==3):
                            print("- | - | O")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | X")
            if(userone==3 and usertwo==9):
                            print("- | - | X")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | O")
            if(userone==9 and usertwo==4):
                            print("- | - | -")
                            print("---------")
                            print("O | - | -")
                            print("---------")
                            print("- | - | X")
            if(userone==4 and usertwo==9):
                            print("- | - | -")
                            print("---------")
                            print("X | - | -")
                            print("---------")
                            print("- | - | O")
            if(userone==9 and usertwo==5):
                            print("- | - | -")
                            print("---------")
                            print("- | O | -")
                            print("---------")
                            print("- | - | X")
            if(userone==5 and usertwo==9):
                            print("- | - | -")
                            print("---------")
                            print("- | X | -")
                            print("---------")
                            print("- | - | O")
            if(userone==9 and usertwo==6):
                            print("- | - | -")
                            print("---------")
                            print("- | - | O")
                            print("---------")
                            print("- | - | X")
            if(userone==6 and usertwo==9):
                            print("- | - | -")
                            print("---------")
                            print("- | - | X")
                            print("---------")
                            print("- | - | O")
            if(userone==9 and usertwo==7):
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("O | - | X")
            if(userone==7 and usertwo==9):
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("X | - | O")
            if(userone==9 and usertwo==8):
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | O | X")
            if(userone==8 and usertwo==9):
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | X | O")
            usertwo=0
            userone=0
            while(1==1):
                if(turnorder==1):
                    while(1==1):
                        print("x turn")
                        userone=int(input())
                
                        if(userone==usertwo or usertwo>9 or usertwo>0 or userone==d or userone==c or userone==a or userone==b or usertwo==f or usertwo==e):
                            
                            print("X pick another number")
                            
                        if(userone!=usertwo and userone!=a and userone!=b and userone!=d and userone!=c and userone!=e and userone!=f):    
                            turnorder=2
                            break
                  
                elif(turnorder==2):
                    while(1==1):
                        #print("o turn")
                        usertwo=random.randint(1,9)
                
                        if(userone==usertwo or usertwo>9 or usertwo>0 or usertwo==b or usertwo==a or usertwo==c or usertwo==d or usertwo==f or usertwo==e):
                            print("processing choice...")
                            
            
                
                        if(userone!=usertwo and usertwo!=a and usertwo!=b and usertwo!=d and usertwo!=c and usertwo!=e and usertwo!=f):
                            turnorder=1
                            break
                if(userone!=usertwo and userone!=0 and usertwo!=0):  
                        g=usertwo
                        h=userone
                        break
              
            if(userone==1 and usertwo==2):
                            print("X | O | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==2 and usertwo==1):
                            print("O | X | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==1 and usertwo==3):
                            print("X | - | O")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==3 and usertwo==1):
                            print("O | - | X")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==2 and usertwo==3):
                            print("- | X | O")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==3 and usertwo==2):
                            print("- | O | X")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==4 and usertwo==2):
                            print("- | O | -")
                            print("---------")
                            print("X | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==2 and usertwo==4):
                            print("- | X | -")
                            print("---------")
                            print("O | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==4 and usertwo==3):
                            print("- | - | O")
                            print("---------")
                            print("X | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==3 and usertwo==4):
                            print("- | - | X")
                            print("---------")
                            print("O | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==4 and usertwo==1):
                            print("O | - | -")
                            print("---------")
                            print("X | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==1 and usertwo==4):
                            print("X | - | -")
                            print("---------")
                            print("O | - | -")
                            print("---------")
                            print("- | - | -")
            if(userone==5 and usertwo==1):
                            print("O | - | -")
                            print("---------")
                            print("- | X | -")
                            print("---------")
                            print("- | - | -")
            if(userone==1 and usertwo==5):
                            print("X | - | -")
                            print("---------")
                            print("- | O | -")
                            print("---------")
                            print("- | - | -")
            if(userone==5 and usertwo==2):
                            print("- | O | -")
                            print("---------")
                            print("- | X | -")
                            print("---------")
                            print("- | - | -")
            if(userone==2 and usertwo==5):
                            print("- | X | -")
                            print("---------")
                            print("- | O | -")
                            print("---------")
                            print("- | - | -")
            if(userone==5 and usertwo==3):
                            print("- | - | O")
                            print("---------")
                            print("- | X | -")
                            print("---------")
                            print("- | - | -")
            if(userone==3 and usertwo==5):
                            print("- | - | X")
                            print("---------")
                            print("- | O | -")
                            print("---------")
                            print("- | - | -")
            if(userone==5 and usertwo==4):
                            print("- | - | -")
                            print("---------")
                            print("O | X | -")
                            print("---------")
                            print("- | - | -")
            if(userone==4 and usertwo==5):
                            print("- | - | -")
                            print("---------")
                            print("X | O | -")
                            print("---------")
                            print("- | - | -")
            if(userone==6 and usertwo==1):
                            print("O | - | -")
                            print("---------")
                            print("- | - | X")
                            print("---------")
                            print("- | - | -")
            if(userone==1 and usertwo==6):
                            print("X | - | -")
                            print("---------")
                            print("- | - | O")
                            print("---------")
                            print("- | - | -")
            if(userone==6 and usertwo==2):
                            print("- | O | -")
                            print("---------")
                            print("- | - | X")
                            print("---------")
                            print("- | - | -")
            if(userone==2 and usertwo==6):
                            print("- | X | -")
                            print("---------")
                            print("- | - | O")
                            print("---------")
                            print("- | - | -")
            if(userone==6 and usertwo==3):
                            print("- | - | O")
                            print("---------")
                            print("- | - | X")
                            print("---------")
                            print("- | - | -")
            if(userone==3 and usertwo==6):
                            print("- | - | X")
                            print("---------")
                            print("- | - | O")
                            print("---------")
                            print("- | - | -")
            if(userone==6 and usertwo==4):
                            print("- | - | -")
                            print("---------")
                            print("O | - | X")
                            print("---------")
                            print("- | - | -")
            if(userone==4 and usertwo==6):
                            print("- | - | -")
                            print("---------")
                            print("X | - | O")
                            print("---------")
                            print("- | - | -")
            if(userone==6 and usertwo==5):
                            print("- | - | -")
                            print("---------")
                            print("- | O | X")
                            print("---------")
                            print("- | - | -")
            if(userone==5 and usertwo==6):
                            print("- | - | -")
                            print("---------")
                            print("- | X | O")
                            print("---------")
                            print("- | - | -")
            if(userone==7 and usertwo==1):
                            print("O | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("X | - | -")
            if(userone==1 and usertwo==7):
                            print("X | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("O | - | -")
            if(userone==7 and usertwo==2):
                            print("- | O | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("X | - | -")
            if(userone==2 and usertwo==7):
                            print("- | X | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("O | - | -")
            if(userone==7 and usertwo==3):
                            print("- | - | O")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("X | - | -")
            if(userone==3 and usertwo==7):
                            print("- | - | X")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("O | - | -")
            if(userone==7 and usertwo==4):
                            print("- | - | -")
                            print("---------")
                            print("O | - | -")
                            print("---------")
                            print("X | - | -")
            if(userone==4 and usertwo==7):
                            print("- | - | -")
                            print("---------")
                            print("X | - | -")
                            print("---------")
                            print("O | - | -")
            if(userone==7 and usertwo==5):
                            print("- | - | -")
                            print("---------")
                            print("- | O | -")
                            print("---------")
                            print("X | - | -")
            if(userone==5 and usertwo==7):
                            print("- | - | -")
                            print("---------")
                            print("- | X | -")
                            print("---------")
                            print("O | - | -")
            if(userone==7 and usertwo==6):
                            print("- | - | -")
                            print("---------")
                            print("- | - | O")
                            print("---------")
                            print("X | - | -")
            if(userone==6 and usertwo==7):
                            print("- | - | -")
                            print("---------")
                            print("- | - | X")
                            print("---------")
                            print("O | - | -")
            if(userone==8 and usertwo==1):
                            print("O | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | O | -")
            if(userone==1 and usertwo==8):
                            print("X | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | O | -")
            if(userone==8 and usertwo==2):
                            print("- | O | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | X | -")
            if(userone==2 and usertwo==8):
                            print("- | X | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | O | -")
            if(userone==8 and usertwo==3):
                            print("- | - | O")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | X | -")
            if(userone==3 and usertwo==8):
                            print("- | - | X")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | O | -")
            if(userone==8 and usertwo==4):
                            print("- | - | -")
                            print("---------")
                            print("O | - | -")
                            print("---------")
                            print("- | X | -")
            if(userone==4 and usertwo==8):
                            print("- | - | -")
                            print("---------")
                            print("X | - | -")
                            print("---------")
                            print("- | O | -")
            if(userone==8 and usertwo==5):
                            print("- | - | -")
                            print("---------")
                            print("- | O | -")
                            print("---------")
                            print("- | X | -")
            if(userone==5 and usertwo==8):
                            print("- | - | -")
                            print("---------")
                            print("- | X | -")
                            print("---------")
                            print("- | O | -")
            if(userone==8 and usertwo==6):
                            print("- | - | -")
                            print("---------")
                            print("- | - | O")
                            print("---------")
                            print("- | X | -")
            if(userone==6 and usertwo==8):
                            print("- | - | -")
                            print("---------")
                            print("- | - | X")
                            print("---------")
                            print("- | O | -")
            if(userone==8 and usertwo==7):
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("O | X | -")
            if(userone==7 and usertwo==8):
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("X | O | -")
            if(userone==9 and usertwo==1):
                            print("O | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | X")
            if(userone==1 and usertwo==9):
                            print("X | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | O")
            if(userone==9 and usertwo==2):
                            print("- | O | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | X")
            if(userone==2 and usertwo==9):
                            print("- | X | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | O")
            if(userone==9 and usertwo==3):
                            print("- | - | O")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | X")
            if(userone==3 and usertwo==9):
                            print("- | - | X")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | O")
            if(userone==9 and usertwo==4):
                            print("- | - | -")
                            print("---------")
                            print("O | - | -")
                            print("---------")
                            print("- | - | X")
            if(userone==4 and usertwo==9):
                            print("- | - | -")
                            print("---------")
                            print("X | - | -")
                            print("---------")
                            print("- | - | O")
            if(userone==9 and usertwo==5):
                            print("- | - | -")
                            print("---------")
                            print("- | O | -")
                            print("---------")
                            print("- | - | X")
            if(userone==5 and usertwo==9):
                            print("- | - | -")
                            print("---------")
                            print("- | X | -")
                            print("---------")
                            print("- | - | O")
            if(userone==9 and usertwo==6):
                            print("- | - | -")
                            print("---------")
                            print("- | - | O")
                            print("---------")
                            print("- | - | X")
            if(userone==6 and usertwo==9):
                            print("- | - | -")
                            print("---------")
                            print("- | - | X")
                            print("---------")
                            print("- | - | O")
            if(userone==9 and usertwo==7):
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("O | - | X")
            if(userone==7 and usertwo==9):
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("X | - | O")
            if(userone==9 and usertwo==8):
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | O | X")
            if(userone==8 and usertwo==9):
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | X | O")
            if(turnorder==1):
                print("last turn X")
                i=45-a-b-c-d-e-f-g-h
                if(i==1):
                            print("X | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
                if(i==2):
                            print("- | X | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
                if(i==3):
                            print("- | - | X")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
                if(i==4):
                            print("- | - | -")
                            print("---------")
                            print("X | - | -")
                            print("---------")
                            print("- | - | -")
                if(i==5):
                            print("- | - | -")
                            print("---------")
                            print("- | X | -")
                            print("---------")
                            print("- | - | -")
                if(i==6):
                            print("- | - | -")
                            print("---------")
                            print("- | - | X")
                            print("---------")
                            print("- | - | -")
                if(i==7):
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("X | - | -")
                if(i==8):
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | X | -")
                if(i==9):
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | X")
            elif(turnorder==2):
                print("last turn O")
                i=45-a-b-c-d-e-f-g-h
                if(i==1):
                            print("O | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
                if(i==2):
                            print("- | O | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
                if(i==3):
                            print("- | - | O")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
                if(i==4):
                            print("- | - | -")
                            print("---------")
                            print("O | - | -")
                            print("---------")
                            print("- | - | -")
                if(i==5):
                            print("- | - | -")
                            print("---------")
                            print("- | O | -")
                            print("---------")
                            print("- | - | -")
                if(i==6):
                            print("- | - | -")
                            print("---------")
                            print("- | - | O")
                            print("---------")
                            print("- | - | -")
                if(i==7):
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("O | - | -")
                if(i==8):
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | O | -")
                if(i==9):
                            print("- | - | -")
                            print("---------")
                            print("- | - | -")
                            print("---------")
                            print("- | - | O")
            if(turnorder==2):
              Oturns=[0,0,0,0,0]
              Xtruns=[0,0,0,0]
              Xturns=[a,c,f,h]
              Oturns=[b,d,e,g,i]
              
            if(turnorder==1):
              Oturns=[0,0,0,0]
              Xtruns=[0,0,0,0,0]
              Xturns=[a,c,f,h,i]
              Oturns=[b,d,e,g]  
            if(a==1):
              matrix_np = np.array([[1, 0, 0],
                                    [0, 0, 0],
                                    [0, 0, 0]])
            if(a==2):
              matrix_np = np.array([[0, 1, 0],
                                    [0, 0, 0],
                                    [0, 0, 0]])
            if(a==3):
              matrix_np = np.array([[0, 0, 1],
                                    [0, 0, 0],
                                    [0, 0, 0]])
            if(a==4):
              matrix_np = np.array([[0, 0, 0],
                                    [1, 0, 0],
                                    [0, 0, 0]])
            if(a==5):
              matrix_np = np.array([[0, 0, 0],
                                    [0, 1, 0],
                                    [0, 0, 0]])
            if(a==6):
              matrix_np = np.array([[0, 0, 0],
                                    [0, 0, 1],
                                    [0, 0, 0]])    
            if(a==7):
              matrix_np = np.array([[0, 0, 0],
                                    [0, 0, 0],
                                    [1, 0, 0]])
            if(a==8):
              matrix_np = np.array([[0, 0, 0],
                                    [0, 0, 0],
                                    [0, 1, 0]])
            if(a==9):
              matrix_np = np.array([[0, 0, 0],
                                    [0, 0, 0],
                                    [0, 0, 1]])
            if(b==1):
              matrixA_np = np.array([[2, 0, 0],
                                    [0, 0, 0],
                                    [0, 0, 0]])
            if(b==2):
              matrixA_np = np.array([[0, 2, 0],
                                    [0, 0, 0],
                                    [0, 0, 0]])
            if(b==3):
              matrixA_np = np.array([[0, 0, 2],
                                    [0, 0, 0],
                                    [0, 0, 0]])
            if(b==4):
              matrixA_np = np.array([[0, 0, 0],
                                    [2, 0, 0],
                                    [0, 0, 0]])
            if(b==5):
              matrixA_np = np.array([[0, 0, 0],
                                    [0, 2, 0],
                                    [0, 0, 0]])
            if(b==6):
              matrixA_np = np.array([[0, 0, 0],
                                    [0, 0, 2],
                                    [0, 0, 0]])
            if(b==7):
              matrixA_np = np.array([[0, 0, 0],
                                    [0, 0, 0],
                                    [2, 0, 0]])
            if(b==8):
              matrixA_np = np.array([[0, 0, 0],
                                    [0, 0, 0],
                                    [0, 2, 0]])
            if(b==9):
              matrixA_np = np.array([[0, 0, 0],
                                    [0, 0, 0],
                                    [0, 0, 2]])
            if(c==1):
              matrixB_np = np.array([[1, 0, 0],
                                    [0, 0, 0],
                                    [0, 0, 0]])
            if(c==2):
              matrixB_np = np.array([[0, 1, 0],
                                    [0, 0, 0],
                                    [0, 0, 0]])
            if(c==3):
              matrixB_np = np.array([[0, 0, 1],
                                    [0, 0, 0],
                                    [0, 0, 0]])
            if(c==4):
              matrixB_np = np.array([[0, 0, 0],
                                    [1, 0, 0],
                                    [0, 0, 0]])
            if(c==5):
              matrixB_np = np.array([[0, 0, 0],
                                    [0, 1, 0],
                                    [0, 0, 0]])
            if(c==6):
              matrixB_np = np.array([[0, 0, 0],
                                    [0, 0, 1],
                                    [0, 0, 0]])
            if(c==7):
              matrixB_np = np.array([[0, 0, 0],
                                    [0, 0, 0],
                                    [1, 0, 0]])
            if(c==8):
              matrixB_np = np.array([[0, 0, 0],
                                    [0, 0, 0],
                                    [0, 1, 0]])
            if(c==9):
              matrixB_np = np.array([[0, 0, 0],
                                    [0, 0, 0],
                                    [0, 0, 1]])
            if(d==1):
              matrixC_np = np.array([[2, 0, 0],
                                    [0, 0, 0],
                                    [0, 0, 0]])
            if(d==2):
              matrixC_np = np.array([[0, 2, 0],
                                    [0, 0, 0],
                                    [0, 0, 0]])
            if(d==3):
              matrixC_np = np.array([[0, 0, 2],
                                    [0, 0, 0],
                                    [0, 0, 0]])
            if(d==4):
              matrixC_np = np.array([[0, 0, 0],
                                    [2, 0, 0],
                                    [0, 0, 0]])
            if(d==5):
              matrixC_np = np.array([[0, 0, 0],
                                    [0, 2, 0],
                                    [0, 0, 0]])
            if(d==6):
              matrixC_np = np.array([[0, 0, 0],
                                    [0, 0, 2],
                                    [0, 0, 0]])
            if(d==7):
              matrixC_np = np.array([[0, 0, 0],
                                    [0, 0, 0],
                                    [2, 0, 0]])
            if(d==8):
              matrixC_np = np.array([[0, 0, 0],
                                    [0, 0, 0],
                                    [0, 2, 0]])
            if(d==9):
              matrixC_np = np.array([[0, 0, 0],
                                    [0, 0, 0],
                                    [0, 0, 2]])
            if(e==1):
              matrixD_np = np.array([[2, 0, 0],
                                    [0, 0, 0],
                                    [0, 0, 0]])
            if(e==2):
              matrixD_np = np.array([[0, 2, 0],
                                    [0, 0, 0],
                                    [0, 0, 0]])
            if(e==3):
              matrixD_np = np.array([[0, 0, 2],
                                    [0, 0, 0],
                                    [0, 0, 0]])
            if(e==4):
              matrixD_np = np.array([[0, 0, 0],
                                    [2, 0, 0],
                                    [0, 0, 0]])
            if(e==5):
              matrixD_np = np.array([[0, 0, 0],
                                    [0, 2, 0],
                                    [0, 0, 0]])
            if(e==6):
              matrixD_np = np.array([[0, 0, 0],
                                    [0, 0, 2],
                                    [0, 0, 0]])
            if(e==7):
              matrixD_np = np.array([[0, 0, 0],
                                    [0, 0, 0],
                                    [2, 0, 0]])
            if(e==8):
              matrixD_np = np.array([[0, 0, 0],
                                    [0, 0, 0],
                                    [0, 2, 0]])
            if(e==9):
              matrixD_np = np.array([[0, 0, 0],
                                    [0, 0, 0],
                                    [0, 0, 2]])
            if(f==1):
              matrixE_np = np.array([[1, 0, 0],
                                    [0, 0, 0],
                                    [0, 0, 0]])
            if(f==2):
              matrixE_np = np.array([[0, 1, 0],
                                    [0, 0, 0],
                                    [0, 0, 0]])
            if(f==3):
              matrixE_np = np.array([[0, 0, 1],
                                    [0, 0, 0],
                                    [0, 0, 0]])
            if(f==4):
              matrixE_np = np.array([[0, 0, 0],
                                    [1, 0, 0],
                                    [0, 0, 0]])
            if(f==5):
              matrixE_np = np.array([[0, 0, 0],
                                    [0, 1, 0],
                                    [0, 0, 0]])
            if(f==6):
              matrixE_np = np.array([[0, 0, 0],
                                    [0, 0, 1],
                                    [0, 0, 0]])
            if(f==7):
              matrixE_np = np.array([[0, 0, 0],
                                    [0, 0, 0],
                                    [1, 0, 0]])
            if(f==8):
              matrixE_np = np.array([[0, 0, 0],
                                    [0, 0, 0],
                                    [0, 1, 0]])
            if(f==9):
              matrixE_np = np.array([[0, 0, 0],
                                    [0, 0, 0],
                                    [0, 0, 1]])
            if(h==1):
              matrixF_np = np.array([[1, 0, 0],
                                    [0, 0, 0],
                                    [0, 0, 0]])
            if(h==2):
              matrixF_np = np.array([[0, 1, 0],
                                    [0, 0, 0],
                                    [0, 0, 0]])
            if(h==3):
              matrixF_np = np.array([[0, 0, 1],
                                    [0, 0, 0],
                                    [0, 0, 0]])
            if(h==4):
              matrixF_np = np.array([[0, 0, 0],
                                    [1, 0, 0],
                                    [0, 0, 0]])
            if(h==5):
              matrixF_np = np.array([[0, 0, 0],
                                    [0, 1, 0],
                                    [0, 0, 0]])
            if(h==6):
              matrixF_np = np.array([[0, 0, 0],
                                    [0, 0, 1],
                                    [0, 0, 0]])
            if(h==7):
              matrixF_np = np.array([[0, 0, 0],
                                    [0, 0, 0],
                                    [1, 0, 0]])
            if(h==8):
              matrixF_np = np.array([[0, 0, 0],
                                    [0, 0, 0],
                                    [0, 1, 0]])
            if(h==9):
              matrixF_np = np.array([[0, 0, 0],
                                    [0, 0, 0],
                                    [0, 0, 1]])
            if(g==1):
              matrixG_np = np.array([[2, 0, 0],
                                    [0, 0, 0],
                                    [0, 0, 0]])
            if(g==2):
              matrixG_np = np.array([[0, 2, 0],
                                    [0, 0, 0],
                                    [0, 0, 0]])
            if(g==3):
              matrixG_np = np.array([[0, 0, 2],
                                    [0, 0, 0],
                                    [0, 0, 0]])
            if(g==4):
              matrixG_np = np.array([[0, 0, 0],
                                    [2, 0, 0],
                                    [0, 0, 0]])
            if(g==5):
              matrixG_np = np.array([[0, 0, 0],
                                    [0, 2, 0],
                                    [0, 0, 0]])
            if(g==6):
              matrixG_np = np.array([[0, 0, 0],
                                    [0, 0, 2],
                                    [0, 0, 0]])
            if(g==7):
              matrixG_np = np.array([[0, 0, 0],
                                    [0, 0, 0],
                                    [2, 0, 0]])
            if(g==8):
              matrixG_np = np.array([[0, 0, 0],
                                    [0, 0, 0],
                                    [0, 2, 0]])
            if(g==9):
              matrixG_np = np.array([[0, 0, 0],
                                    [0, 0, 0],
                                    [0, 0, 2]])
            
            matrixAns_np=matrix_np+matrixA_np+matrixC_np+matrixB_np+matrixE_np+matrixF_np+matrixG_np+matrixD_np
            target_value=0
            indices = np.where(matrixAns_np == target_value)
            
            if indices[0].size > 0:  # Check if any element was found
                for r_idx, c_idx in zip(indices[0], indices[1]):
                    matrixAns_np[r_idx,c_idx]=turnorder
            else:
                print(f"Value {target_value} not found in the matrix.")
            print()
            for rowsofm in range(0,2):
                if(matrixAns_np[rowsofm,0]==1):
                    print(" X |",end='')
                elif(matrixAns_np[rowsofm,0]==2):
                    print(" O |",end='')
            if(matrixAns_np[2,0]==1):
                    print(" X ")
            elif(matrixAns_np[2,0]==2):
                    print(" O ")
            print("-----------")
            for rowsofma in range(0,2):
                if(matrixAns_np[rowsofma,1]==1):
                    print(" X |",end='')
                elif(matrixAns_np[rowsofma,1]==2):
                    print(" O |",end='')
            if(matrixAns_np[2,1]==1):
                    print(" X ")
            elif(matrixAns_np[2,1]==2):
                    print(" O ")
            print("-----------")        
            for rowsofmb in range(0,2):
                if(matrixAns_np[rowsofmb,2]==1):
                    print(" X |",end='')
                elif(matrixAns_np[rowsofmb,2]==2):
                    print(" O |",end='')
            if(matrixAns_np[2,2]==1):
                    print(" X ")
            elif(matrixAns_np[2,2]==2):
                    print(" O ")
            if 5 in Oturns:
                if 2 in Oturns:
                    if 8 in Oturns:
                        print("O gains one point")
                        scoreO+=1
            if 5 in Oturns:
                if 3 in Oturns:
                    if 7 in Oturns:
                        print("O gains one point")
                        scoreO+=1   
            if 5 in Oturns:
                if 1 in Oturns:
                    if 9 in Oturns:
                        print("O gains one point")
                        scoreO+=1 
            if 5 in Oturns:
                if 4 in Oturns:
                    if 6 in Oturns:
                        print("O gains one point")
                        scoreO+=1
            if 1 in Oturns:
                if 2 in Oturns:
                    if 3 in Oturns:
                        print("O gains one point")
                        scoreO+=1
            if 1 in Oturns:
                if 4 in Oturns:
                    if 7 in Oturns:
                        print("O gains one point")
                        scoreO+=1
            if 7 in Oturns:
                if 8 in Oturns:
                    if 9 in Oturns:
                        print("O gains one point")
                        scoreO+=1
            if 3 in Oturns:
                if 6 in Oturns:
                    if 9 in Oturns:
                        print("O gains one point")
                        scoreO+=1
            if 5 in Xturns:
                if 2 in Xturns:
                    if 8 in Xturns:
                        print("X gains one point")
                        scoreX+=1
            if 5 in Xturns:
                if 3 in Xturns:
                    if 7 in Xturns:
                        print("X gains one point")
                        scoreX+=1   
            if 5 in Xturns:
                if 1 in Xturns:
                    if 9 in Xturns:
                        print("X gains one point")
                        scoreX+=1 
                  
                        
            if 5 in Xturns:
                if 4 in Xturns:
                    if 6 in Xturns:
                        print("X gains one point")
                        scoreX+=1
            if 1 in Xturns:
                if 2 in Xturns:
                    if 3 in Xturns:
                        print("X gains one point")
                        scoreX+=1
            if 1 in Xturns:
                if 4 in Xturns:
                    if 7 in Xturns:
                        print("X gains one point")
                        scoreX+=1
            if 7 in Xturns:
                if 8 in Xturns:
                    if 9 in Xturns:
                        print("X gains one point")
                        scoreX+=1
            if 3 in Xturns:
                if 6 in Xturns:
                    if 9 in Xturns:
                        print("X gains one point")
                        scoreX+=1
  print()
  print("X points: ",scoreX)
  print("O points: ",scoreO)  
  ans=input("Do you want to keep playing:")   
  
  return scoreX,scoreO,game,ans
def games(k,usernum):
    scores=["",0,"",0,"",0]
    import socket
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    
    while(getip()!=local_ip):
        ans=input("Are you the same person playing this game?")
        if(ans=="no"):
            while(0==0):
                h=9
        if(ans=="yes"):
            break
    if(0==0):
            print("GAME ONE TIC TAC TOE")
            u="tic tac toe"
            j=0
            hil=0
            done=0
            while(u=="tic tac toe"):
                j=XO(usernum)
                #print(j)
                
                if(j[3]=='no'):
                    break
                
                k=j[0]-j[1]
                hil=2
            
            scores[0]=(u)
            scores[1]=(j[0]-j[1])
            #print(usernum,j[0]-j[1])
            #return usernum,j[0]-j[1]
            
            print("GAME TWO ROCK PAPER SCISSORS")
            u="rps"
            while(u=="rps"):
                while(0==0):
                   if(k>0):
                    olp=defineinstantwinconstant(k)
                    olcp=defineinstantwinconstant(0)
                   if(k<0):
                    olcp=defineinstantwinconstant(abs(k))
                    olp=defineinstantwinconstant(0)
                   else:
                    olcp=defineinstantwinconstant(0)
                    olp=defineinstantwinconstant(0)
                   op=rpswithtwist(olcp,olp,usernum)
                   k+=(int(op[0]))
                   hil=4
                   if(op[2]=='no'):
                       break
                if(k!=0 and hil==4):
                       break
                
                       
        
                      
            
            scores[2]=u
            scores[3]=k
            while(u=="word guessing"):
                wordgame()
            return scores   
            if(u!="tic tac toe" and u!="rps" and "word guessing"):
                return 0
        
def main(): 
 
 if(0==0): 
    usernumb=welcometogames()
    l=0
    a=games(l,usernumb)
    print(a)
    
    
if __name__ == "__main__":
    main()
