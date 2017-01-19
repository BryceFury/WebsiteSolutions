'''

Codewars Kata - 7 Kyu - Remove the minimum

Description:

The museum of incredible dull things wants to get rid of some exhibitions. Miriam, the interior architect, comes up with a plan to remove the most boring exhibitions. She gives them a rating, and then removes the one with the lowest rating.

However, just as she finished rating all exhibitions, she's off to an important fair, so she asks you to write a program that tells her the ratings of the items after one removed the lowest one. Fair enough.

Task

Given an array of integers, remove the smallest value. If there are multiple elements with the same value, remove the one with a lower index. If you get an empty array/list, return an empty array/list.

Don't change the order of the elements that are left.

Examples

remove_smallest([1,2,3,4,5]) = [2,3,4,5]
remove_smallest([5,3,2,1,4]) = [5,3,2,4]
remove_smallest([2,2,1,2,1]) = [2,2,2,1]

'''

def remove_smallest(numbers):
    if numbers == []:
        return numbers
    else:
        numbers.remove(min(numbers))
        [x for (i,x) in enumerate(numbers) if x not in numbers[0:i]]
        return (numbers)

    raise NotImplementedError("TODO: remove_smallest")
