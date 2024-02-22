class Process:
    def __init__(self,pid,bt,priority):
        self.pid=pid
        self.bt=bt
        self.priority=priority

def getPriority(process):
    return process.priority

def PrioSche(process):
    process.sort(key=getPriority)
    wt=[0]
    total=0
    for i in range(1,len(process)):
        wt.append(wt[i-1]+process[i-1].bt)
        total+=wt[i]
    avgt=total/len(process)
    return (wt,avgt)

def run():
    n=int(input("Enter the number of processes: "))
    processes=[]
    for i in range(n):
        pid=input("Enter PID: ")
        bt=int(input(f"Enter Burst time for {pid}: "))
        priority=int(input(f"Enter priority for {pid}: "))
        processes.append(Process(pid,bt,priority))
    wt,avg=(PrioSche(processes))
    print(f"{'PID':<10}{'BT':<15}{'WT':<15}")
    for i in range(len(processes)):
        print(f"{processes[i].pid:<10}{processes[i].bt:<15}{wt[i]:<15}")
    print(f"Avg_WT using PSNP: {avg}")
