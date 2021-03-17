import matplotlib.pyplot as plt
import numpy as np
# Input numbers
gene_lengths = [9410, 394141, 4442, 105338,
                19149, 76779, 126550, 36296, 842, 15981]
exon_counts = [51, 1142, 42, 216, 25, 650, 32533, 57, 1, 523]
# change the form in to which can use computations
gene = np.array(gene_lengths)
exon = np.array(exon_counts)
a = gene / exon  # get average exon legth
a.sort()  # sort average exon
print(a)
plt.boxplot(a,
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=False,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch=False,
            )
plt.title('Average axon legth')
# define the boxplot
plt.show()
