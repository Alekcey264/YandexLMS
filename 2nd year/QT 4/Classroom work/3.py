def reverse():
    with open('Classroom work/input.dat', 'rb') as f:
        lines = f.readlines()
        if lines:
            for line in lines[::-1]:
                with open('Classroom work/output.dat', 'ab') as sf:
                    sf.write(line[::-1])

reverse()