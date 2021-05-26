"""
    ====================== GMIT ====================== 
         Computational Thinking with Algorithms
        Implementation of five sorting algorithms
    ==================================================
"""

nConsoleColumns=13 # number columns displayed
nInputSize=78 # input size start
nPercentIncrease=1.5 # nInputSize 50% increase 
nInputSize=[int((nPercentIncrease**nEachColumn)*nInputSize) for nEachColumn in range(0,nConsoleColumns)] # [0,12] intervel [0,13)
# [78, 117, 175, 263, 394, 592, 888, 1332, 1999, 2998, 4497, 6746, 10120]

# define function - fRandomCollection
def fRandomCollection(nParInputSize):
    """Create collection of random integers in the range [0,99].
Input: nParInputSize
Process: append random integer to each element in local name nCollection (random.randint)
Output: returns local name nCollection of size Input=nParInputSise of random integers
""" 
    from random import randint # standard library import
    nCollection=[] # local collection empty
    for nEachElement in range(0,nParInputSize): # [0,nParInputSize-1] interval [0,nParInputSize)
        nCollection.append(randint(0,99)) # [0,99] interval [0,100)
    return nCollection # to be sorted
# --- END ---

# define function - fBubbleSort
def fBubbleSort(nParCollection):
    """Bubble Sort Algorithm.
    Source: https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheBubbleSort.html
Input: nParCollection
Process: 
Output: sorted collection (in-place)
"""     
    for nOuterIndex in range(len(nParCollection)-1,0,-1): # counting down RHS
        for nInnerIndex in range(nOuterIndex): # bubbling up LHS
            if nParCollection[nInnerIndex]>nParCollection[nInnerIndex+1]: # out of order
                nTemporary=nParCollection[nInnerIndex] # capture inner counter
                nParCollection[nInnerIndex]=nParCollection[nInnerIndex+1] # swap adjacent element
                nParCollection[nInnerIndex+1]=nTemporary # swap inner counter
# --- END ---

# define function - fSelectionSort
def fSelectionSort(nParCollection):
    """Selection Sort Algorithm.
    Source: https://www.geeksforgeeks.org/python-program-for-selection-sort
Input: nParCollection
Process: 
Output: sorted collection (in-place)
""" 
    for nOuterIndex in range(len(nParCollection)): # traverse all elements       
        nMinimumIndex=nOuterIndex # set minimum element        
        for nInnerIndex in range(nOuterIndex+1,len(nParCollection)): # traverse remaining elements
            if nParCollection[nMinimumIndex]>nParCollection[nInnerIndex]: # determine minimum element
                nMinimumIndex=nInnerIndex # minimum element found
        nTemporary=nParCollection[nOuterIndex] # capture current pass
        nParCollection[nOuterIndex]=nParCollection[nMinimumIndex] # swap minimum element
        nParCollection[nMinimumIndex]=nTemporary # swap pass element
# --- END ---

# define function - fInsertionSort
def fInsertionSort(nParCollection):
    """Insertion Sort Algorithm.
    Source: https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheInsertionSort.html
Input: nParCollection
Process: 
Output: sorted collection (in-place)
""" 
    for nOuterIndex in range(1,len(nParCollection)): # traverse all [ 1 ]       
        nElement=nParCollection[nOuterIndex] # capture element value
        nElementPosition=nOuterIndex # capture element position
        while nElementPosition>0 and nParCollection[nElementPosition-1]>nElement: # both are True
            nParCollection[nElementPosition]=nParCollection[nElementPosition-1] # current position move
            nElementPosition=nElementPosition-1 # reset element position
        nParCollection[nElementPosition]=nElement # adjacent element move
# --- END --- 

