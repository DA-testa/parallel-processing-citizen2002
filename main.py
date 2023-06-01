def parallel_processing(n, m, data):
    output = []
    check = [0]*n
    num = 0
    for i in range(m):
        t = data[i]
        thread = min(threads, key=lambda x: x[1])  
        output.append((thread[0], thread[1]))  
        threads[threads.index(thread)] = (thread[0], thread[1] + t)  
    return output

def main():
    nr = input()
    nr = nr.split()
    n = int(nr[0])
    m = int(nr[1])
    data = list(map(int, input().split()))
    result = parallel_processing(n,m,data)
    for i, j in result:
        print(i, j)
        
if __name__ == "__main__":
    main()