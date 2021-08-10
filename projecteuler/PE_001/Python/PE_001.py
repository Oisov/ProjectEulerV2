"""
Problem 1: Multiples of 3 and 5
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
    3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

import itertools
import math
import sys

import typing
from typing import Tuple, Optional, Union
import functools
import copy


@functools.cache
def reduce_w_cache(function, sequence):
    """Reduces the sequence to a single number by left folding function over it

    Example:

        The easiest way to understand how reduce works is applying a tuple to it
        >>> sequence = tuple([1, 3, 5, 6, 2])
        >>> make_tuple = lambda x, y: tuple([x, y])
        >>> reduce_w_cache(make_tuple, sequence)
        ((((1, 3), 5), 6), 2)

        Similarly a right fold would look like ``(1, (3, (5, (6, 2))))``

        >>> add = lambda x, y: x + y
        >>> sum_reduce = lambda x: reduce_w_cache(add, x)
        >>> reduce_w_cache(add, sequence)
        17

        Understanding how this works is as easy as replacing , with + in the
        example above

            reduce_w_cache(add, sequence) = ((((1 + 3) + 5) + 6) + 2) = 17

        >>> prod = lambda x, y: x * y
        >>> reduce_w_cache(prod, sequence)
        180

        By replacing ``,`` with ``*`` we have

            reduce_w_cache(add, sequence) = ((((1 * 3) * 5) * 6) * 2) = 17

        Lastly we can find the max / min just as easilly
        >>> maximum = lambda x, y: x if y < x else y
        >>> reduce_w_cache(maximum, sequence)
        6

        >>> reduce_w_cache(min, sequence)
        1

        Let us test if the caching works. We first save how many misses we
        have, where a miss corresponds to a value being added to the cache. We
        will then perform some lookups and study how many values were cached.

        >>> repeat_reduce = lambda fun, seqs: [reduce_w_cache(fun, tuple(s)) for s in seqs]
        >>> def values_cached(function, sequences):
        ...     initial = reduce_w_cache.cache_info().misses
        ...     repeat_reduce(function, sequences)
        ...     total = reduce_w_cache.cache_info().misses
        ...     return total - initial

        >>> test_function = lambda x, y: [x, y]
        >>> sequences = [[103], [103, 105], [103, 105, 107], [103, 105, 107, 109], [103, 105, 107, 109, 111]]

        We are going to run ``reduce_w_cache`` with ``test_function`` over
        each element in ``sequences`` With no caching we would expect ``len - 1``
        function calls with a minimal of ``1`` for each sequence in sequences. Totaling to
        `1 + 1 + 2 + 3 + 4 = 11` function calls.

        However with cached values this is greatly lowered. For instance ``(103, 105,
        107)`` folds to ``(103, (105, 107))`` and the value of ``(105, 107)``
        is already stored in the cache.
        >>> values_cached(test_function, sequences)
        5

        No new values should be added if we lookup the same values again
        >>> values_cached(test_function, sequences)
        0

        As a sanity check let us test how many values are cached when
        we can not use previously stored values
        >>> sequences = [[112], [113, 114], [115, 116, 117], [118, 119, 120, 121], [118, 119, 120, 121, 122]]
        >>> values_cached(test_function, sequences)
        11

        Let us double check that the number of calls really is 11. For each
        function call we wrap two elements in ``[]`` so simply counting the number
        of either ``[`` or ``]`` returns the number of function calls.
        >>> str(repeat_reduce(test_function, sequences)).count('[')
        11
    """
    *remaining, last = sequence
    if not remaining:
        return last
    return function(reduce_w_cache(function, tuple(remaining)), last)

class ConstructorIEP:
    # def __init__(self, intersect, cardinality):
    #     self.intersect = intersect
    #     self.cardinality = cardinality
    
    @property
    def content(self):
        return self._content
    
    @content.setter
    def content(self, stuff):
        self._content = stuff
        self.len = self.cardinality(self._content)
    
    def intersection(self, *others):
        if len(others) == 0:
            new_content = self.content
    
        new_content = self.content
        for other in others:
            new_content = self.intersect(new_content, other.content)
        IEP = make_IEP(self.intersect, self.cardinality)
        return IEP(new_content)

    def __eq__(self, other):
        if not type(self) == type(other):
            return False
        same_intersect = self.intersect == other.intersect
        same_cardinality = self.cardinality = other.cardinality
        return same_intersect and same_cardinality

    def __and__(self, other):
        if not self.__eq__(other):
            raise TypeError("& is only defined for objects of same type")
        return self.intersection(other)

    def __len__(self):
        return self.len
    
    def __repr__(self):
        return f"IEP({self.content})"
    
    def __str__(self):
        return f"{self.content}, len={self.len}"

def make_IEP(intersect, cardinality):

    class IEP(ConstructorIEP):
    
        def __init__(self, content):
            self.intersect = intersect
            self.cardinality = cardinality
            self.content = content

    return IEP


def inclusion_exclusion_principle(
    list_of_object_contents, intersection, cardinality, cache=False
):
    """Use inclusion-exclusion principle to find the cardinality of the union of a list of objects

    Takes advantage of that set intersection ∩ is an associative operation
    that is for every set A, B, C we have A ∩ B ∩ C = A ∩ (B ∩ C) in programming
    this is known as a right fold (rfold) and is implemented by reduce

    Examples:

        Setup for discrete sets
        >>> intersection = lambda a, b: a.intersection(b)
        >>> cardinality = len
        >>> sets = [set([])]
        >>> inclusion_exclusion_principle([{}], intersection, cardinality)
        0
        >>> inclusion_exclusion_principle([{1, 2, 3}, {1, 2, 3}], intersection, cardinality)
        3
        >>> inclusion_exclusion_principle([{1, 2, 3}, {4, 5, 6}], intersection, cardinality)
        6

        Setup for continous ranges
        >>> intersection = lambda a, b: [max(a[0], b[0]), min(a[1], b[1])]
        >>> cardinality = lambda a: len(range(*a))
        >>> inclusion_exclusion_principle([[0, 0]], intersection, cardinality)
        0
        >>> inclusion_exclusion_principle([[1, 2], [1, 2]], intersection, cardinality)
        1
        >>> inclusion_exclusion_principle([[0, 3], [1, 2]], intersection, cardinality)
        3
        >>> inclusion_exclusion_principle([[2, 4], [3, 5], [4, 6]], intersection, cardinality)
        4

    """
    Object = make_IEP(intersection, cardinality)
    list_of_objects = list(map(Object, list_of_object_contents))
    reduce = reduce_w_cache if cache else functools.reduce

    def intersect(list_of_objects):
        """Finds the intersection of a list of sets according to the rules set by intersections"""

        # If the list of sets only contains one element we are left with
        # finding the intersection of a set with itself. However, the
        # intersection of a set with itself is the set itself. This is because
        # intersection is a set of common elements. Here, all elements of a set
        # is common with itself. The resulting intersection, therefore, is set
        # itself.
            
        if len(list_of_objects) == 1:
            return list_of_objects[0]
        return reduce(lambda x, y: x.intersection(y), list_of_objects)

    def cardinality(obj):
        return len(obj)

    sign = 1
    cardinality_of_union = 0
    # It will be easier to follow this code through an example
    # list_of_objects = [A, B, C]
    # powerset(list_of_objects) = [
    #       [[A], [B, [C]], 
    #       [[A, B], [A, C], [B, C]], 
    #       [A, B, C]]
    # ]
    for subsets_w_same_len in powerset(list_of_objects, flatten=False):
        # intersections:
        #    First pass: = [A, B, C]              # All subsets of len 1 (intersection of itself is itself)
        #   Second pass: = [A ∩ B, A ∩ C, B ∩ C]  # All subsets of len 2
        #    Final pass: = [A ∩ B ∩ C]            # All subsets of len 3
        intersections = map(intersect, subsets_w_same_len)
        # cardinalities:
        #    First pass: = [ |A|, |B|, |C| ]
        #   Second pass: = [ |A ∩ B|, |A ∩ C|, |B ∩ C| ]
        #    Final pass: = [ |A ∩ B ∩ C| ]
        cardinalities = map(cardinality, intersections)
        # cardinality_of_union:
        #    First pass: = |A| + |B| + |C| 
        #   Second pass: = |A| + |B| + |C|
        #                - ( |A ∩ B| + |A ∩ C| + |B ∩ C| )
        #    Final pass: = |A| + |B| + |C|
        #                - ( |A ∩ B| + |A ∩ C| + |B ∩ C| )
        #                + ( |A ∩ B ∩ C| )
        cardinality_of_union += sign * sum(cardinalities)
        sign *= -1
    return cardinality_of_union


def lcm_of(numbers: Tuple[int]) -> int:
    """Computes the lcm (lowest common multiple) of a tuple of numbers

    Equivalent of using itertools.reduce, but with memoization.
    This code first performs a right fold of the input values

    .. code-block:: python

        (3, 5, 7) = (3, (5, 7)) = (3, (5, (7))) = (3, (5, (7, ())))

    Then each parenthesis is recursively applied a lcm, starting from within

    .. code-block:: python

          (3, (5, (7, ())))   # if last value is empty, return first (7)
        = (3, (5, 7))         # lcm(5,  7) = 15
        = (3, 15)             # lcm(3, 15) = 15
        = 105

    If ``(3, 5)`` was precomputed, the calculation would instead be

    .. code-block:: python

        (3, 5, 7) = (3, (5, 7)) = (3, 15) = 105

    Example:


    >>> [lcm_of(nums) for nums in [(3,), (3, 5), (3, 5, 7)]]
    [3, 15, 105]
    """
    return reduce_w_cache(math.lcm, numbers)


def sum_integers(start: int, stop: int) -> int:
    """Finds the sum of all numbers in [start, stop] in constant time

    Equivalent to

        list(range(start, stop + 1))

    but in constant time. Exploits the fact that 1 + 2 + 3 + ... + n = n(n + 1)/2 see
    https://en.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_⋯

    Since we do not neccecarily start from 1, we substract the sum from 1 to start-1 for instance

        5 + 6 + 7 + ... + n = (1 + 2 + 3 + ... + n) - (1 + 2 ... + 5 - 1)
                            = n(n + 1)/2 - 5(5 - 1)/2
                            = (n + 5)(n - 5 + 1)/2
    >>> sum_integers(0, 0)
    0

    >>> pairs = [(0, 5), (0, -5), (5, 0), (-5, 0)]
    >>> [sum_integers(*pair) for pair in pairs]
    [15, -15, 15, -15]

    >>> pairs = [(5, 10), (5, -10), (-5, -10), (-5, 10)]
    >>> [sum_integers(*pair) for pair in pairs]
    [45, -40, -45, 40]

    >>> sum_integers(10, 10)
    10
    """
    start, stop = min(start, stop), max(start, stop)
    return (stop + start) * (stop - start + 1) // 2


def sum_multiplies_of(k: int, start: int, stop: int) -> int:
    """Finds the sum of all numbers in [start, stop] such that number is a multiple of k in constant time

    This code is equivalent to the following code

        sum(d for d in range(start, stop) if d % k == 0)

    The difference is that the code below achieves this in linear time (O(n)).
    We are interested in multiples of k, for instance let k = 3 then

        3 + 6 + 9 + 12 + ... + 999 = 3(1 + 2 + 3 + ... + 333) = 3 * 333(333 + 1)/2

    To figure out how many terms we need to sum (333) we do `stop // k`

    >>> sum_multiplies_of(2, 0, 10)
    30

    Since 0 + 2 + 4 + 6 + 8 + 10 = (2 + 8) + (4 + 6) + (10) = 30
    >>> sum_multiplies_of(2, 10, 10)
    10
    """
    return k * sum_integers(start // k, stop // k)


def powerset(iterable, emptyset=False, flatten=True):
    """Returns the powerset of some list, grouped by length

    Examples:
        >>> list(powerset([1,2,3]))
        [(1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]

        >>> list(powerset([1,2,3], emptyset=True))
        [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]

        >>> list(list(i) for i in powerset([1,2,3], flatten=False))
        [[(1,), (2,), (3,)], [(1, 2), (1, 3), (2, 3)], [(1, 2, 3)]]

        >>> list(list(i) for i in powerset([1,2,3], emptyset=True, flatten=False))
        [[()], [(1,), (2,), (3,)], [(1, 2), (1, 3), (2, 3)], [(1, 2, 3)]]
    """

    try:
        iterator = iter(iterable)
        s = list(iterable)
    except TypeError:
        if not isinstance(iterable, list):
            raise TypeError("Input must be list or iterable")
        s = iterable
    start = 0 if emptyset else 1
    powerset_ = (itertools.combinations(s, r) for r in range(start, len(s) + 1))
    return itertools.chain.from_iterable(powerset_) if flatten else powerset_


def yield_times(iterable, pattern):
    """ " Yield an iterator times some pattern

    >>> list(yield_times(range(10), [1, -1]))
    [0, -1, 2, -3, 4, -5, 6, -7, 8, -9]

    >>> alternating_sum = lambda x: sum(yield_times(x, [1, -1]))
    >>> alternating_sum(range(10))
    -5

    >>> squared = lambda x: yield_times(x, x)
    >>> list(squared(range(10)))
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    """
    total = 0
    pattern_ = itertools.cycle(pattern)
    for i, value in enumerate(iterable):
        yield next(pattern_) * value


Divisor = typing.NewType("Divisor", int)
Divisors = typing.NewType("Divisors", list[Divisor])
Stop = typing.NewType("Stop", int)
Start = typing.NewType("Start", int)


def make_proper(divisors: Divisors) -> Divisors:
    """Returns the unique sorted divisors such that x % y != 0 for every x, y in divisors

    1. We remove every duplicate in the list
    >>> make_proper([2, 2])
    [2]

    2. We sort the divisors from smallest to largest
    >>> make_proper([3, 2])
    [2, 3]

    This offers a small speedup as more numbers are divisible by 2 than 3.
    3. We only keep the divisors which are not a multiple of another value
    >>> make_proper([5, 10, 6, 9])
    [5, 6, 9]

    >>> make_proper([5, 10, 6, 9, 3])
    [3, 5]

    Since every multiple of 4 is also a multiple of 2, we can discard 4.
    """
    new_divisors = list()
    for divisor in sorted(set(divisors)):
        if all(divisor % d != 0 for d in new_divisors):
            new_divisors.append(divisor)
    return new_divisors


def PE_001(
    x: Union[Start, int], y: Union[Stop, Divisors], divisors: Optional[Divisors] = None
) -> int:
    """Finds the sum of all numbers divisible by the divisors in range [start, stop).

    This is done using the inclusion-exclusion principle
    https://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle

    Since the running time of the algorithm is O(2**divisors) some
    some effort is put into minimizing the number of divisors see make_proper for details

    >>> PE_001(0, 10, [2, 3])
    32

    >>> PE_001(10, [2, 3])
    32

    Since 2 + 3 + 4 + 6 + 8 + 9 = 32.
    """
    if divisors is None:
        start, stop, divisors = 0, x, y
    else:
        start, stop = x, y

    # if len(divisors) == 0:
    #     return 0

    """
    To use the inclusion_exclusion_principle (IEP) we need to define what our
    list of objects are, their cardinality (how to define the size of an
    object) and intersection (how to define what two objects has in common) Let
    our ``list_of_objects = [3, 5]`` but do not think of 3 and 5 as the numbers
    3 and 5 but as the objects 3 and 5. For instance these objects may then
    represents how many numbers are divisible by this number in some range.
    Concretely if 3 is our object, start = 1 and stop = 5 then

        3 := [i for i in range(start, stop) if i % 3]

    This makes it really easy to define cardinality! That just just the size of
    the object so 

        cardinality(3) = sum(3)

    In our actual implementation though we use a smarter method for evaluating
    the right hand side in constant time. Intersection defines what the object
    has in common. For instance if we look at what the following objects has in
    common

        3 = [i for i in range(start, stop) if i % 3]
        5 = [i for i in range(start, stop) if i % 5]

    it is not hard to figure out that this as to be 

        Intersection(3, 5) = [i for i in range(start, stop) if i % 15]

    Because every multiple of 15 is divisible by both 3 and 5. You might think
    that we can always just multiply the numbers togheter, but we have to be
    more careful. If we study the objects 6 and 9, it is clear that 56 divides
    both 6 and 9, but so does 18. To summarize to find the intersection of two
    objects X and Y we need to find the smallest number Z such that Z / X and Z / Y
    are integers. Luckilly clever mathematicians has named such a number the 
    lowest common multiple (lcm) and has a built in function for calculating it
    """

    intersection = lambda x, y: math.lcm(x, y)
    cardinality = lambda x: sum_multiplies_of(x, start, stop - 1)
    return inclusion_exclusion_principle(
        make_proper(divisors), intersection, cardinality
    )


if __name__ == "__main__":

    import doctest

    # doctest.testmod()

    #     if len(sys.argv) == 2:
    #         args = sys.argv[1].split("|")
    #         start, stop, divisors = int(args[0]), int(args[1]), eval(args[2])
    #     else:
    #         start, stop, divisors = 1, 1000, [3, 5]
    #
    #     print(PE_001(start, stop, divisors))

    def intersect(list_of_objects):
        """Finds the intersection of a list of sets according to the rules set by intersections"""

        # If the list of sets only contains one element we are left with
        # finding the intersection of a set with itself. However, the
        # intersection of a set with itself is the set itself. This is because
        # intersection is a set of common elements. Here, all elements of a set
        # is common with itself. The resulting intersection, therefore, is set
        # itself.
        first_object = list_of_objects[0]
        intersection = first_object.intersection
        return (
            first_object
            if len(list_of_objects) == 1
            else functools.reduce(intersection, list_of_objects)
        )

    def cardinality(obj):
        return len(obj)

    start, stop, divisors = 1, 1000, []
    intersection = lambda x, y: math.lcm(x, y)
    cardinality = lambda x: sum_multiplies_of(x, start, stop - 1)
    print(inclusion_exclusion_principle(divisors, intersection, cardinality))
    # IEP = make_IEP(intersection, cardinality)
    # objects = [IEP(content) for content in divisors]
    # print(objects[0] & objects[1])
#     print(objects[0] == objects[1])
# 
#     intersection_ = lambda x, y: math.lcm(int(x), int(y))
#     cardinality_ = lambda x: x**2
#     IEP2 = make_IEP(intersection_, cardinality_)
#     object2 = IEP2(2)
#     print(object2 == objects[0])

#     a, b, c = list(powerset(objects, flatten=False))
#     a, b, c = list(a), list(b), list(c)
# 
#     first, second, third = objects[:3]
# 
#     print(b[1])
#     print(intersect(b[1]))
# 
#     def overlap(interval1, interval2):
#         """
#         Given [0, 4] and [1, 10] returns [1, 4]
#         """
#         if interval2[0] <= interval1[0] <= interval2[1]:
#             start = interval1[0]
#         elif interval1[0] <= interval2[0] <= interval1[1]:
#             start = interval2[0]
#         else:
#             return [float('Inf'), float('Inf')]
#     
#         if interval2[0] <= interval1[1] <= interval2[1]:
#             end = interval1[1]
#         elif interval1[0] <= interval2[1] <= interval1[1]:
#             end = interval2[1]
#         else:
#             return [float('Inf'), float('Inf')]
#         return [start, end]
# 
#     intersection = lambda a, b: overlap(a, b)
#     cardinality = lambda a: len(range(*a))
#     intervals = [[1,3], [2,5], [3, 4]]
#     IEP = make_IEP(intersection, cardinality)
#     objects = [IEP(id_) for id_ in intervals]
#     a, b, c = list(powerset(objects, flatten=False))
#     a, b, c = list(a), list(b), list(c)
# 
#     chosen = b[2]
#     print(chosen, intersect(chosen))
#     print(overlap(chosen[0].content, chosen[1].content))
# 
#     if len(c[0]) == 3:
#         print("hmm")
#         first, second, third = c[0]
#         print(first, second, third)
#         first & second