# define function - fMergeSort
def fMergeSort(nParCollection):
    """Merge Sort Algorithm.
    Source: https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheMergeSort.html
Input: nParCollection
Process: 
Output: sorted collection (in-place)
""" 
    if len(nParCollection)>1: # check base case
        nAppropriatelyHalf=len(nParCollection)//2 # floor division appropriate        
        nLeftPartition=nParCollection[:nAppropriatelyHalf] # slice appropriately half        
        nRightPartition=nParCollection[nAppropriatelyHalf:] # slice appropriately half        
        fMergeSort(nLeftPartition) # recursion call itself
        fMergeSort(nRightPartition) # recursion call itself
        nLeftCounter,nRightCounter,nLoopCounter=0,0,0 # initialise loop counters
        while nLeftCounter<len(nLeftPartition) and nRightCounter<len(nRightPartition):
            if nLeftPartition[nLeftCounter]<=nRightPartition[nRightCounter]: # ensure algorithm stable
                nParCollection[nLoopCounter]=nLeftPartition[nLeftCounter]                
                nLeftCounter+=1
            else:
                nParCollection[nLoopCounter]=nRightPartition[nRightCounter]                
                nRightCounter+=1
            nLoopCounter+=1
            
        while nLeftCounter<len(nLeftPartition): # split if True
            nParCollection[nLoopCounter]=nLeftPartition[nLeftCounter]            
            nLeftCounter+=1
            nLoopCounter+=1
            
        while nRightCounter<len(nRightPartition): # merge if False
            nParCollection[nLoopCounter]=nRightPartition[nRightCounter]            
            nRightCounter+=1
            nLoopCounter+=1
# --- END ---

# define function - fCountingSort
def fCountingSort(nParCollection):
    """Counting Sort Algorithm.
    Source: https://codezup.com/implementation-of-counting-sort-algorithm-in-python/
Input: nParCollection
Process: 
Output: sorted collection
"""     
    nSetMaximumIndex=0 # set start index/position
    for nEachIndex in range(len(nParCollection)): # iterate collection indices
        if nParCollection[nEachIndex]>nSetMaximumIndex: # determine maximum element
            nSetMaximumIndex=nParCollection[nEachIndex] # maximum valued element 
    # each element zero
    nBuckets=[0]*(nSetMaximumIndex+1) # length maximum element+1
    for nEachElement in nParCollection: # iterate collection elements
        nBuckets[nEachElement]+=1 # populate discrete indices
    # bucket includes indices
    nIndexReset=0 # set start index/position
    for nEachElement in range(nSetMaximumIndex+1): # iterate bucket length
        for nBucketElement in range(nBuckets[nEachElement]): # iterate bucket zeros
            nParCollection[nIndexReset]=nEachElement # populate count zeros 
            nIndexReset+=1 # move next index/position
    return nParCollection
# --- END ---

# define function - fTotalRuns
def fTotalRuns(nParRuns):
    """Initialise number of runs based on specification.
    
Input: nParRuns
Process: assign global name=nRuns to number of runs specified
Output: used within functions: i) main and; ii) fAverageTime
"""
    global nRuns # accessed by main/fAverageTime
    nRuns=nParRuns # initialise global in-place
# --- END ---

# define function - fAverageTime
def fAverageTime(nParCollection):
    """Average time of each algorithm based on specified number of runs.
Input: nParCollection
Process: sum total of all elements within Input=nParColleciton (sum);
    global name=nRuns determines average time (fTotalRuns)
Output: average time
"""
    return sum(nParCollection)/nRuns # console output average
# --- END ---

# define function - main
def main():
    """Benchmark the implementation of five sorting algorithms.
Input: 
Process: traverse the global name=nInputSize;
    initialise dictionary with sorting algorithm function **copies** - calling functions later;
    traverse the dictionary keys or function copies;
    traverse the number of runs as per specification - ten;
    start timer; (time.time
    call functions via copy; generate random integers interval [0,100) of size name=nEachInputSize;
    end timer; (time.time)
    capture time and calculate average time for each algorithm
Output: formatted console display of each sorting algorithm with associated average times
"""
    from time import time # standard library import

    global nAverage
    nAverage=[] # collection average time

    for nEachInputSize in nInputSize: # default global nInputSize
    # [78, 289, 623, 1075, 1639, 2315, 3099, 3990, 4986, 6086, 7289, 8594, 10000]

        global nSortingAlgorithms
        nSortingAlgorithms={ # key function copy
            fBubbleSort:f"{fBubbleSort.__name__[1:-4]}"+f" {fBubbleSort.__name__[-4:]}", # value output console
            fSelectionSort:f"{fSelectionSort.__name__[1:-4]}"+f" {fSelectionSort.__name__[-4:]}",
            fInsertionSort:f"{fInsertionSort.__name__[1:-4]}"+f" {fInsertionSort.__name__[-4:]}",
            fMergeSort:f"{fMergeSort.__name__[1:-4]}"+f" {fMergeSort.__name__[-4:]}",
            fCountingSort:f"{fCountingSort.__name__[1:-4]}"+f" {fCountingSort.__name__[-4:]}"
        } # dictionary of algorithms

        for nKeyFunction in nSortingAlgorithms.keys(): # function copy key
        # keys: fBubbleSort; fSelectionSort; fInsertionSort; fMergeSort; fCountingSort

            nTimes=[] # collection of times

            # module fubar - function fTotalRuns 
            fTotalRuns(nParRuns=10) # global name nRuns

            for nEachRun in range(nRuns): # ten per specification

                nStart=time() # green flag go
                # module fubar - function fRandomCollection     
                nKeyFunction(fRandomCollection(nParInputSize=nEachInputSize)) # collection size nInputSize   
                nEnd=time() # chequered flag stop

                nTimes.append((nEnd-nStart)*1000) # time milliseconds calculation

            # module fubar - function fAverageTime
            nAverage.append(round(fAverageTime(nParCollection=nTimes),3)) # average three decimals
