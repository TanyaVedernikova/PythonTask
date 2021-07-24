from user import User
import multiprocessing


class IteratorForReallyBigResponse:

    def __init__(self, start_offset, finish_offset):
        self.token = User.make_auth()
        self.start_offset = start_offset
        self.finish_offset = finish_offset

    def __iter__(self):
        return self

    def __next__(self):
        resp = User.make_req(self.token, self.start_offset)
        if resp.get("results") and self.start_offset != self.finish_offset:
            self.start_offset += 100
            return resp
        raise StopIteration


def loader(iterator: IteratorForReallyBigResponse):
    for resp in iterator:
        f = open('text.txt', 'a', encoding="utf-8")
        f.write(str(resp))


if __name__ == '__main__':
    Process_jobs = []
    for z in [0, 5000, 10000]:
        p = multiprocessing.Process(target=loader, args=(IteratorForReallyBigResponse(z, z+5000),))
        Process_jobs.append(p)
        p.start()
    for p in Process_jobs:
        p.join()