from math import inf
def nextGreaterElements(nums):
    maximum = -inf
    for i, n in enumerate(nums):
        if n > maximum:
            maximum = n
            max_i = i
    i = (max_i - 1) % len(nums)
    next_greaters = [maximum]
    arg_max = [max_i]
    for j in range(len(nums) - 1):
        curr = nums[i]
        if curr < next_greaters[-1]:
            nums[i] = next_greaters[-1]
            next_greaters.append(curr)
        else:
            while curr >= next_greaters[-1]:
                if curr != maximum:
                    next_greaters.pop()
                else:
                    arg_max.append(i)
                    break
            nums[i] = next_greaters[-1]
            next_greaters.append(curr)
        i -= 1
    for i in arg_max:
        nums[i] = -1
    return nums
