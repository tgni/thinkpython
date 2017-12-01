def do_twice(f, obj):
    f(obj)
    f(obj)

def print_spam(obj):
    print obj

do_twice(print_spam, 'spam')
