#Round Robin
class Process:
    def __init__(self,pid,bt,at):
        self.pid=pid
        self.bt=bt
        self.at=at

def RR(process, quantum):
    n=n
    queue=[]
    waiting_time=[0]*n
    remaining_burst_time = [p.bt for p in process]
    time = 0
    completed_processes = 0
    while completed_processes < n:
        for i in range(n):
            if remaining_burst_time[i] > 0 and process[i].at <= time:
                queue.append((process[i], i))

        if not queue:
            time += 1
            continue

        current_process, index = queue.pop(0)
        if remaining_burst_time[index] > quantum:
            time += quantum
            remaining_burst_time[index] -= quantum
        else:
            time += remaining_burst_time[index]
            waiting_time[index] = time - current_process.bt - current_process.at
            remaining_burst_time[index] = 0
            completed_processes += 1

    avg_waiting_time=sum(waiting_time)/n
    return waiting_time,avg_waiting_time
    
def run():
    n=int(input("Enter the number of processes: "))
    quantum=int(input("Enter the time quantum: "))
    pc=[]
    for i in range(n):
        processes=input("Enter PID: ")
        bt=int(input(f"Enter Burst time for {processes}: "))
        at=int(input(f"Enter Arrival time for {processes}: "))
        pc.append(Process(processes,bt,at))
    wt,avg=(RR(pc,quantum))
    print(f"{'PID':<10}{'BT':<15}{'WT':<15}")
    for i in range(len(pc)):
        print(f"{pc[i].pid:<10}{pc[i].bt:<15}{wt[i]:<15}")
    print(f"Avg_WT using RR: {avg}")
    