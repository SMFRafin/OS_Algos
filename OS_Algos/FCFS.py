class Process:
    def __init__(self,processes,bt,at):
        self.processes=processes
        self.bt=bt
        self.at=at
    
def getAT(proc):
    return proc.at

def FCFS(process):
    process.sort(key=getAT)
    wt=[0]
    total=0
    for i in range(1,len(process)):
        wt.append(wt[i-1]+process[i-1].bt)
        total+=wt[i]
    avgwt=total/len(process)
    return (wt,avgwt)

def display_gantt_chart(processes):
    print("\t\\Gantt Chart\\")
    print("\t-------------")
    print("-", end="")
    for p in processes:
        process_name_length = len(p.processes)
        for _ in range(p.bt):
            print("--", end="")
        for _ in range(process_name_length):
            print("-", end="")
        print("-", end="")
    print("\n|", end="")
    for p in processes:
        for _ in range(p.bt):
            print(" ", end="")
        print(p.processes, end="")
        for _ in range(p.bt):
            print(" ", end="")
        print("|", end="")
    print("\n+", end="")
    for p in processes:
        process_name_length = len(p.processes)
        for _ in range(p.bt):
            print("--", end="")
        for _ in range(process_name_length):
            print("-", end="")
        print("+", end="")
    print()

def run():
    n=int(input("Enter the number of processes: "))
    pc=[]
    for i in range(n):
        processes=input("Enter PID: ")
        bt=int(input(f"Enter Burst time for {processes}: "))
        at=int(input(f"Enter Arrival Time for {processes}: "))
        pc.append(Process(processes,bt,at))
    wt,avg=(FCFS(pc))
    print(f"{'PID':<10}{'BT':<15}{'WT':<15}")
    for i in range(len(pc)):
        print(f"{pc[i].processes:<10}{pc[i].bt:<15}{wt[i]:<15}")
    print(f"Avg_WT using FCFS: {avg}")
    display_gantt_chart(pc)
