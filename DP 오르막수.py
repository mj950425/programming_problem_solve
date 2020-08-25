import sys
N = int(sys.stdin.readline())
nums = [1] * 10
mod = 10007
for _ in range(N-1):
    for i in range(1, 10):
        nums[i] = (nums[i] + nums[i-1]) % mod

sys.stdout.write(str(sum(nums) % mod))

"""
N=int(input())
buf=10+N-1
m=10+N-1
for i in range(1,N):
    m=m*(buf-i)/(i+1)
print(int(m)%10007)
    
"""