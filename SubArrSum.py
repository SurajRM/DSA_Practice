def subArraySum(arr,n,s):
    for k in range(n):
        for i in range(n - k + 1):
            current_sum = 0
            sub_arr = []
            for j in range(k):
                sub_arr.append(i+j+1)
                current_sum = current_sum + int(arr[i + j])
                if current_sum == s:
                    return [sub_arr[0],sub_arr[-1]]



arr = input("Enter array elements: ").split()
n = len(arr)
s = int(input("\nSum of expected subarray: "))
print(subArraySum(arr,n,s))