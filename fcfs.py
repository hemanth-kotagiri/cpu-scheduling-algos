class FCFS:
    """ A class to implement FCFS Algorithm for Process Scheduling """

    times = []

    def __init__(self):
        n = int(input("Enter number of processess: "))

        print("Arrival Time | Burst Time")
        while n:
            self.times.append(list(map(int, input().split())))
            n -= 1

    def showProcessArrivalAndBursts(self):
        for i in range(len(self.times)):
            print(
                f"Proess {i + 1} Arrived At : {self.times[i][0]}  With Burst time : {self.times[i][1]}")

    def firstComeFirstServe(self):

        # Sorting the processess by the arrival time
        temp = sorted(self.times, key=lambda x: x[0])

        completionTimes = []
        turnAroundTimes = []
        waitingTimes = []

        for process in temp:

            # completion times for the current process
            if not completionTimes:
                completionTimes.append(sum(process))
            else:
                currentCompletion = completionTimes[-1] + process[1]

                # Handling the case when the cpu is idle
                idlePeriod = process[0] - completionTimes[-1]
                if idlePeriod > 0:
                    currentCompletion += idlePeriod

                completionTimes.append(currentCompletion)

            # turn around time: Completing time - Arrival Time
            turnAroundTimes.append(completionTimes[-1] - process[0])

            # Waiting time: Turn around time - burst time
            waitingTimes.append(turnAroundTimes[-1] - process[1])

        print("PID | CT | TAT | WT")
        id = 1
        for i, j, k in zip(completionTimes, turnAroundTimes, waitingTimes):
            print(f"P{id}  | {i} | {j}  | {k}")
            id += 1

        print(
            f"Average Turn Around Time: {sum(turnAroundTimes)/len(turnAroundTimes)}")
        print(f"Average Waiting Time: {sum(waitingTimes)/len(waitingTimes)}")


demo = FCFS()
demo.firstComeFirstServe()
