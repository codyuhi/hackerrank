import xml.etree.ElementTree as etree

maxdepth = -1
def depth(elem, level):
    # print("Evaluating:",elem)
    if level == -1:
        level += 1
    global maxdepth
    # your code goes here
    for child in elem:
        depth(child, level + 1)
    if level > maxdepth:
        maxdepth = level
        # print("maxdepth is now",maxdepth)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)