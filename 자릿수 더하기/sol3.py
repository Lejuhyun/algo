def solution(n):
    return sum(map(int, list(str(n)))) #list(str(n)) => ['1','2','3','4']
    #map(int,list(str(n))) => [1,2,3,4]