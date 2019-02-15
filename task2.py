def my_log():
    file = open("access.log","r")
    fget = open("get.log","w")
    fpost = open("post.log","w")
    fput = open("put.log","w")
    fdelete = open("delete.log","w")
    for line in file:
        if "GET /" in file:
            fget.write(line)
        elif "POST /" in file:
            fpost.write(line)
        elif "PUT /" in file:
            fput.write(line)
        else:
            fdelete.write(line)


print(my_log())




import operator

def topipaddress():
    d = dict()
    fopen = open("access.log","r")
    for line in fopen:
        if "GET /" in line or "POST /" in line:
            ip = line.split('-')[0]
            if ip not in d:
                d[ip] = 1
            else:
                d[ip] += 1
    new = sorted(d, key=d.get, reverse=True)[:20]
    return new


print(topipaddress())
