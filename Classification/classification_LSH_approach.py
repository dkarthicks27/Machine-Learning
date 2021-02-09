import glob
from pprint import pprint
from datasketch import MinHash, MinHashLSH
import time
import multiprocessing as mp
from tqdm import tqdm


def minhash_operation(parameter, size=5):
    file = parameter['param1']
    d = parameter['param2']
    with open(file, errors="ignore") as f1:
        buf = f1.read()  # read entire file
    array = []
    for y in range(0, len(buf) - size + 1):
        array.append(buf[y:y + size])
    stream_set = set(array)
    minhash = MinHash(num_perm=256)
    for x in stream_set:
        minhash.update(x.encode('utf8'))
    d[file] = minhash


def similarities(queryFilepath, LSH):
    result = dict()
    for qry in queryFilepath:
        bucket = LSH.query(qry)
        if len(bucket) > 1:
            for i in bucket[1:]:
                if not result.get(i):
                    result[i] = Dict[i].jaccard(qry)
                else:
                    result[i] = (result[i] + Dict[i].jaccard(qry)) / 2
    return result


if __name__ == '__main__':
    t1 = time.time()
    print("processing starts....")

    k = glob.glob(r'/OneDoc/*.txt')  # Full filePath is required for processing this

    '''
        INPUT: for classification we will be given a list of documents doc_id and a list of corresponding labels
    ex: list1 = ['101.txt', '102.txt', '109.txt', '201.txt', '391.txt']     list2 = [1, 1, 2, 2, 1]
    given this we have to classify all other documents either as class 1 or class 2 and their similarity percent

        For all the documents in the training dataset list1 we can find the elements in its bucket and
    store it in a dictionary, here the key will be the doc_id and similarity percent will be the value
    as soon as we see the document again we will simply take the average the value of the similarity percent
    we will do this for all the elements of list1'''

    Dict = mp.Manager().dict()
    NUM_PERMUTATION = 256

    params = ({
        'param1': x,
        'param2': Dict
    } for x in k)
    print(f'{time.time() - t1} secs was taken to initiate\n')

    print("Starting minhash + shingle creation....")

    with mp.Pool() as p:
        MAX_COUNT = len(k)
        for res in tqdm(p.imap(minhash_operation, params), total=MAX_COUNT):
            pass

    print("Completed creating minhash\nIndexing documents complete")
    t2 = time.time()

    lsh = MinHashLSH(threshold=0.50, num_perm=NUM_PERMUTATION, weights=(0.5, 0.5))
    with lsh.insertion_session() as session:
        for key in tqdm(Dict.keys(), desc="LSH processing"):
            session.insert(key=key, minhash=Dict[key])

    query = ['/OneDoc/120.txt', '/OneDoc/123.txt',
             '/OneDoc/117.txt']  # using the first ten documents in the k and seeing
    print(query)
    query = [Dict[i] for i in query]
    print(f"{time.time() - t2} secs was taken to create LSH")

    print("\nfinding candidate pairs.....")
    res = similarities(query, lsh)
    pprint(res)
    with open('result.csv', 'w') as f:
        for key in res.keys():
            f.write("%s,%s\n" % (key, res[key]))
    print("\ncandidate pairs done")
    print(f"total time : {time.time() - t1} secs")
