class Process:
    def __init__(self,processes,bt,order):
        self.processes=processes
        self.bt=bt
        self.order=order
    
def getOrder(proc):
    return proc.order

def FCFS(process):
    process.sort(key=getOrder)
    wt=[0]
    total=0
    for i in range(1,len(process)):
        wt.append(wt[i-1]+process[i-1].bt)
        total+=wt[i]
    avgwt=total/len(process)
    return (wt,avgwt)

if __name__=='__main__':
    n=int(input("Enter the number of processes: "))
    pc=[]
    for i in range(n):
        processes=input("Enter PID: ")
        bt=int(input(f"Enter Burst time for {processes}: "))
        order=int(input(f"Enter order for {processes}: "))
        pc.append(Process(processes,bt,order))
    wt,avg=(FCFS(pc))
    print(f"{'PID':<10}{'BT':<15}{'WT':<15}")
    for i in range(len(pc)):
        print(f"{pc[i].processes:<10}{pc[i].bt:<15}{wt[i]:<15}")
    print(f"Avg_WT:{avg}")