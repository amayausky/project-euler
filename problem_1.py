target = 1000

# works
num_sum = 0
for i in range(1, target):
    if i % 3 == 0 or i % 5 == 0:
        num_sum += i
print num_sum

# better
print sum([i for i in range(1, target) if i % 3 == 0 or i % 5 == 0])

# best
quick_sum = lambda n, p: n*(p*(p + 1))/2
print quick_sum(3, target/3) + quick_sum(5, target/5) - quick_sum(15, target/15)