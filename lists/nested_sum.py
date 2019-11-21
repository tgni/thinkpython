#import types
def nested_sum(__list):
    total = 0
    for i in __list:
        #if type(i) is types.ListType:
        if isinstance(i, list):
            total += nested_sum(i)
        else:
            total += i
    return total

t = [1, 2, 3, [4, 5]]
print nested_sum(t)
