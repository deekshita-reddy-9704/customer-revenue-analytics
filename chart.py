# chart.py

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate synthetic monthly revenue data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

np.random.seed(42)
data = {
    'Month': months * 3,
    'Revenue': np.concatenate([
        np.random.normal(50000, 5000, 12),
        np.random.normal(70000, 7000, 12),
        np.random.normal(60000, 6000, 12)
    ]),
    'Segment': ['Retail']*12 + ['Wholesale']*12 + ['Online']*12
}

df = pd.DataFrame(data)

# Professional Seaborn styling
sns.set_style('whitegrid')
sns.set_context('talk')

# Create the figure
dpi = 64
fig_size_inches = 512 / dpi  # 8 inches
plt.figure(figsize=(fig_size_inches, fig_size_inches), dpi=dpi)

# Create lineplot
sns.lineplot(
    data=df,
    x='Month',
    y='Revenue',
    hue='Segment',
    marker='o',
    palette='Set2'
)

# Customize
plt.title('Monthly Revenue Trend by Customer Segment', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Revenue ($)', fontsize=14)
plt.xticks(rotation=45)
plt.legend(title='Segment', fontsize=12, title_fontsize=12)
plt.tight_layout()

# Save WITHOUT bbox_inches='tight'
plt.savefig('chart.png', dpi=dpi)
plt.show()
