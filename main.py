import random, time
import tabulate

import sys

sys.setrecursionlimit(999999999)

def ssort(L):
    ### selection sort
    if (len(L) == 1):
        return(L)
    else:
        m = L.index(min(L))
        print('selecting minimum %s' % L[m])       
        L[0], L[m] = L[m], L[0]
        print('recursively sorting L=%s\n' % L[1:])
        return [L[0]] + ssort(L[1:])
        
def qsort(a, pivot_fn):
    # If list is empty, return the empty list
    if len(a) == 0:
        return a
    else:
        # Pick random pivot point
        p = pivot_fn(a)
        # list of elements less than pivot
        lesser_list = list(filter(lambda x: x < p, a))
        # list of elements equal to pivot
        pivot_list = list(filter(lambda x: x == p, a))
        # list of elements grater than pivot
        greater_list = list(filter(lambda x: x > p, a))

        # Recursively Sort greater and lesser lists
        sorted_lesser = qsort(lesser_list, pivot_fn)
        sorted_greater = qsort(greater_list, pivot_fn)

        # Return a total sorted list by recombining lists
        return sorted_lesser + pivot_list + sorted_greater



    
def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds. 
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key 

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    # adjusted time.time to time.perf_counter() to help make sure to get more accurate time
    start = time.perf_counter()
    sort_fn(mylist)
    return (time.perf_counter() - start) * 1000
    ###
'''5000, 10000, 20000, 50000, 100000'''
def compare_sort(sizes=[100, 200, 500, 1000, 2000, 5000,10000]):
    """
    Compare the running time of different sorting algorithms.

    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """

    qsort_fixed_pivot = lambda a: qsort(a, lambda x: x[0])
    qsort_random_pivot = lambda a: qsort(a, lambda x: random.choice(x))
    tim_sort = sorted
    result = []
    for size in sizes:
        # create list in ascending order
        mylist = list(range(size))
        # shuffles list if needed
        #random.shuffle(mylist)
        result.append([
            len(mylist),
            time_search(qsort_fixed_pivot, mylist),
            time_search(qsort_random_pivot, mylist),
            time_search(tim_sort, mylist)
        ])
    print(result)
    return result


def print_results(results):
    """ change as needed for comparisons """
    print(tabulate.tabulate(results,
                            headers=['n', 'qsort-fixed-pivot', 'qsort-random-pivot', 'tim_sort'],
                            floatfmt=".3f",
                            tablefmt="github"))

def test_print():
    print_results(compare_sort())

random.seed()

test_print()
