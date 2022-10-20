"""
graph point with input then get distance for each point if the data is letter change to number with ceaser cipher and the cipher key = 0, a will now = 1. 
"""
import math

ogpoint = (5,6)
#turn text data into number data
def ceas(string):
    news = ""
    for i in string:
        number = (ord(i) - 96)
        news += str(number)
    return news

#calculate length distance between points and return a float value
def pt(pt1 : tuple, pt2 : tuple):
    pt1 = [pt1]
    pt2 = [pt2]
    x1 = pt1[0][0]
    y1 = pt1[0][1]
    x2 = pt2[0][0]
    y2 = pt2[0][1]
    tops = (y2-y1)
    bottom = (x2-x1)
    tops = tops**2
    bottom = bottom**2
    addfinal = tops + bottom
    final = [math.sqrt(addfinal), pt2]
    return final

#goes through the list of points and finds what is closest
def findclosest(allpts):
    total = []
    for i in allpts:
        total.append(i[0])
    pts = total
    print(pts)
    if pts[0] == pts[1]:
        print(pts[0])
        print("First Two Are The Same")
    else:
        print(pts[0])

def datatopts():
    #turn passing data into float
    pass

#madeup points
w1 = pt(ogpoint, (4, 5))
w2 = pt(ogpoint, (3, 4))
w3 = pt(ogpoint, (6, 9))
w4 = pt(ogpoint, (7, 4))
w5 = pt(ogpoint, (-9, 2))
w7 = pt(ogpoint, (8, 2))
#pass points into list
totalpts = [w1, w2, w3, w4, w5, w7]
#pass into function
findclosest(totalpts)
