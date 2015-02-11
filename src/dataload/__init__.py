from __future__ import print_function
import time

from utils.common import timesofar
from utils.mongo import get_src_db


def load_source(collection_name, src_module):
    src_db = get_src_db()
    target_coll = src_db[collection_name]
    t0 = time.time()
    cnt = 0
    src_data = src_module.load_data()
    for doc in src_data:
        target_coll.insert(doc, manipulate=False, check_keys=False, w=0)
        cnt += 1
        if cnt % 100000 == 0:
            print(cnt, timesofar(t0))
    print("successfully loaded %s into mongodb" % collection_name)
    print("total docs: {}; total time: {}".format(cnt, timesofar(t0)))
