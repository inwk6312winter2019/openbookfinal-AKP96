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
