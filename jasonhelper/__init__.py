import argparse
import os
import time

## Argparser

def str2slist(s):
    s.replace(' ', '')
    return s.split(',')

def str2ilist(s):
    s.replace(' ', '')
    return [int(c) for c in s.split(',')]

def str2bool(v):
    if v in ['true', 'True']:
        return True
    elif v in ['false', 'False']:
        return False
    else:
        assert(False)

argparser = argparse.ArgumentParser()
argparser.register('type','bool',str2bool)
argparser.register('type','slist', str2slist)
argparser.register('type','ilist', str2ilist)



# Adopted from: http://stackoverflow.com/a/8412405
def rolling_window(l, w_size):
    for i in range(len(l)-w_size+1):
        yield [l[i+o] for o in range(w_size)]


def check_and_create_dir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

# Adopted from: https://stackoverflow.com/a/21894086
class bidict(dict):
    def __init__(self, *args, **kwargs):
        super(bidict, self).__init__(*args, **kwargs)
        self.inverse = {}
        for key, value in self.items():
            self.inverse.setdefault(value,[]).append(key)

    def __setitem__(self, key, value):
        if key in self:
            self.inverse[self[key]].remove(key)
        super(bidict, self).__setitem__(key, value)
        self.inverse.setdefault(value,[]).append(key)

    def __delitem__(self, key):
        self.inverse.setdefault(self[key],[]).remove(key)
        if self[key] in self.inverse and not self.inverse[self[key]]:
            del self.inverse[self[key]]
        super(bidict, self).__delitem__(key)

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

class FtnTimer(object):
    def __init__(self):
        self.tot_time = 0
        self.tot_cnt = 0
        self.curr_time = 0

    def start(self):
        self.start_time = time.clock()

    def end(self):
        end_time = time.clock()
        self.tot_time += end_time - self.start_time
        self.tot_cnt += 1

    def get_result(self):
        if not self.tot_cnt:
            avg_time = None
        else:
            avg_time = self.tot_time / self.tot_cnt
        res = {
            'average_time': avg_time
        }
        return res
