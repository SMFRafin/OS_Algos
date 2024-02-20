class Process:
    def __init__(self,pid,bt,priority,at):
        self.pid=pid
        self.bt=bt
        self.priority=priority
        self.at=at

def PrioSche(processes):
    processes.sort(key=lambda x:(x.at,x.priority))

    n=len(processes)
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

if __name__=="__main__":
    n=int(input("Enter number of process: "))
    processes=[]
    for i in range(n):
        pid=input("Enter the PID: ")
        bt=int(input(f"Enter the bust time for {pid}: "))
        priority=int(input(f"Enter the priority for {pid}: "))
        at=int(input(f"Enter the arrival time for {pid}: "))
        processes.append(Process(pid,bt,priority,at))
    wt, avg = PrioSche(processes)

    print(f"{'PID':<10}{'BT':<15}{'WT':<15}")
    for i in range(len(processes)):
        print(f"{processes[i].pid:<10}{processes[i].bt:<15}{wt[i]:<15}")

    print(f"Avg_WT: {avg}")
