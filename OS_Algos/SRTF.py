#SRTF
class Process:
    def __init__(self, pid, bt, at):
        self.pid = pid
        self.bt = bt
        self.at = at

def SRTF(processes):
    processes.sort(key=lambda x: x.at)

    n=len(processes)
    wt=[0] * n 
    rt=[proc.bt for proc in processes] 
    complete=0
    t=0
    minm=float('inf')
    short=None
    check=False
   
    while complete != n:
        for j in range(n):
            if processes[j].at <= t and rt[j] < minm and rt[j] > 0:
                minm = rt[j]
                short = j
                check = True
        if check is False:
            t += 1
            continue

        rt[short] -= 1

        minm = rt[short]
        if minm == 0:
            minm = float('inf')

        if rt[short] == 0:
            complete += 1
            check = False
            fint = t + 1
            wt[short] = fint - processes[short].bt - processes[short].at
            if wt[short] < 0:
                wt[short] = 0
        t += 1

    avg_wt = sum(wt) / n
    return wt, avg_wt

def run():
    n = int(input("Enter the number of processes: "))
    processes = []
    for i in range(n):
        pid = input(f"Enter Process ID for process {i + 1}: ")
        bt = int(input(f"Enter Burst time for process {pid}: "))
        at = int(input(f"Enter Arrival Time for process {pid}: "))
        processes.append(Process(pid, bt, at))

    wt, avg_wt = SRTF(processes)
    print(f"{'PID':<10}{'BT':<15}{'WT':<15}")
    for i in range(len(processes)):
        print(f"{processes[i].pid:<10}{processes[i].bt:<15}{wt[i]:<15}")
    print(f"Average Waiting Time using SRTF: {avg_wt:.2f}")
