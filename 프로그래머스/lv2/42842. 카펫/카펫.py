# def solution(brown, yellow):
#     entral = brown + yellow
#     for sello in range(entral,0,-1):
#         if entral % sello == 0:
#             garo = entral // sello
#             if (garo >= sello) and (brown == garo * 2 + (sello-2) * 2):
#                 return [garo,sello]


def solution(brown,yellow):
    entrol = brown + yellow
    for sero in range(entrol,0,-1):
        if entrol % sero == 0:
            garo = entrol // sero
            if garo >= sero and 2*garo + 2*(sero-2) == brown:
                return [garo,sero]