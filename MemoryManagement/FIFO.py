import queue

def FIFO(pages, capacity, n):
    page_q = queue.Queue()
    page_fault = 0
    hits=0
    for i in range(n):
        if page_q.qsize() < capacity:
            if pages[i] not in page_q.queue:
                page_q.put(pages[i])
                page_fault += 1
            else:
                hits+=1
        else:
            if pages[i] not in page_q.queue:
                page_q.get()
                page_q.put(pages[i])
                page_fault += 1
            else:
                hits+=1
    return (page_fault,hits)

def run():
    capacity = int(input("Enter the capacity of page frame: "))
    n = int(input("Enter the number of pages: "))
    pages = list(map(int, input("Enter the pages: ").split()))
    faults,hits=FIFO(pages,capacity,n)
    print("Number of page faults: ", faults)
    print("Number of page hits: ", hits)
