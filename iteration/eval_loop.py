def eval_loop():
    while True:
        cmd = raw_input(">>> ")
        if cmd == 'done':
            break
        elif cmd == '\r':
            continue
        print eval(cmd)

eval_loop()
