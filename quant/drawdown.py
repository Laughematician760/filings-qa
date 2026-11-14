#Spec
#Inputs: Must be lists of length >=1, that do not start with a zero value, and have all values of the list nonnegative. 
#Outputs: The range of the function is [-1, 0] and output is a floating point value
#Error Cases: The function will raise an error if the input list 1) has length 0, 
#                                                                2) the initial entry in the input list is 0, 
#                                                                3) there are negative entries in the input list
#Hand-worked tests: drawdown([100, 120, 90, 130]) = -.25, drawdown([100]) = 0, drawdown([100, 100, 10]) = -.9



def drawdown(prices):
    if len(prices) < 1 or prices[0] == 0 or not all(p >= 0 for p in prices):
        raise ValueError("List must be at least length one, have a nonzero first price, and have all entries nonnegative.")
    min_list = [0.0]
    peak = prices[0]
    for i in range(len(prices)-1):
        if peak == prices[i+1]:
            continue
        elif peak < prices[i+1]:
            peak = prices[i+1]
            continue
        else:
            min_list += [(prices[i+1]-peak)/peak]
    return min(min_list)

