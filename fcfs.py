def getProcessArrivalAndBursts():
    n = int(input("Enter number of processess: "))
    times = []

    while n:
        times.append(list(map(int, input().split())))
        n -= 1

    return times


def showProcessArrivalAndBursts(times):
    # print("PROCESS | ARRIVAL TIME | BURST TIME")
    for i in range(len(times)):
        print(f"Proess {i + 1} Arrived At : {times[i][0]}  With Burst time : {times[i][1]}")


def firstComeFirstServe(times):
    dup = sorted(times, key=lambda x:x[0])
    print(dup)
    completionTimes = []
    turnAroundTimes = []
    waitingTimes = []
    for process in dup:

        # completion times for each process

        if not completionTimes:
            completionTimes.append(process[1])
        else: completionTimes.append(completionTimes[-1] + process[1])

        # turn around time: Completing time - Arrival Time

        turnAroundTimes.append(completionTimes[-1] - process[0])
    
        # Waiting time
        waitingTimes.append(turnAroundTimes[-1] - process[1])

    for i, j in zip(completionTimes, turnAroundTimes):
        print(f"Completing Time: {i} and Turn Around time: {j}")
    
    print(f"Avg TAT: {sum(turnAroundTimes)/len(turnAroundTimes)}")
    print(f"Avg WT: {sum(waitingTimes)/len(waitingTimes)}")
    print(f"TATs: {turnAroundTimes}")
    print(f"WTs: {waitingTimes}")





# Get the arrival times, burst times for processess
times = getProcessArrivalAndBursts()

# print("given processess without order")
# showProcessArrivalAndBursts(times)

# Perform the algorithm
firstComeFirstServe(times)
