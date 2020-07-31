# libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create a dataframe
regions = ('VISUAL [3765]', 'THALAMUS [5848]', 'HPC [3933]', 'PFC [2113]', 'MOTOR [3031]', 'BG [3199])')
accs_uncompressed = (0.512, 0.504, 0.516, 0.555, 0.542, 0.514) #these are the values from not compressing the time bins to a single mean
accs_avgd = (0.518, 0.502, 0.503, 0.513, 0.507, 0.508) #these are the values from avging the time bins to a single mean


df = pd.DataFrame({'group':(regions), 'values':(accs_uncompressed) })

# Reorder it following the values:
ordered_df = df.sort_values(by='values')
my_range=range(1,len(df.index)+1)

# The vertival plot is made using the hline function
# I load the seaborn library only to benefit the nice looking feature
import seaborn as sns


plt.hlines(y=my_range, xmin=0.4, xmax=ordered_df['values'], color='skyblue')
plt.plot(ordered_df['values'], my_range, "o")
plt.axvline(x=0.5, ymin=0, ymax=1, color = 'm', linestyle = 'dotted')

# Add titles and axis names
plt.yticks(my_range, ordered_df['group'])
plt.title("Classifying Miss vs NoGo Responses Using \n Prestimulus Activity (Uncompressed)\n \n ",  loc='center')
plt.xlabel('Accuracy Score of Regression Model')
plt.ylabel('Group [no. of units]')
