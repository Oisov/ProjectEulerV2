"""
    Provides a module for the inclusion exclusion protocol
"""

from projecteuler.utilities import reduce_w_cache, powerset
import functools

from collections.abc import Callable
from typing import Annotated, Any

ObjectIEP = Annotated[
    object,
    "An user defined object that has a defined intersection and way to define its size (len)",
]
Content = Annotated[
    Any,
    "An intrinsic property that defines the shape and form of our object",
]

Limit = Annotated[
    int,
    "A positive integer representing the limit "
    "below which all even Fibonacci numbers are to be summed",
]


class ConstructorIEP:

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
    list_of_object_contents: list[Content],
    intersection: Callable[[Content, Content], Content],
    cardinality: Callable[[ObjectIEP], int],
    cache=False,
) -> int:
    """If list_of_objects = [A, B, C, D, ...] this function returns |A ∩ B ∩ C ∩ D ∩ ...|

    The return value is calculated using the exclusion inclusion principle;
    here | | denotes the cardinality (or in Pythons words the length) of the set,
    and ∩ represents the intersection of two objects. See the link for more information

    https://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle

    Args:
        list_of_object_contents: A list of contents that with intersection and
                                 cardinality defines an object
        intersection: A function(x, y) that returns what two object contents has
                      in common (defines x.intersection(y))
        cardinality: A function(x) that returns the size of an object (defines len(object))

    Returns:
        int: Returns the size (len) of the intersection of every element in ``list_of_objects``

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

        Setup for continous ranges is a bit harder as it is cumbersome to define the
        intersections between two intervals properly
        >>> def intersection(*intervals):
        ...     max_first, min_last = [f(i) for f, i in zip([max, min], zip(*intervals))]
        ...     if (min_last - max_first) >= 0:
        ...         return [max_first, min_last]
        ...     return [float("inf"), float("inf")]
        ...
        >>> cardinality = lambda a: len(range(*a))
        >>> inclusion_exclusion_principle([[0, 0]], intersection, cardinality)
        0
        >>> inclusion_exclusion_principle([[1, 2], [1, 2]], intersection, cardinality)
        1
        >>> inclusion_exclusion_principle([[0, 3], [1, 2]], intersection, cardinality)
        3
        >>> inclusion_exclusion_principle([[2, 4], [3, 5], [4, 6]], intersection, cardinality)
        4

        As a more advanced example we can use inclusion-exclusion-principle to
        find the union of all numbers divisible by 1 or more of our objects.
        Essentially solving the first project euler problem
        >>> gcd = lambda m,n: m if not n else gcd(n, m % n)
        >>> lcm = lambda a, b: abs(a * b) // gcd(a, b)
        >>> start, stop = 1, 1000
        >>> intersection = lcm
        >>> cardinality = lambda x: sum(i for i in range(start, stop) if i % x == 0)
        >>> inclusion_exclusion_principle([3, 5], intersection, cardinality)
        233168

        Of course this could have been improved by implementing a cardinality
        that runs in linear time
        >>> sum_linear = lambda start, stop: (stop + start + 1) * (stop - start) // 2
        >>> cardinality = lambda x: x * sum_linear(start//x, (stop-1)//x)
        >>> inclusion_exclusion_principle([3, 5], intersection, cardinality)
        233168

    """

    Object = make_IEP(intersection, cardinality)
    list_of_objects = list(map(Object, list_of_object_contents))
    reduce = reduce_w_cache if cache else functools.reduce

    def intersect(list_of_objects):
        """Finds the intersection of a list of objects according to the rules set by intersections"""

        # If the list of sets only contains one element, we are left with
        # finding the intersection of a set with itself. However, this is just
        # the set itself, because intersection retrieves the common elements.
        # Here, all elements of a set is common with itself. Hence, the
        # resulting intersection of a set with itself, is itself

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


if __name__ == "__main__":
    import doctest

    doctest.testmod()
