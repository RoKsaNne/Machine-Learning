import pandas as pd
import numpy as np
import os
## compress data file
os.system("gzip -d data.tar.gz")
os.system("tar -xf data.tar")

N = 1000##individulas
M = 4268## SNPs

## load beta marginal information
beta_marginal = pd.read_csv('data/beta_marginal.csv.gz')
beta_marginal.columns = ['SNP', 'beta']
## calculate beta^2
beta_marginal['beta^2'] = beta_marginal['beta']**2

## load LD mateix
LD = pd.read_csv('data/LD.csv.gz')
LD = LD.rename(columns={'Unnamed: 0': 'SNP'})
LD = LD.set_index('SNP')
ld_matrix = LD.to_numpy()

## compute l_j = sum (r_jk)^2
l = np.sum(np.square(ld_matrix),axis = 0)
## sum l_j^2/M
denominator = np.sum(np.divide(np.square(l),M))
## sum (l_j * (beta_j^2-1/N))
numerator = np.sum(np.multiply(l,[beta_square -1/N for beta_square in beta_marginal['beta^2'].tolist()]))

heritability = numerator/denominator

print("The estimated heritability of phenotype is:", heritability)
### The estimated heritability of phenotype is: 0.19017122782624735