#!/usr/bin/python3
def eval_loop():
    while True:
        cmd = input(">>> ")
        if cmd == 'done':
            break
        elif cmd == '\r':
            continue
        print (eval(cmd))

eval_loop()
