
matrix = [[0 for j in range(5)] for i in range(5)]

# set the lower triangle half of the matrix to zero
for i in range(len(matrix)):
    for j in range(i):
        matrix[i][j] = 0
def Print_Matrix_Half():
    print("       ---+---+---+---+---+")
    print("        2 + 3 + 4 + 5 + 6 |")
    print("       ---+---+---+---+---+")
    print("")
    # print the upper triangle half of the matrix as a box

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j == 0:
                print("|",i+1,"|  ", end=" ")
            if j >= i:
                print(matrix[i][j], end=" ")
            else:
                print(" ", end=" ")
            print("|", end=" ")
            if j == len(matrix[i]) - 1:
                print("")
        print("+---+      ---+---+---+---+")

def Print_Matrix_Full():
# print all the matrix     
    print("       ---+---+---+---+---+")
    print("        2 + 3 + 4 + 5 + 6 |")
    print("       ---+---+---+---+---+")
    print("")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j == 0:
                print("|",i+1,"|  ", end=" ")
            print(matrix[i][j],end=" ")
            print("|",end=" ")
        if j == len(matrix[i]) - 1:
            print("")
            
            
        print("+---+  ---+---+---+---+---+")

def Candidate_List_Generator(i):
    if i==0:
        Candidate_List =     [[[5,4],5],  # Best
                             [[3,6], 3],
                             [[3,2], 1],
                             [[4,1],-4]]
    if i==1:
        Candidate_List =     [[[3,1],3], # Best
                             [[3,2], 1],
                             [[5,1],-1],
                             [[6,2],-5]]
    if i==2:
        Candidate_List =     [[[1,3],-3], # Best But Tabu
                             [[4,2], -4], # Next Best
                             [[4,5], -6],
                             [[6,2], -7]]
    if i==3:
        Candidate_List =     [[[1,3],5],  # Best but Tabu but Better than Best_Obj_Func
                             [[2,5], 1],
                             [[1,4],-1],
                             [[6,4],-3]]
    if i==4:
        Candidate_List =     [
                             [[5,1], 0],
                             [[3,6],-1],
                             [[1,4],-2],
                             [[3,1],-5]]


    return Candidate_List


def Reduce_Matrix():
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (matrix[i][j]!=0):
                matrix[i][j] = matrix[i][j] - 1      # We Reduce The Number in all indexes By 1 => -1
                

def Swap(First_Number,Second_Number):
    for i in range(len(Init_Solution)):
        if (Init_Solution[i] == First_Number):
            Pos_0 = i
        elif(Init_Solution[i] == Second_Number):
            Pos_1 = i
        
    Init_Solution[Pos_0] , Init_Solution[Pos_1] = Init_Solution[Pos_1] , Init_Solution[Pos_0]
    

def Pick_Our_Best_Candidate(i,j):
    global Best_Pick
    global Added_Value
    global Index_Left
    global Index_Right
    
    Best_Pick = Candidate_List_Generator(i)[j][0]       # The First one in the candidate list generator has the highest value , therefore is the best pick
    Index_Right = Candidate_List_Generator(i)[j][0][0]        # Index 1   The Index on the Left 
    Index_Left = Candidate_List_Generator(i)[j][0][1]        # Index 0   The index Above
    
    if (Index_Left>Index_Right):                                # If the one on the left is larger than the one on the right we swap so we dont have bugs later on , exp : (1,3) Left = 1 | Right = 3 / So (3,1) should also be Left = 1 | Right = 3
        Index_Left , Index_Right = Index_Right , Index_Left
  
    
    Added_Value = Candidate_List_Generator(i)[j][1]        # our best value 
    
    print("Best Pick: ", Best_Pick)
    
    # Fix the Best Pick Positioning 
    if (Best_Pick[0] > Best_Pick[1]):
        Best_Pick[0],Best_Pick[1] = Best_Pick[1] , Best_Pick[0]   #If the first index value is bigger than the second index value then we swap (switch) the values . since that is how it works apparently 
    #print ("Idx_Left: ",Index_Left ,'|', "Idx_Right: ",Index_Right)          #This is here to check which index is which , since it is swaped 
    
    print ("Added_Value: ",Added_Value)

def Check(Iteration,Participant,Obj_Func,Best_Obj_Func):
    for i in range (len(Storage_Unit)):
        if (Best_Pick == Storage_Unit[i]):
            print (" **************** Tabu Found **************")
            if (Obj_Func + Added_Value > Best_Obj_Func):
                print("The Aspiration Criterion is Met!")
                print(Obj_Func ,"+", Added_Value ,">", Best_Obj_Func)
            else: 
                Participant = Participant+1
                Pick_Our_Best_Candidate(Iteration,Participant)      # Picks the Best Next in the candidates 
                Check(Iteration,Participant,Obj_Func,Best_Obj_Func)     # we check again if this best is also in tabu or not

