def boardgenerator(boardsize=8):
    board = []
    for i in range (boardsize):
        temprow = []
        for j in range(boardsize):
            temprow.append("0")
        board.append(temprow)
    return board

#print(board)
#print(boardgenerator())
"""
schaakpositienu = [
    [57,67,77,87,96,78,68,58],
    [49,50,51,52,53,54,55,56],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [1,2,3,4,5,6,7,8],
    [9,19,29,39,48,30,20,10]]
    """

"""
0xx = leeg
1xx = wit
2xx = zwart
x1x = pion
x2x = toren
x3x = paard
x4x =  bishop
x5x = koningin
x6x = koning
laatste x --> zelfde stuk
"""
stuktype={"pion":"a",
             "toren":"b",
             "paard":"c",
             "bishop":"d",
             "koningin":"e",
             "koning":"f"}
#lijstdingske
#print(stuknummers.get("pion"))
stukkenvoorkomen={ #stukkenmethoeveelkeerzevoorkomenal
    "1a":0, #witte pion komt 0 keer voor in het begin
    "1b":0,
    "1c":0,
    "1d":0,
    "1e":0,
    "1f":0,
    "2a":0,
    "2b":0,
    "2c":0,
    "2d":0,
    "2e":0,
    "2f":0
}
def default8():
    boardsize = 8
    board = boardgenerator(boardsize)
    offset = int((boardsize-8)/2)
    zwart = "2"
    wit = "1"
    back_row = ["toren", "paard", "bishop", "koningin", "koning", "bishop", "paard" ,"toren"]
    for i in range(boardsize):
        stukkenvoorkomen["2a"] = stukkenvoorkomen.get("2a")+1
        board[1][i] = f"{zwart}{stuktype.get("pion")}{stukkenvoorkomen["2a"]}"

    for i in range(boardsize):
        stukkenvoorkomen["1a"] = stukkenvoorkomen.get("1a")+1
        board[6][i] = f"{wit}{stuktype.get("pion")}{stukkenvoorkomen["1a"]}"

    for i in range(0, len(back_row)):
        stukkenvoorkomen[zwart + stuktype.get(back_row[i])] = stukkenvoorkomen.get(zwart + stuktype.get(back_row[i])) + 1
        board[0][i] = f"{zwart + stuktype.get(back_row[i]) + str(stukkenvoorkomen.get(zwart + stuktype.get(back_row[i])))}"


    for i in range(0, len(back_row)):
        stukkenvoorkomen[wit + stuktype.get(back_row[i])] = stukkenvoorkomen.get(wit + stuktype.get(back_row[i])) + 1
        board[7][i] = f"{wit + stuktype.get(back_row[i]) + str(stukkenvoorkomen.get(wit + stuktype.get(back_row[i])))}"

    """
    #generatie toren links
    board[0][0] = f"{zwart + stuktype.get("toren") + str(stukkenvoorkomen.get(zwart + stuktype.get("toren"))+1)}"
    stukkenvoorkomen[f"{zwart + stuktype.get("toren")}"] = stukkenvoorkomen.get(f"{zwart + stuktype.get("toren")}")+1

    #generatie toren rechts
    print(f"{zwart + stuktype.get("toren")}")
    board[0][-1] = f"{zwart + stuktype.get("toren") + str(stukkenvoorkomen.get(zwart + stuktype.get("toren"))+1)}"
    stukkenvoorkomen[f"{zwart + stuktype.get("toren")}"] = stukkenvoorkomen.get(f"{zwart + stuktype.get("toren")}")+1

    # generatie paard links
    board[0][1] = f"{zwart + stuktype.get("paard") + str(stukkenvoorkomen.get(zwart + stuktype.get("paard")) + 1)}"
    stukkenvoorkomen[f"{zwart + stuktype.get("paard")}"] = stukkenvoorkomen.get(f"{zwart + stuktype.get("paard")}") + 1

    # generatie paard rechts
    board[0][-2] = f"{zwart + stuktype.get("paard") + str(stukkenvoorkomen.get(zwart + stuktype.get("paard")) + 1)}"
    stukkenvoorkomen[f"{zwart + stuktype.get("paard")}"] = stukkenvoorkomen.get(f"{zwart + stuktype.get("paard")}") + 1

    # generatie bishop links
    board[0][2] = f"{zwart + stuktype.get("paard") + str(stukkenvoorkomen.get(zwart + stuktype.get("paard")) + 1)}"
    stukkenvoorkomen[f"{zwart + stuktype.get("paard")}"] = stukkenvoorkomen.get(f"{zwart + stuktype.get("paard")}") + 1

    # generatie bishop rechts
    board[0][-3] = f"{zwart + stuktype.get("paard") + str(stukkenvoorkomen.get(zwart + stuktype.get("paard")) + 1)}"
    stukkenvoorkomen[f"{zwart + stuktype.get("paard")}"] = stukkenvoorkomen.get(f"{zwart + stuktype.get("paard")}") + 1
        """





    for i in board:
        print(i)


if True:
    default8()
else:
    default8(16)
    print(stukkenvoorkomen)
"""for i in range(8):
    print(f"3{i}")"""