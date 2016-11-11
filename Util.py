def countLengthRow(rows=[],length=1):
    count = 0
    for row in rows:
        if(len(row) == length):
            count = count + 1
    return count
