import matplotlib.pyplot as plt

squares = [1,4,9,16,25]
#plt.plot(squares)
#plt.show()

squares = [10,20,30,40,50]
input_value = [10,20,30,40,40]

#plt.plot(squares,linewidth = 5)
plt.scatter(input_value,squares,linewidth = 5)
plt.title("Square Number 虹", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)
plt.show()