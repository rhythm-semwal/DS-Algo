class ItemValue:
    def __init__(self, weight, value, ind):
        self.weight = weight
        self.value = value
        self.ind = ind
        self.cost = float(value) / float(weight)


#     def __lt__(self, other):
#         return self.cost < other.cost

class Solution:
    # @type of weight: list of integers
    # @type of value: list of integers
    # @type of capacity: integer
    # @return type: integer
    @staticmethod
    def letter_cmp(a, b):
        if a.cost > b.cost:
            return -1
        else:
            return 1

    def fractionalKnapsack(self, weight, value, capacity):
        # write your awesome code here
        value_per_weight = []

        for i in range(len(weight)):
            value_per_weight.append(ItemValue(weight[i], value[i], i))

        # value_per_weight.sort(reverse=True)
        from functools import cmp_to_key
        letter_cmp_key = cmp_to_key(self.letter_cmp)
        value_per_weight.sort(key=letter_cmp_key)

        result = 0
        for i in range(len(value_per_weight)):
            current_wt = int(value_per_weight[i].weight)
            current_value = int(value_per_weight[i].value)

            if current_wt <= capacity:
                result += current_value
                capacity -= current_wt
            else:
                result += int(capacity * value_per_weight[i].cost)
                break

        return int(result)