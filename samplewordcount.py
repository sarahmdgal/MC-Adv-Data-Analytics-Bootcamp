from collections import Counter


sampledoc = open(r"wordscount.txt", "r", encoding="utf-8-sig")

wordcount = Counter(sampledoc.read().split())

for item in wordcount.items(): print("{}\t{}".format(*item))
