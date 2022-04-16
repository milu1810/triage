import pandas as pd
import numpy as np
import matplotlib
import time
import matplotlib.pyplot as plt

dc = pd.DataFrame(np.sort(np.random.randint(1,50,2000)))
da = pd.DataFrame(np.random.randint(1,50,2000))
dd = pd.DataFrame(np.sort(np.random.randint(1,50,2000))[::-1])
dc.to_csv('fichier1.csv', index=False)
da.to_csv('fichier2.csv', index=False)
dd.to_csv('fichier3.csv', index=False)


start = time.time()
B = np.sort(dc, axis=-1, kind='quicksort')
end = time.time()
print(B)

tpp = end-start

dt = pd.DataFrame(tpp)
print(tpp)
plt.plot()
plt.show()


