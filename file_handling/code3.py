r = open(r"file_handling\sample2.txt", 'w')

r.write("helloooooooooooo\n")

r = open(r"file_handling\sample2.txt", 'a')

r.write("hi")

r.close()