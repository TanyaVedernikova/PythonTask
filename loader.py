from user import User
import threading


class IteratorForReallyBigResponse:

    def __init__(self, start_offset, finish_offset):
        self.token = User.make_auth()
        self.start_offset = start_offset
        self.finish_offset = finish_offset
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        resp = User.make_req(self.token, self.start_offset)
        self.count = resp.get("count")
        if resp.get("results") and self.start_offset != self.finish_offset:
            self.start_offset += 100
            return resp
        raise StopIteration


def loader(iterator: IteratorForReallyBigResponse):
    for resp in iterator:
        f = open('text.txt', 'a', encoding="utf-8")
        f.write(str(resp))


def count_of_all_answer():
    resp = IteratorForReallyBigResponse(0, 1)
    resp.__next__()
    count = resp.count
    return count


if __name__ == '__main__':
    count_of_threads = 100
    count_of_answer = count_of_all_answer()
    value_of_step = count_of_answer // count_of_threads + 1
    thread_jobs = []
    for z in [i * value_of_step for i in range(count_of_threads)]:
        p = threading.Thread(target=loader, args=(IteratorForReallyBigResponse(z, z + value_of_step),))
        thread_jobs.append(p)
        p.start()
    for p in thread_jobs:
        p.join()