# --- END ---

if __name__=="__main__": # __name__ current module 
    # module fubar - function main 
    main()
    
    #
    # 1.1. The Application
    # ====================
    
    # application console output
    nRowDisplay="{:<15}"*(len(nInputSize)+1) # format console output
    print(nRowDisplay.format("Size", *nInputSize))
    print(nRowDisplay.format(f"{nSortingAlgorithms[fBubbleSort]}", # key value "Bubble Sort"
                             *nAverage[::5])) # slice step five
    print(nRowDisplay.format(f"{nSortingAlgorithms[fSelectionSort]}", # key value "Selection Sort"
                             *nAverage[1::5])) # index one slice
    print(nRowDisplay.format(f"{nSortingAlgorithms[fInsertionSort]}",*nAverage[2::5]))
    print(nRowDisplay.format(f"{nSortingAlgorithms[fMergeSort]}",*nAverage[3::5]))    
    print(nRowDisplay.format(f"{nSortingAlgorithms[fCountingSort]}",*nAverage[4::5]))
    
    #
    # --- END ---
    # ===========
    
    #
    # 1.3 Report (Implementation & Benchmarking) 
    # ==========================================
    
    # i) build csv "rc\Benchmark\dataset.csv"
    from pandas.core.frame import DataFrame # third-party library import
    from numpy import array # third-party library import    
    df=DataFrame(data=array( # list of list
                    [nAverage[::5],nAverage[1::5],nAverage[2::5],nAverage[3::5],nAverage[4::5]]), # slice as before
                 index=[nSortingAlgorithms[fBubbleSort],nSortingAlgorithms[fSelectionSort],
                    nSortingAlgorithms[fInsertionSort],nSortingAlgorithms[fMergeSort],
                    nSortingAlgorithms[fCountingSort]]) # algorithms as index
    df.to_csv("rc\Benchmark\dataset.csv") # bare bones csv

    # ii) build plot "BenchmarkingPlot.png"    
    from matplotlib.pyplot import savefig,close # third-party library import

    # RangeIndex(start=0, stop=13, step=1) ...
    df.columns=nInputSize # change x-axis ticks ...
    # Int64Index([78, 289, 623, 1075, 1639, 2315, 3099, 3990, 4986, 6086, 7289, 8594, 10000], dtype='int64')

    df.T.plot(kind="line", # default plot value
              figsize=(19.2,10.8), # size in inches
              title="Benchmarking - Sorting Algorithms", # plot overall title
              grid=True, # split into five
              style="o-", # data point circle
              xlabel="Input size n", # label on x-axis
              ylabel="Running time milliseconds" # label on y-axis
            ); # benchmarking results plot
    savefig(fname="BenchmarkingPlot.png") # to current directory
    close() # close figure window    
    
    # iii) build table "BenchmarkingTable.png"
    from pandas.io.parsers import read_csv # third-party library import
    df=read_csv("rc\Benchmark\dataset.csv",header=0,names=nInputSize) # read csv created
    df.columns.name="Size" # set index heading
    df=df.style.set_table_styles( # сhange style output
                        [{"selector":"","props":[("border","2px solid black"),("font-size","25px")]}]
                                    ).set_precision(3) # set decimal percision
    
    try:
        import dataframe_image # third-party library import
        dataframe_image.export(df,"BenchmarkingTable.png",table_conversion="matplotlib") # build dataframe image
    except ImportError:
        print("You Are Missing a Package (dataframe_image)")
        print("Please Install - Restart Application")
        print("$ conda install -c conda-forge dataframe_image ")
        print("https://pypi.org/project/dataframe-image/")  
        
    #
    # --- END ---
    # ===========