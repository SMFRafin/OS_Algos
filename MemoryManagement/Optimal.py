#Optimal Page Replacement Algorithm
def Optimal(pages,capacity,n):
    pages_array=[]
    hits=0
    page_fault=0
    for i in range(n):
        if pages[i] not in pages_array:
            pages_array.append(pages[i])
            page_fault+=1
        else:
            pages_array.remove(pages[i])
            pages_array.append(pages[i])
            hits+=1
    return (page_fault,hits)


def run():
    capacity = int(input("Enter the capacity of page frame: "))
    n = int(input("Enter the number of pages: "))
    pages = list(map(int, input("Enter the pages: ").split()))
    faults,hits=Optimal(pages,capacity,n)
    print("Number of page faults: ", faults)
    print("Number of page hits: ", hits)
