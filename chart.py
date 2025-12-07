# chart.py

# Step 1: Import libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Step 2: Generate synthetic monthly revenue data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Assume 3 customer segments: Retail, Wholesale, Online
np.random.seed(42)
data = {
    'Month': months * 3,
    'Revenue': np.concatenate([
        np.random.normal(50000, 5000, 12),   # Retail
        np.random.normal(70000, 7000, 12),   # Wholesale
        np.random.normal(60000, 6000, 12)    # Online
    ]),
    'Segment': ['Retail']*12 + ['Wholesale']*12 + ['Online']*12
}

df = pd.DataFrame(data)

# Step 3: Set Seaborn style and context
sns.set_style('whitegrid')
sns.set_context('talk')  # Presentation-ready text sizes

# Step 4: Create lineplot
plt.figure(figsize=(8, 8))  # 512x512 pixels
lineplot = sns.lineplot(data=df, x='Month', y='Revenue', hue='Segment', marker='o', palette='Set2')

# Step 5: Customize chart
plt.title('Monthly Revenue Trend by Customer Segment', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Revenue ($)', fontsize=14)
plt.xticks(rotation=45)
plt.legend(title='Segment', fontsize=12, title_fontsize=12)
plt.tight_layout()

# Step 6: Save chart as PNG (512x512 pixels)
plt.savefig('chart.png', dpi=64, bbox_inches='tight')
plt.show()
