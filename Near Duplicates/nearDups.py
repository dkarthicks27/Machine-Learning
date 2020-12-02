from itertools import repeat
from datasketch import MinHash, MinHashLSH
import time
import multiprocessing as mp
from pandas import DataFrame as df
from tqdm import tqdm
from glob import glob


def minHashing(Parameters, size=5):
    """
    This function reads a file, generates its minhash and at last adds that to our index which is stored in the master dictionary

    :param Parameters: a dictionary with 3 key, value pair d: master dictionary, file: filepath of a document, doc_id: Document id (by default it is the filepath)
    :param size: it is the shingle size
    :return: none
    """
    d = Parameters['Dict']
    file = Parameters['filepath']
    doc_id = Parameters['Doc_id']
    with open(file, errors="ignore") as f1:
        buf = f1.read().lower()  # read entire file
    array = []
    for y in range(0, len(buf) - size + 1):
        array.append(buf[y:y + size])
    stream_set = set(array)
    minhash = MinHash(num_perm=256)
    for x in stream_set:
        minhash.update(x.encode('utf8'))
    d[doc_id] = minhash


def create_candidate_pairs(queryDict, threshold):
    """
    It creates an csv file as output for all the duplicate document pairs based on the threshold given

    :param queryDict: Dict  --This is our index created stored in master or manager dictionary
    :param threshold: float -- the threshold of the document  above which it is considered duplicate
    :return: none
    """
    similarity = []
    for query in queryDict.keys():
        bucket = lsh.query(queryDict[query])

        if len(bucket) > 1:
            _a = bucket[0]
            for value in bucket[1:]:
                _b = value
                if queryDict[query].jaccard(queryDict[_b]) >= threshold:
                    similarity.append((_a, _b, queryDict[query].jaccard(queryDict[_b])))

        if len(similarity) == 1000:
            my_df = df(similarity, columns=['doc_id', 'duplicate_doc', 'similarity_percent'])
            with open('Result.csv', 'a+') as csv_file:
                my_df.to_csv(path_or_buf=csv_file, index=False)
            similarity.clear()
            del my_df

    if len(similarity) > 0:
        my_df = df(similarity, columns=['doc_id', 'duplicate_doc', 'similarity_percent'])
        with open('Result.csv', 'a+') as csv_file:
            my_df.to_csv(path_or_buf=csv_file, index=False)
        similarity.clear()
        del my_df


if __name__ == '__main__':
    t1 = time.time()
    print("processing starts....")

    filePath = glob(r'')  # Enter your filepath of the folder where the text data lies
    # All the files must be of .txt format or any other supported text document format

    print(f'Total there are {len(filePath)} documents\n')

    Dict = mp.Manager().dict()
    NUM_PERMUTATION = 256

    iterable = zip(repeat(Dict, len(filePath)), filePath)
    print(f'{time.time() - t1} secs was taken to initiate\n')

    params = ({
        'Dict': Dict,
        'filepath': x,
        'Doc_id': x
    } for x in filePath)
    print("Starting minhash + shingle creation....")
    with mp.Pool() as pool:
        MAX_COUNT = len(filePath)
        for res in tqdm(pool.imap(minHashing, params), total=MAX_COUNT, desc="Creating Index using Minhash..."):
            if res is not None:
                pass

    print("Completed creating minhash\n")
    t2 = time.time()

    lsh = MinHashLSH(threshold=0.50, num_perm=NUM_PERMUTATION, weights=(0.5, 0.5))
    with lsh.insertion_session() as session:
        for key in tqdm(Dict.keys(), desc="LSH processing..."):
            session.insert(key=key, minhash=Dict[key])

    print(f"{time.time() - t2} secs was taken to create LSH")

    print("\nfinding candidate pairs.....")

    # Outputs the result as csv file
    create_candidate_pairs(Dict, threshold=0.75)  # the default threshold is 0.75 you can change it

    print("\ncandidate pairs done")
    print(f"total time : {time.time() - t1} secs")
