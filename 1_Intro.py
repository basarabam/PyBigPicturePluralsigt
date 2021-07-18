from urllib.request import urlopen
story = urlopen('http://sixty-north.com/c/t.txt')
story_words = []

for line in story:
    line_words = line.decode('utf-8').split() #Decodeing bytes transfered over HTTP
    for word in line_words:
        story_words.append(word)

story.close()

#Bytes transfered over HTTP not strings
print(story_words)


