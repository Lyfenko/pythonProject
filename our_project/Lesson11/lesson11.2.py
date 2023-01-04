### With Timer()


# class IterNext:
#     def __init__(self, min , max):
#         self.min = min
#         self.max = max
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.min > self.max:
#             raise StopIteration
#         else:
#             self.min += 1
#             return self.min - 1
# my_list = IterNext(1, 20)
# print(list(my_list))
# import time
#
# import time
#
# class Timer:
#     def __init__(self):
#         self._start = None
#         self.elapsed = 0.0
#
#     def start(self):
#         if self._start is not None:
#             raise RuntimeError("Timer has been started")
#         else:
#             self._start = time.perf_counter()
#
#     def stop(self):
#         if self._start is None:
#             raise RuntimeError("Timer not started")
#         end = time.perf_counter()
#         self.elapsed += end - self._start
#         self._start = None
#
#     def __enter__(self):
#         self.start()
#         return self
#
#     def __exit__(self, *args):
#         self.stop()
#
# t = Timer()
# t.__enter__()
# time.sleep(5)
# t.__exit__(None, None, None)
# print(t.elapsed)
#
# class A:
#     num = 2
#
#     def __getattr__(self, name):
#         if name == "string":
#             return "Its string"
#         pass
# a = A()
# print(a.num)
# print(a.string)

# class B:
#     num = 2
#
#     def __getattribute__(self, name):
#         if name == "string":
#             return "Its string"
#         pass
#
# a = B()
# print(a.num)
# print(a.string)

# import os
#
# class Fdict:
#     def __setitem__(self, filename, value):
#         file = open(filename, "w")
#         file.write(value)
#         file.close()
#
#     def __delitem__(self, filename):
#         os.remove(filename)
#
# fd = Fdict()
#
# fd["TEMP_FILE"] = "Hello World"
# del fd["TEMP_FILE"]
#
# from os.path import exists
#
# class Ifilexist:
#     file_path = ""
#
#     def __init__(self, file_path):
#         self.file_path = file_path
#
#     def __bool__(self):
#         return exists(self.file_path)
#
# file = Ifilexist("TEMP_FILE")
# print(bool(file))




