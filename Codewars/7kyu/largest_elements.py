"""
Write a program that outputs the top n elements from a list.
"""

def largest(n,xs):
    elements = xs
    largest_elements = []
    for i in range(len(elements)):
        largest_elements.append(max(elements))
        elements.remove(elements[elements.index(max(elements))])
        if len(largest_elements) == n:
            return sorted(largest_elements)
        
        
print(largest(7,[9,1,50,22,3,13,2,63,5]))