from abr import ABR
from arn import ARN
from random import shuffle
from timeit import default_timer as timer


def runAllTests(numbers):
    risultati = []
    cifreDec = 4
    for n in numbers:
        # test di inserimento di elementi ordinati
        array = range(n)
        ordBT_Height, ordRBT_Height, ordBT_Time, ordRBT_Time = test(array)
        ordBT_Time = round(ordBT_Time, cifreDec)
        ordRBT_Time = round(ordRBT_Time, cifreDec)

        # test di inserimento di elementi in ordine ottimo
        array = bestOrder(array)
        bestBT_Height, bestRBT_Height, bestBT_Time, bestRBT_Time = test(array)
        bestBT_Time = round(bestBT_Time, cifreDec)
        bestRBT_Time = round(bestRBT_Time, cifreDec)

        # test di inserimento di elementi in ordine casuale
        randBT_Height, randRBT_Height, randBT_Time, randRBT_Time = 0, 0, 0, 0
        numRandomTests = 10
        for i in range(numRandomTests):
            shuffle(array)
            BTh, RBTh, BTt, RBTt = test(array)
            randBT_Height += BTh
            randRBT_Height += RBTh
            randBT_Time += BTt
            randRBT_Time += RBTt

        randBT_Height /= numRandomTests
        randRBT_Height /= numRandomTests
        randBT_Time /= numRandomTests
        randRBT_Time /= numRandomTests
        randBT_Time = round(randBT_Time, cifreDec)
        randRBT_Time = round(randRBT_Time, cifreDec)
        
        risultati.append([n, ordBT_Height, ordRBT_Height, bestBT_Height, bestRBT_Height, randBT_Height, randRBT_Height, ordBT_Time, ordRBT_Time, bestBT_Time, bestRBT_Time, randBT_Time, randRBT_Time])
    return risultati


def test(array):
    # array2 = copyArray(array)
    bTree = ABR()
    rbTree = ARN()

    # misuro il tempo di inserimento di n elementi in albero binario di ricerca
    start = timer()
    for x in array:
        bTree.insert(x)
    end = timer()
    bTime = end - start

    # misuro il tempo di inserimento di n elementi in albero rosso nero
    start = timer()
    for x in array:
        rbTree.insert(x)
    end = timer()
    rbTime = end - start
    
    return bTree.height(), rbTree.height(), bTime, rbTime


def bestOrder(orderedArray):
    def _bestOrder(orderedArray, recursionStep=0):
        if len(orderedArray) > 0:
            m = int(len(orderedArray)/2)
            values.append((orderedArray[m], recursionStep))
            _bestOrder(orderedArray[:m], recursionStep+1)
            _bestOrder(orderedArray[m+1:], recursionStep+1)
    values = []
    _bestOrder(orderedArray)
    values.sort(key=lambda tupla: tupla[1])
    return [tupla[0] for tupla in values]
