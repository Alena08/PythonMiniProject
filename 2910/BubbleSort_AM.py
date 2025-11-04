# Funktion BubbleSort(a) 
# Es wird eine Liste (a) übergeben und dann sortiert

def BubbleSort(a) :
    n = len(a)
    i = n-1
    while i > 0:
        j = 1
        while j <= i:
            if a[j-1] > a[j]:
                tausche(a, j)
            j+=1
        i-=1

# tausche(a, j) tauscht, bei Bedarf, die beiden Listenelemente

def tausche(a, j):
        a[j-1],a[j] = a[j],a[j-1]
        # temp = a[j-1]
        # a[j-1]=a[j]
        # a[j]=temp


###############    
### M A I N ###
###############

#a = [ 7, 4, 12, 1, 2]
a = [23, 67, 84, 0, 12, -4,100,1]
BubbleSort(a)
print('#######################################')
print('Ergebnis:             ',a, sep='')