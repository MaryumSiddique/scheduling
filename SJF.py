burstT = []
waitingT = []
turn_aroundT = []
process = []
avg_wt = 0
avg_tat = 0
n = input("Enter the number of processes: ")
n = int(n)
for i in range(0, n):
    process.insert(i, i+1)
print("Enter burst time for processes: ")
burstT = list(map(int, input().split()))
for i in range(0, len(burstT)-1):
    for j in range(0, len(burstT)-i-1):
        if burstT[j] > burstT[j+1]:
            tmp = burstT[j]
            burstT[j] = burstT[j+1]
            burstT[j+1] = tmp
            tmp = process[j]
            process[j] = process[j+1]
            process[j+1] = tmp
waitingT.insert(0, 0)
turn_aroundT.insert(0, burstT[0])
for i in range(1, len(burstT)):
    waitingT.insert(i, waitingT[i-1] + burstT[i-1])
    turn_aroundT.insert(i, waitingT[i] + burstT[i])
    avg_wt = avg_wt + waitingT[i]
    avg_tat = avg_tat + turn_aroundT[i]
avg_wt = float(avg_wt)/n
avg_tat = float(avg_tat)/n
print("Process\t Burst Time\t Waiting Time\tTurn Around Time ")
for i in range(0, len(burstT)):
    print(str(process[i])+"\t\t\t"+str(burstT[i])+"\t\t\t"+str(waitingT[i])+"\t\t\t"+str(turn_aroundT[i]))
    print("\n")
print("Average waiting time is: "+str(avg_wt))
print("Average turn around time is: "+str(avg_tat))