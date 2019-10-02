"""
utility functions for working with DataFrames
"""

import pandas
import seaborn as sns
import matplotlib.pyplot as plt


"""
use seaborn color palette and style for plots
"""
plt.style.use('seaborn')

"""
plot a confusion matrix with labels for easier interpretation
"""


def plot_confusion_matrix(y_true, y_pred):
    labels = unique_labels(y_true)
    columns = [f'Predicted {label}' for label in labels]
    index = [f'Actual {label}' for label in labels]
    table = pd.DataFrame(confusion_matrix(y_true, y_pred),
                         columns=columns, index=index)
    return sns.heatmap(table, annot=True, fmt='d', cmap='viridis')
