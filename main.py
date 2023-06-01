import math

def parallel_processing(a, b, data):
    output = []
    check = [0]*b
    number = 0
    for c in range(math.ceil(b/a):
        for i in range(a:
            output.append((i, check[i]))
            check[i]+=data[number]
            number+=1
            if number>=b:
                break
    return output

def main():

    num = input()
    num = num.split()
    #a- thread skaits
    #b- job skaits
    a= int(num[0])
    b= int(num[0])
    data = list(map(int, input().split()))
    result = parallel_processing(n,m,data)

    for i, j in result:
        print(i, j)

if __name__ == "__main__":
    main()
