import math 

#Inputs: a list [prices] of at least two prices
#Outputs: a list of len(prices)-1, one entry per consecutive pair. The simple returns are (p_1-p_0)/p_0, and the log returns are ln(p_1/p_0)
#Assumptions: Every price is stictly positive. Any other values will raise a ValueError
#Test: Prices 100, 110, and 99 give the simple returns .10 and -.10, and log_returns sums to ln(99/100)

def simple_returns(prices):
    if not all(p > 0 for p in prices) or len(prices) < 2:
        raise ValueError("Prices must be strictly positive and there must be at least two entries")
    else:
         return [(prices[i+1]-prices[i])/prices[i] for i in range(len(prices)-1)]

def log_returns(prices):
    if not all(p > 0 for p in prices) or len(prices) < 2:
            raise ValueError("Prices must be strictly positive and there must be at least two entries")
    else:
         return [math.log(prices[i+1]/prices[i]) for i in range(len(prices)-1)]