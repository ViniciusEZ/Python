# Write a function called sumIntervals/sum_intervals() that accepts an
# array of intervals, and returns the sum of all the interval lengths.
# Overlapping intervals should only be counted once.

def sum_of_intervals(intervals):
    sum_interval = map(lambda x:[y for y in range(x[0], x[-1])], intervals)
    return list(sum_interval)

print(sum_of_intervals([(1,5)]))

# Unfinished