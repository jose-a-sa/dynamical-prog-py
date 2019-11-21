import math

def lcm(a,b):
  return (a*b)//math.gcd(a,b)

def min_coins(cents,coins=[25,15,1]):
  cutoff=1
  for c in coins:
    cutoff = lcm(cutoff,c)
  
  n_t = (cents // cutoff) * (cutoff // max(coins))
  cents %= cutoff
  
  dp = [math.inf] *(cents+1)
  dp[0] = 0
  for i in range(1,cents+1):
    for c in coins:
      if i>=c:
        dp[i] = min(dp[i], dp[i-c] + 1)
  print(dp)
  return dp[cents]+n_t 

print(min_coins(74))