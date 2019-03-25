# How to start
1. Download the dataset from [here](https://archive.ics.uci.edu/ml/machine-learning-databases/eeg-mld/eeg_full.tar).
2. Decompress the full_eeg.tar file in the working directory.
3. In the command line run:
```
python
from extract_load_eeg_dataset import extract_dataset
extract_dataset('eeg_full', remove = True)
```
4. Use jupyter notebook to start the alcohol_abuse_eeg_classification notebook.