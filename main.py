index = 0
datas = []

def run(targetString, endCharacter, startIndexOffset, endIndexOffset, isAddingLink):
    global datas, index

    targetStringProgression = 0
    isSearchingForDataEndCharacter = False
    startIndex = 0

    gap = ""
    with open("input.txt", encoding="utf-8") as file:
        for line in file:
            for charIndexInLine in range(0, len(line)):
                if(isSearchingForDataEndCharacter):
                    if(line[charIndexInLine] == endCharacter):
                        if(isAddingLink == False):
                            datas.append(line[startIndex + startIndexOffset:charIndexInLine + endIndexOffset:1])
                        else:
                            gap = ""
                            for i in range(len(datas[index]), 30):
                                gap = gap + " "
                            datas[index] = datas[index] + gap + "Link: https://www.youtube.com/" + line[startIndex + startIndexOffset:charIndexInLine + endIndexOffset:1]
                            index += 1
                        isSearchingForDataEndCharacter = False
                    continue

                if(line[charIndexInLine] == targetString[targetStringProgression]):
                    #print(targetStringProgression)
                    targetStringProgression += 1
                    if(targetStringProgression == len(targetString) - 1):
                        isSearchingForDataEndCharacter = True
                        startIndex = charIndexInLine
                    continue
                
                targetStringProgression = 0

run("<span id=\"title\" class=\"style-scope ytd-grid-channel-renderer\">", "<", 2, 0, False)
run("<a id=\"channel-info\" class=\"yt-simple-endpoint style-scope ytd-grid-channel-renderer\" href=\"", ">", 2, -1, True)
with open("result.txt", encoding="utf-8", mode = "a") as file:
    for channel in datas:
        file.write(channel + "\n")