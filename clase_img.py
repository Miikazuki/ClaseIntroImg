import numpy as np
import matplotlib.pyplot as plt 

print("paquete numpy importado correctamente")
#a = np.array([[255, 0, 255],[255, 0, 255],[255, 0, 255],[255, 0, 255]])
a = np.array([[200, 255, 210],[10, 255, 20],[79, 25, 90],[20, 255, 10]])
print(a)
print(a.shape)
plt.figure(figsize=(5,5))
plt.imshow(a, cmap='gray', vmin=0, vmax=255)
plt.show()