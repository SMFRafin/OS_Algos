import FCFS,PrioritySchedulingNP,PrioritySchedulingPremptive,SJF,RR

def main():
    while(True):
        print("1. Memory Management")
        print("2. CPU Scheduling")
        print("3. Exit")
        ch=input("Enter your choice: ")
        if ch=="1":
            print("Not yet Implemented")
        
        if ch=='2':
            while True:
                print("1. FCFS")
                print("2. SJF")
                print("3. SRTF")
                print("4. Priority Scheduling Non-Premtive")
                print("5. Priority Scheduling Premtive")
                print("6. Round Robin")
                print("7. Go to Main Menu")
                ch1=input("Enter scheduling choice: ")
                
                if ch1=="1":
                    print("For FCFS: ")
                    FCFS.run()
                if ch1=="2":
                    SJF.run()
                if ch1=="3":
                    print("Not yet Implemented")
                if ch1=="4":
                    print("For PSNP: ")
                    PrioritySchedulingNP.run()
                if ch1=="5":
                    print("For PSP")
                    PrioritySchedulingPremptive.run()
                if ch1=="6":
                    print("For RR: ")
                    RR.run()
                if ch1=="7":
                    break
                
        if ch=="3":
            break

        
    
if __name__=="__main__":
    main()