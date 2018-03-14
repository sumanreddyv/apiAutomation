import pandas as pd
import numpy as np
import xlwings as xw
import win32api
sht = xw.Book().sheets[4]
s = pd.Series([1.1, 3.3, 5., np.nan, 6., 8.], name='myseries')

sht.range('A1').value = s
sht.range('A1:B7').options(pd.Series).value