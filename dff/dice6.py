def amount():
    a = '106'
    b = '15'
    if len(a) > len(b):
        for v in range(len(a) - len(b)):
            b = '0' + b

    if len(a) < len(b):
        for v in range(len(b) - len(a)):
            a = '0' + a

    print(a)
    print(b)
    result = ''
    amount_fn_sn = 0
    for i in range(len(a)):
        amount_fn_sn = int(a[i]) + int(b[i])
        if amount_fn_sn >= 10:
            list_result = list(result)
            list_result[i-1] = str(int(list_result[i-1]) + amount_fn_sn // 10)
            list_result.append(str(amount_fn_sn % 10))
            result = ''.join(list_result)
        else:
            result = result + str(amount_fn_sn)
    print(result)


amount()
