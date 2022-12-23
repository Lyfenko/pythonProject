#urlib

# from urllib.request import urlopen
#
# page = urlopen("http://www.google.com.ua")
#
# content = page.read()
#
# print(page.headers)
# print("")
# print(content)


#dis

# import dis
#
# def greet(name):
#     print(f"Hello {name}")
#
# def test(number):
#     return (str(number) + str(number))
# dis.dis(greet)
#
# dis.dis(test)

# pip instal emoji
# from emoji import emojize

# print(emojize(":thumbs_up:"))

# from collections import namedtuple

# Point = namedtuple("Point", ["x","y"])

# point = Point(2,5)

# print("point", point)

# print("point x ", point.x)
# print("point y ", point.y)
# print("point inx ", point[0])

# # generator expression
# from collections import namedtuple
# # Point = namedtuple("Point", (field for field in "xy"))
# # print(Point(2,5))

# Human = namedtuple("Employee", "name position", defaults=["Python developer"])
# human = Human("Alisa")
# # print(human)

# # print(human._asdict())

from collections import deque

# ticket_queue = deque()
# print(ticket_queue)

# ticket_queue.append("Alisa")
# ticket_queue.append("Bob")
# ticket_queue.append("Dmytro")

# print(ticket_queue)

# one = ticket_queue.popleft()
# print(one)
# two = ticket_queue.popleft()
# print(two)
# three = ticket_queue.popleft()
# print(three)

# recent_pages = deque(["main_page", "shop", "order"], maxlen=3)
# recent_pages.appendleft("cart")
# print(recent_pages)

# from collections import OrderedDict

# employees = OrderedDict()

# employees["developer"] = "1000-2000"
# employees["qa"] = "500-1000"
# employees["pm"] = "1500-2500"
# employees["ba"] = "2000+"

# for empl, salary in employees.items():
#     print(empl, "->", salary)

# cart = {"toys": "cars", "color": "orange"}

# # print(cart["items"])
# print(cart.get("items", 2))
# # cart.setdefault("items", "2")
# print(cart)

from collections import defaultdict

# cars = defaultdict(int)

# cars["mercedes"]
# print(cars)
# cars["mercedes"] +=1
# cars["audi"] +=1
# cars["mercedes"] +=1
# cars["audi"] +=1
# cars["mercedes"] +=1

# print(cars)

# cars = [
#     ("mersedes", "s600"),
#     ("mersedes", "G"),
#     ("mersedes", "A"),
#     ("Audi", "a100"),
#     ("Audi", "a8")
# ]

# cars_sallon = defaultdict(list)

# for car, model in cars:
#     cars_sallon[car].append(model)

# print(cars_sallon)

# from collections import ChainMap

# cmd_proxy = {} # user doesnt provide a proxy
# dev_proxy = {"proxy": "proxy.dev.com"}
# prod_proxy = {"proxy": "proxy.prod.com"}

# configuration = ChainMap(cmd_proxy, dev_proxy, prod_proxy)
# configuration["proxy"]

# print(configuration)