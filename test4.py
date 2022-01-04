# # Time
# import time as t

# time_now=t.localtime()
# print(time_now.tm_hour)
# print(t.time())
# t.sleep(5)
# print(t.localtime())

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [95656, 43234, 324324, 324243]

plt.plot(x, y)
legend = ['Jan', 'Feb', 'Mar', 'Apr']
plt.xticks(x, legend)
plt.bar(x, y)
plt.ylabel('Sales')
plt.xlabel('Months')
plt.show()