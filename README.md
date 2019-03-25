# How to start
1. Install and activate the MNE enviorment in anaconda:
```
conda env create -f environment.yml
conda activate mne
```
2. Download the dataset from [here](https://archive.ics.uci.edu/ml/machine-learning-databases/eeg-mld/eeg_full.tar).
3. Decompress the full_eeg.tar file in the working directory.
4. In the command line run:
```
python
from extract_load_eeg_dataset import extract_dataset
extract_dataset('eeg_full', remove = True)
```
5. Use jupyter notebook to start the alcohol_abuse_eeg_classification notebook.
