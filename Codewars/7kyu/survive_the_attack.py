"""
Given two Arrays in which values are the power of each soldier, return true if you survive the attack or false if you perish.

CONDITIONS

Each soldier attacks the opposing soldier in the same index of the array. The survivor is the number with the highest value.
If the value is the same they both perish
If one of the values is empty(different array lengths) the non-empty value soldier survives.
To survive the defending side must have more survivors than the attacking side.
In case there are the same number of survivors in both sides, the winner is the team with the highest initial attack power. 
If the total attack power of both sides is the same return true.
The initial attack power is the sum of all the values in each array.
"""


def is_defended(attackers, defenders):
    return sum(defenders) >= sum(attackers)