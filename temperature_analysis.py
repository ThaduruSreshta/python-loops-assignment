import numpy as np

temps_celcius = np.array([ 22, 25, 28, 24, 26])

temps_F = (temps_celcius * 1.8) + 32

print(f"the temperatures in celcius are {temps_celcius}\n the temperatures in fahreinheit are {temps_F}")
# test_scores question
test_scores=np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])

print(f"the shape of the array{test_scores.shape}\nthe total number of elements in the array are{len(test_scores)}\nthe highest score is {np.max(test_scores)}\nthe lowest score is{np.min(test_scores)}\n the range of scores is{np.max(test_scores) - np.min(test_scores)}")
# comparing coputing cost of numpy arrays and python lists
import numpy as np
import time
arrange_np=np.arange(50001)
arrangement=list(range(1,50001))
np.sum(arrange_np)
print(f"sum using numpy array is{np.sum(arrange_np)}\nnumpy time is{time.time()}")
sum(arrangement)
print(f"sum using list is{sum(arrangement)}\nlist time is{time.time()}")