def Check_Life_Period(matrix):
    Expired_List = []
    for i in range (len(Storage_Unit)):
        Left_Index = Storage_Unit[i][0] - 1
        Up_Index = Storage_Unit[i][1] - 2
        
        #print("Left_Index: ",Left_Index)
        #print("Up_Index: ",Up_Index)
        
        if (matrix[Left_Index][Up_Index]==0):
            
            print("Candidate: ",Storage_Unit[i],"Has Expired")  #We Remove The Unit With The Dead Expiration Date
            Expired_List.append(Storage_Unit[i])    # We Fill The Expired Values in this List .
            
    #print("Expired_List: ",Expired_List)
    
    
    for x in range (len(Expired_List)):             #Then we simply remove the expired values from our Storage_Unit
        Storage_Unit.remove(Expired_List[x])    
    Expired_List.clear()                            #Then We Clear it for future use
        
def Tabu_Search(Obj_Func , Init_Solution):
    Full_Candidates_Size = 4
    Best_Obj_Func = Init_Obj_Func
    for i in range(Full_Candidates_Size):
       
        print("________________________________ Iteration",i+1,"__________________________________________")
        # -------------------------------------- Prep --------------------------------------
    
        Participant=0
        Pick_Our_Best_Candidate(i,Participant)      # We Pick Our Best Candidate , and we pass through our itteration index (i)  and the position of our best candidate (in theory) so if the first one doesnt workout (tabu) we pass the next one and so on
       
        
        # -------------------------------------------------------------------------------------------
        
        
        # -------------------------------------- Checks --------------------------------------
        # Check if Best Pick is already in tabu stroage or no .  Paritcipant means which row we are on . 
        Check(i,Participant,Obj_Func,Best_Obj_Func)
        
                
        # ---------------------------------- We Fill it With 3 iterations  ----------------------------------
        matrix[Index_Left-1][Index_Right-2] = 3        #We Put the value to 3 iterations in the case of [[[5, 4], 5]] we take (4,5) that's why i removed  -2 we do not take (5,4)
        #matrix[Index_Right-1][Index_Left-2] = 3       # I was trying to fill the other half but there is a bug so its commented don't remove the comment .
        
        #----------------------------------------------------------------------------------------------------
        #---------------------------------- Tabu Storage ----------------------------------------------------
        # we make sure it doesn't already exist , cuz of the aspiration criteria
        already_exists_in_storage = False
        for x in range (len(Storage_Unit)):
            if (Best_Pick == Storage_Unit[x]):
                already_exists_in_storage = True
                print("Alredy Exists In Storage After Aspiration Criteria Is Met , No Need For Doubles")
        
        if (already_exists_in_storage == False):
            Storage_Unit.append(Best_Pick)      # then we add it to our tabu list
        print("...............................................")
        print("Storage_Unit: ",Storage_Unit)
        print("...............................................")
        #----------------------------------------------------------------------------------------------------
        print(Obj_Func , "+" , Added_Value , "=" , Obj_Func + Added_Value)
        Obj_Func = Obj_Func + Added_Value
        if (Obj_Func > Best_Obj_Func):
            Best_Obj_Func = Obj_Func
        print("Obj_Func = ",Obj_Func)                               #Prints Our Obj_Func 
        
        Swap(Index_Left,Index_Right)
        print(Init_Solution)                                        #Prints Our List
        
        print("Best Obj_Func So Far: ",Best_Obj_Func)
        Print_Matrix_Half()
        Reduce_Matrix()
        # We Check to see if any Candidate in the tabu list has a dead life period in the matrix .
        Check_Life_Period(matrix)  # Index_Left-1 and Index_Right-2  so the index would be spot on as an idex that starts from 0 , rather from 1 . so it matches the Compiled matrix 
        
        
Storage_Unit = []
Init_Solution = [5,3,4,6,1,2]
Init_Obj_Func = 20

print(" ############################ Initialization  ############################ ")
print("Init_Solution : ", Init_Solution)
print("Init_Obj_Func : ", Init_Obj_Func)
Print_Matrix_Half()
print(" ######################################################################### ")
Tabu_Search(Init_Obj_Func , Init_Solution)

#Print_Matrix_Half()
#Print_Matrix_Full()