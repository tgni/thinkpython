from swampy.Lumpy import Lumpy

def ack(m, n):
    lumpy.object_diagram()
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ack(m - 1, 1)
    if m > 0 and n > 0:
        return ack(m - 1, ack(m, n -1))

lumpy = Lumpy()
lumpy.make_reference()

r = ack(3, 4)
print r
