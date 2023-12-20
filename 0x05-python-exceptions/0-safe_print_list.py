def safe_print_list(my_list=[], x=0):
    xx = 0
    for t in range(x):
        try:
            print("{}".format(my_list[t]), end="")
            xx ++
        except IndexError:
            break
    print("")
    return (xx)
