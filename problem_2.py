# works
def fibonacci_sum(limit, total=0, current=1, previous=0):
    next_num = current + previous
    if limit >= next_num:
        if next_num % 2 == 0:
            total += next_num
        return fibonacci_sum(limit, total, next_num, current)
    return total


# better, only calculates even fibonacci numbers
# based on first number always increasing by x + 2y
# and second increasing by 2x + 3y
def better_fibonacci_sum(limit, total=0, x=1, y=1):
    next_num = x + y
    if limit >= next_num:
        total += next_num
        x, y = x + 2*y, 2*x + 3*y
        return better_fibonacci_sum(limit, total, x, y)
    return total

print fibonacci_sum(4000000)
print better_fibonacci_sum(4000000)