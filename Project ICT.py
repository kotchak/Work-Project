
while True:
    from random import*
    b=input("Enter the list of players")
    players=b.split(",")
    print(players)
    print("Options")
    print("Enter '2' for creating two teams")
    print("Enter '3' for creating three teams")
    print("Enter '4' for creating four teams")
    n=int(input("Enter the option from menu!"))
    print("Options for teams")
    print("Enter '1' for creating 'ANIMALS' team")
    print("Enter '2' for creating 'COUNTRIES' team")
    print("Enter '3' for creating 'PSL' teams")
    e=int(input("Enter desired option for making team"))
    if(n==2):
        TeamA=[]
        TeamB=[]
        if(len(players))<2:
            print("Please, Enter at least two players for making two teams")
        else:
            while(len(players)>0):
                playerA=choice(players)
                TeamA.append(playerA)
                players.remove(playerA)
                if players==[]:
                    continue
                playerB=choice(players)
                TeamB.append(playerB)
                players.remove(playerB)
            if(e==1):
                teams=["Horse","Camel"]
                team1=choice(teams)
                teams.remove(team1)
                team2=choice(teams)
                teams.remove(team2)
                print("Here are your teams")
                print(team1,TeamA)
                print(team2,TeamB)
            elif(e==2):
                teams=["Pakistan","India"]
                team1=choice(teams)
                teams.remove(team1)
                team2=choice(teams)
                teams.remove(team2)
                print("Here are your teams")
                print(team1,TeamA)
                print(team2,TeamB)
            elif(e==3):
                teams=["ZALMI","GLADIATARS"]
                team1=choice(teams)
                teams.remove(team1)
                team2=choice(teams)
                teams.remove(team2)
                print("Here are your teams")
                print(team1,TeamA)
                print(team2,TeamB)
            else:
                print("PLease!,Enter correct match")
                winsound.Beep(ui,yt)

                
    elif(n==3):
        TeamA=[]
        TeamB=[]
        TeamC=[]
        if(len(players))<3:
            print("Please ,Enter at least 3 players")
        else:
            while(len(players))>0:
                playerA=choice(players)
                TeamA.append(playerA)
                players.remove(playerA)
                if players==[]:
                    break
                playerB=choice(players)
                TeamB.append(playerB)
                players.remove(playerB)
                if players==[]:
                    break
                playerc=choice(players)
                TeamC.append(playerc)
                players.remove(playerc)
            if(e==1):
                teams=["Horse","Camel","Fox"]
                team1=choice(teams)
                teams.remove(team1)
                team2=choice(teams)
                teams.remove(team2)
                team3=choice(teams)
                teams.remove(team3)
                print("Here are your teams")
                print(team1,TeamA)
                print(team2,TeamB)
                print(team3,TeamC)
            elif(e==2):
                teams=["Pakistan","India","England"]
                team1=choice(teams)
                teams.remove(team1)
                team2=choice(teams)
                teams.remove(team2)
                team3=choice(teams)
                teams.remove(team3)
                print("Here are your teams")
                print(team1,TeamA)
                print(team2,TeamB)
                print(team3,TeamC)
            elif(e==3):
                teams=["ZALMI","GLADIATARS","Qalandars"]
                team1=choice(teams)
                teams.remove(team1)
                team2=choice(teams)
                teams.remove(team2)
                team3=choice(teams)
                teams.remove(team3)
                print("Here are your teams")
                print(team1,TeamA)
                print(team2,TeamB)
                print(team3,TeamC)
            else:
                print("PLease!,Enter correct match")
    elif(n==4):
        TeamA=[]
        TeamB=[]
        TeamC=[]
        TeamD=[]
        if(len(players))<4:
            print("Please ,Enter at least 4 players")
        else:
            while(len(players))>0:
                playerA=choice(players)
                TeamA.append(playerA)
                players.remove(playerA)
                if players==[]:
                    break
                playerB=choice(players)
                TeamB.append(playerB)
                players.remove(playerB)
                if players==[]:
                    break
                playerc=choice(players)
                TeamC.append(playerc)
                players.remove(playerc)
                if players==[]:
                    break
                playerD=choice(players)
                TeamD.append(playerD)
                players.remove(playerD) 
                
                
            if(e==1):
                teams=["Horse","Camel","Fox","Jerman Shefered"]
                team1=choice(teams)
                teams.remove(team1)
                team2=choice(teams)
                teams.remove(team2)
                team3=choice(teams)
                teams.remove(team3)
                team4=choice(teams)
                teams.remove(team4)
                print("Here are your teams")
                print(team1,TeamA)
                print(team2,TeamB)
                print(team3,TeamC)
                print(team4,TeamD)
                      
            elif(e==2):
                teams=["Pakistan","India","England","Australia"]
                team1=choice(teams)
                teams.remove(team1)
                team2=choice(teams)
                teams.remove(team2)
                team3=choice(teams)
                teams.remove(team3)
                team4=choice(teams)
                teams.remove(team4)
                print("Here are your teams")
                print(team1,TeamA)
                print(team2,TeamB)
                print(team3,TeamC)
                print(team4,TeamD)
            elif(e==3):
                teams=["ZALMI","GLADIATARS","Qalandars","Karachi Kings"]
                team1=choice(teams)
                teams.remove(team1)
                team2=choice(teams)
                teams.remove(team2)
                team3=choice(teams)
                teams.remove(team3)
                team4=choice(teams)
                teams.remove(team4)
                print("Here are your teams")
                print(team1,TeamA)
                print(team2,TeamB)
                print(team3,TeamC)
                print(team4,TeamD) 
            else:
                print("PLease!,Enter correct match")
                import winsound
                g=1000
                t=1000
                winsound.Beep(g,t)

    else:
        print("Please,Enter correct input")
        import winsound
        g=1000
        t=1000
        winsound.Beep(g,t)
 
   
    n=input("Enter 'RUN' for run again and 'KILL' for quit")
    if(n=='RUN'):
        continue
    elif(n=='KILL'):
        print("OK, I hope,See you in Cinema")
        break
    else:
        print("Enter right choice,Please!")
        break
    import winsound
    g=1000
    t=1000
    winsound.Beep(g,t)


            

            
        
            
            
            
            
            
            
        
            
            
            
