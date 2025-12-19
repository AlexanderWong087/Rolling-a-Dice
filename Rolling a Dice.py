import random 

scoreA=0 
scoreB=0 
scores=[scoreA,scoreB] 
roll1=0 
roll2=9 

for i in range(5): 
    for j in range(2): 
        roll1=random.randint(1,6) 
        roll2=random.randint(1,6) 
        scores[j]+=roll1+roll2 
        print('Player '+str((j+1))+' rolled '+str(roll1)+' and '+str(roll2)) 
        if roll1==roll2: 
            print('Player '+str((j+1))+' received a bonus 5 points for rollong the two same numbers') 
            scores[j]+=5 

print('Final scores:') 
print('Player 1 has '+str(scores[0])+' points') 
print('Player 2 has '+str(scores[1])+' points') 
