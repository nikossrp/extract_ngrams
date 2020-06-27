def extract_ngrams(text, num):      
    
    text = str(text)        #split work only with strings
    l = []

    #1-gram
    if num == 1:        
        for i in range(len(text.split())):     #range(number of words)
            l.append(text.split()[i])          #make a list with the words
        return l
    #2-gram
    if num == 2:           
        for i in range(len(text.split())):
            if i-1 < 0: 
                continue
            l.append((text.split()[i-1] + ' ' + text.split()[i]))
        return l
    #3-gram
    if num == 3:
        for i in range(len(text.split())):
            if i-1 < 0 or i-2 <0:
                continue
            l.append((text.split()[i-2] + ' ' + text.split()[i-1] + ' ' + text.split()[i]))
        return l

    return "You gave wrong number!"
