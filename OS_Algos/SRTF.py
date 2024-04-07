#Shortest Remaining Time First
class Process:
    def __init__(self,pid,bt,at):
        self.pid=pid
        self.bt=bt
        self.at=at

def SRTF(processes):
    n=len(processes)
    processes.sort(key=lambda x:x.at)

    wt=[0]*n
    avg_wt=0
    currentTime=0
    remainingTime=[process.bt for process in processes]

    while True:
        done=True
        for i in range(n):
            if remainingTime[i]>0 and processes[i].at<=currentTime:
                done=False
                if remainingTime[i]>1:
                    wt[i]=currentTime
                else:
                    wt[i]=currentTime-processes[i].bt
                currentTime+=1
                remainingTime[i]-=1
        if done:
            break
    for i in range(n):
        avg_wt+=wt[i]

    avg_wt/=n

    return wt,avg_wt

def run():
    n=int(input("Enter the number of processes: "))
    processes=[]
    for i in range(n):
        pid=input("Enter PID: ")
        bt=int(input(f"Enter Burst time for {pid}: "))
        at=int(input(f"Enter Arrival time for {pid}: "))
        processes.append(Process(pid,bt,at))
    wt,avg=(SRTF(processes))
    print(f"{'PID':<10}{'BT':<15}{'WT':<15}")
    for i in range(len(processes)):
        print(f"{processes[i].pid:<10}{processes[i].bt:<15}{wt[i]:<15}")
    print(f"Avg_WT using SRTF: {avg}")

        
