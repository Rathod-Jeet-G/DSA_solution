def source_to_dest(src,dest):
    print("source:",src,"to destination:",dest)
    if src == dest:
        print("destination is reached")
        return
    source_to_dest(src+1,dest)

print(source_to_dest(1,10))