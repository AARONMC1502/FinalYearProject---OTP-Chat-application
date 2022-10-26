def usedPad(numbersUsed):
    with open("pad.txt") as file:
        pad = file.read()

    """
    
    because some utf-8 characters can use up to 4 bytes
    we have to see how many chars in pad were used by taking the
    number of binary bits used and dividing by 8(no bits in byte)
    this can result in float numbers so result is rounded up
    
    """

    numbersUsed = round(numbersUsed / 8)

    # removes chars in pad
    pad = pad[numbersUsed:]

    with open("pad.txt", "w") as newFile:
        newFile.write(str(pad))
