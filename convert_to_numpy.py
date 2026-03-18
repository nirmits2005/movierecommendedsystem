import pickle
import numpy as np
import scipy
import pandas as pd

with open('df.pkl', 'rb') as f:
    df = pickle.load(f)
with open('indices.pkl', 'rb') as f:
    indices_obj = pickle.load(f)
with open('tfidf_matrix.pkl', 'rb') as f:
    tfidf = pickle.load(f)

# Convert dicts
title_to_idx = {}
if isinstance(indices_obj, dict):
    for k, v in indices_obj.items():
        title_to_idx[str(k).strip().lower()] = int(v)
else:
    for k, v in indices_obj.items():
        title_to_idx[str(k).strip().lower()] = int(v)

titles = df['title'].fillna("").apply(str).tolist()

csr = tfidf.tocsr()
csc = tfidf.tocsc()

np.savez_compressed('movie_data.npz',
    csr_data=csr.data,
    csr_indices=csr.indices,
    csr_indptr=csr.indptr,
    csc_data=csc.data,
    csc_indices=csc.indices,
    csc_indptr=csc.indptr,
    # Can't easily save python dict/lists natively in npz without pickling taking over,
    # but object arrays are supported.
)

with open('movie_meta.pkl', 'wb') as f:
    pickle.dump({
        'titles': titles,
        'title_to_idx': title_to_idx,
    }, f)

print("Saved pure-numpy / pure-python equivalents.")
