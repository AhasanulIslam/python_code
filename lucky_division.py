n = int(input())
while(n):
    if ((n % 4) == 0)or((n % 7) == 0)or((n % 47) == 0)or((n % 74) == 0)or((n % 474) == 0)or((n % 447) == 0)or((n % 774) == 0)or((n % 777) == 0)or((n % 444) == 0)or((n % 44) == 0)or((n % 77) == 0)or((n % 477) == 0):
        print("YES")
        break
    else:
        print("NO")
        break
        n = 0


