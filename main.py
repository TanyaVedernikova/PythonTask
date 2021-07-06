from user import User
import threading


class LoaderForReallyBigResponse:

    def __init__(self, offset):
        self.token = User.make_auth()
        self.offset = offset

    def __iter__(self):
        return self

    def __next__(self):
        if (self.offset % 10000 == 0) is not True:
            resp = User.make_req(self.token, self.offset)
            if resp.get("results") is not None:
                self.offset += 100
                return resp
            raise StopIteration
        else:
            self.token = User.make_auth()
            resp = User.make_req(self.token, self.offset)
            if resp.get("results") is not None:
                self.offset += 100
                return resp
            raise StopIteration



first_resp = LoaderForReallyBigResponse(0)
# second_resp = LoaderForReallyBigResponse(3000)
# third_resp = LoaderForReallyBigResponse(6000)
#
#
# def start_loader(a, stop_offset):
#     for resp in a:
#         if a.offset < stop_offset:
#             counter = 1
#             print("call next", counter)
#             counter += 1
#             f = open('text.txt', 'a', encoding="utf-8")
#             f.write(str(resp))
#         print("why")
#
#
# x = threading.Thread(target=start_loader, args=(first_resp, 3001))
# y = threading.Thread(target=start_loader, args=(second_resp, 6001))
# z = threading.Thread(target=start_loader, args=(third_resp, 11116001))
# x.start()
# y.start()
# z.start()


for i in first_resp:
    f = open('text.txt', 'a', encoding="utf-8")
    f.write(str(i))