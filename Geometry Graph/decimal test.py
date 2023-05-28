import matplotlib.pyplot as plt
import numpy as np

for i in range(0, 10, 0.1) :
    print(i)

start_number = 0
end_number = 10
step = 0.1          
number_list = np.arrange(start_number, end_number, step)  # to end in 10, end_number + step
print(number_list)