# Near Duplicates Identification 
## This package is based on LSH, which is a probabilistic approach to finding near duplicates from a large dataset

### Advantages:
1. Scalable solution as only a number of documents * are processed at a time in RAM
2. Indexing and searching is very quick especially for very large dataset
3. Can run on multiple cores if your system supports

### Disadvantages:
1. Possibility of False negatives and False positives in the result due to the probabilistic approach
2. For more probable issues please refer to the official Documentation of Datasketch

### Dependencies Required:
1. itertools
2. datasketch
3. time
4. multiprocessing
5. pandas
6. tqdm
7. glob

If any of these are missing use ""pip install dependencyName"" and install them before running the python file

### Reference:
https://github.com/ekzhu/datasketch


