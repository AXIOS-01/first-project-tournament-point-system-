#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~password section~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
global Pcount
Pcount = (0) #password counter
def login_func():
    global Pcount
    password = "fanta ft"
    login=input("enter the password: ")
    if Pcount == 2:
        print ("to many password attempts")
        quit()
    elif login != password:
        Pcount= Pcount + 1
        login_func()
    else:
        print("Welcome \n")
login_func()
# the login section allows the user 3 attemptes at entering the password before being closing the program,

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~USER DETAILS SECTION~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
print ("before being allowed to use the program we need to to fill out some details:")
name=input("please enter your full name: \n")
address=input("please enter your address: \n")
email=input("please enter your E-mail address: \n")
company=input("please enter the company: \n")

with open ('final_booking.txt', 'w') as f:
    f.write(name+"\n")
    f.write(address+"\n")
    f.write(email+"\n")

print ("thank you for that information " + name + " from " + company +".")

while True:
    questions=input("""before we continue would you like to read out FAQ about the scoring system?
answer with yes or no: """)
    
    if questions.lower() == "yes":
        with open ('FAQ.txt','r+') as f:
            lines = f.read()
            print (lines)
            break
    elif questions.lower() == "no":
        break
    else:
        print("please enter as required.\n")
        continue

point1=int(input("how many points will first place be awarded? "))
point2=int(input("how many points will second place be awarded? "))
point3=int(input("how many points will third place be awarded? "))
point4=int(input("how many points will fourth place be awarded? "))

global position 

position={
    1:point1,
    2:point2,
    3:point3,
    4:point4,
    "NA":0
}
print (position)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~THE TEAMS SECTION~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

global team_temp
global player_temp
team_temp = ()
player_temp = []

print("now you will enter the teams names and players starting with team 1. ")

def team_names():
    global team_temp
    team_temp=input("enter the team's name: \n")
    
def team_players():
    count=5
    global player_temp
    while True:
        if count != 0:
            player_temp = input("enter a players name: ")
            count = count-1
        else:
            break

team_names()
team1=(team_temp)
team1_r=str(team1) # the r is for real, their real true variable name
with open ('TEAM_1.txt', 'a') as f:
    f.write(team1+"\n")

team_players()
players1=(player_temp)
with open ('TEAM_1.txt', 'a') as f:
    f.write(players1+"\n")
###############################################
team_names()
team2=(team_temp)
team2_r=str(team2)
with open ('TEAM_2.txt', 'a') as f:
    f.write(team2+"\n")

team_players()
players2=(player_temp)
with open ('TEAM_2.txt', 'a') as f:
    f.write(players2+"\n")
###############################################
team_names()
team3=(team_temp)
team3_r=str(team3)
with open ('TEAM_3.txt', 'a') as f:
    f.write(team3+"\n")

team_players()
players3=(player_temp)
with open ('TEAM_3.txt', 'a') as f:
    f.write(players3+"\n")
####################################################
team_names()
team4=(team_temp)
team4_r=str(team4)
with open ('TEAM_4.txt', 'a') as f:
    f.write(team4+"\n")

team_players()
players4=(player_temp)
with open ('TEAM_4.txt', 'a') as f:
    f.write(players4+"\n")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~THE POINTS SECTION~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
global team1_p
global team2_p
global team3_p
global team4_p

global team1_tot
global team2_tot
global team3_tot
global team4_tot

team1_tot=int()
team2_tot=int()
team3_tot=int()
team4_tot=int()

def team_placement():
    global team1_p
    global team2_p
    global team3_p
    global team4_p
    global team1_tot
    global team2_tot
    global team3_tot
    global team4_tot

    print("enter the postions that the teams placed during the event with: 1, 2, 3, 4 OR NA: ")
    team1_p=int(input(team1_r+"- what did they place?"))
    team2_p=int(input(team2_r+"- what did they place?"))
    team3_p=int(input(team3_r+"- what did they place?"))
    team4_p=int(input(team4_r+"- what did they place?"))

    team1_tot=team1_tot+position[team1_p]
    team2_tot=team2_tot+position[team2_p]
    team3_tot=team3_tot+position[team3_p]
    team4_tot=team4_tot+position[team4_p]

    print("The current standings are:")
    print (team1_r+" with ")
    print(team1_tot)
    print (team2_r+" with ")
    print(team2_tot)
    print (team3_r+" with ")
    print(team3_tot)
    print (team4_r+" with ")
    print(team4_tot)

while True:
    sport_ac1=input("""please choose between a sporting event or an academic event,
with S and A respectively, if all events are done enter F """)
    if sport_ac1.upper()== "S":
        print ("thank you for selecting a sporting event")
        print ("the event is basketball match. ")
        print ("if thats already completed, then a vollyball game")
        print ("if thats already completed, then a dodgeball game")
        print ("if thats already completed, then a football match")
        print ("if all sporting events are concluded enter NA when doing team placements")
        team_placement()
        continue
    elif sport_ac1.upper()=="A":
        print ("thank you for selecting an academic event")
        team_placement()
        continue
    elif sport_ac1 == "F":
        break
    else:
        print("please select one of the options")
        continue

print("The final standings are:")
print (team1_r+" with ")
print(team1_tot)
print (team2_r+" with ")
print(team2_tot)
print (team3_r+" with ")
print(team3_tot)
print (team4_r+" with ")
print(team4_tot)