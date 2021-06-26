def valida_int(num):
    try:
        int(num)
    except:
        return 0
    else:
        return int(num)
