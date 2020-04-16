"""
you are given  queries. Each query is of the form two integers described below:
-1 x : Insert x in your data structure.
-2 y : Delete one occurence of y from your data structure, if present.
-3 z : Check if any integer is present whose frequency is exactly z. If yes, print 1 else 0.
"""

from collections import defaultdict

def freqQuery(queries): 
    val_counts = defaultdict(int)
    freq_counts = defaultdict(int)
    answers = []
    for i, j in queries:
        print(freq_counts)
        if i == 1:
        # O(1)
            if j in val_counts:
                # decrement the value's old count 
                if freq_counts[val_counts[j]] > 0:
                    freq_counts[val_counts[j]] -= 1
                val_counts[j] += 1
                # increment the frequency in freq_counts 
                freq_counts[val_counts[j]] += 1
            else:
                val_counts[j] = 1
                if freq_counts[val_counts[j]]:
                    freq_counts[val_counts[j]] += 1
                else:
                    freq_counts[val_counts[j]] = 1
        if i == 2:
            # O(1)
            # check that the value exists in val_counts
            if val_counts[j]:
                # decrement the old frequency count 
                freq_counts[val_counts[j]] -= 1
                val_counts[j] -= 1
                # increment the new frequency count 
                freq_counts[val_counts[j]] += 1
        if i == 3:
            # O(n) linear in the number of key, value pairs 
            # aim for a O(1) runtime 
            # somehow check j in an object 
            # instead of having the j values be checked against 
            # the values in an object, it would be much faster 
            # to check the j values against the keys of an object
            if j in freq_counts and freq_counts[j] > 0:
                answers.append(1)
            else:
                answers.append(0)
        
    return answers


if __name__ == '__main__':
    print(freqQuery([(1,1), (2,2), (3,2), (1,1), (1,1),(2,1),(3,2)]))
