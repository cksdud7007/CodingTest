def solution(n, words):
    words_count = {}
    for i in words: 
        words_count[i] = 0

    for i in range(len(words)-1):
        words_count[words[i]] += 1
        if words_count[words[i]] > 1 or words[i][-1] != words[i+1][0]:
            if words_count[words[i]] > 1:
                return [(i%n) + 1 ,(i//n) + 1]
            else:
                return [((i+1)%n) + 1 ,((i+1)//n) + 1]
        if i+1 == len(words) - 1:
            words_count[words[i+1]] += 1
            if words_count[words[i+1]] > 1:
                return [((i+1)%n) + 1 ,((i+1)//n) + 1]
    return [0,0]