burstT = []
waitingT = []
turn_aroundT = []
avg_wt = 0
avg_tat = 0
print("Enter number of processes: ")
n = int(input())
print('Enter burst time for processes: ')
burstT = list(map(int, input().split()))
waitingT.insert(0, 0)
turn_aroundT.insert(0, burstT[0])

for i in range(1, len(burstT)):
    waitingT.insert(i, waitingT[i-1] + burstT[i-1])
    turn_aroundT.insert(i, waitingT[i] + burstT[i])
    avg_wt = avg_wt + waitingT[i]
    avg_tat = avg_tat + turn_aroundT[i]
avg_wt = float(avg_wt)/n
avg_tat = float(avg_tat)/n

print("Process\t  Burst Time\t  Waiting Time\t  Turn Around Time")
for i in range(0, len(burstT)):
    print(str(i)+"\t\t\t"+str(burstT[i])+"\t\t\t\t"+str(waitingT[i])+"\t\t\t\t"+str(turn_aroundT[i]))
    print("\n")
print("Average waiting time is:  " + str(avg_wt))
print("Average Turn around time is:  " + str(avg_tat))




