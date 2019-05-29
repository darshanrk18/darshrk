class Job: 
    def __init__(self, start, finish, weight): 
        self.start  = start 
        self.finish = finish 
        self.weight  = weight
def binarySearch(job, start_index): 
    lo = 0
    hi = start_index - 1
    while lo <= hi: 
        mid = (lo + hi) // 2
        if job[mid].finish <= job[start_index].start: 
            if job[mid + 1].finish <= job[start_index].start: 
                lo = mid + 1
            else: 
                return mid 
        else: 
            hi = mid - 1
    return -1
def schedule(job): 
    job = sorted(job, key = lambda j: j.finish) 
    n = len(job)  
    table = [0 for _ in range(n)] 
    table[0] = job[0].weight; 
    for i in range(1, n): 
        inclProf = job[i].weight 
        l = binarySearch(job, i) 
        if (l != -1): 
            inclProf += table[l]; 
        table[i] = max(inclProf, table[i - 1]) 
  
    return table[n-1] 
n=int(input('Enter the number of jobs\n'))
j=[]
for i in range(n):
    s,f,w=input('enter the start time,finish time and weight of the job\n').split()
    s=int(s)
    f=int(f)
    w=int(w)
    j.append(Job(s,f,w))
print("Optimal profit:"), 
print(schedule(j)) 
    
 
    

