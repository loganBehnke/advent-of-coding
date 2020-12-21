
# baglist is {container : [(num , type)]}
def findnumbags(bagType, baglist):
    storedItems = baglist.get(bagType)
    if not storedItems:
        return 0
    count = 0
    for item in storedItems:
        num = item[0]
        currentBag = item[1]
        count = count + (num * findnumbags(currentBag, baglist)) + num
        #print(currentBag, count)
    return count


if __name__ == "__main__":
    with open("d7_input.txt") as reader:
        text = reader.read()

    rules = text.split('.\n')
    baglst = {}
    for rule in rules:
        container, stored = rule.split('contain')
        stored = stored.strip().strip('.').split(', ')
        container = container.strip().rstrip('s')
        newLst = []
        for item in stored:
            if item == 'no other bags':
                break
            num = int(item[:2])
            bag = item[2:].rstrip('s')
            newLst.append((num, bag))
        baglst[container] = newLst
    # print(baglst)
    # count = 0
    # index = 0
    # notFound = True
    # bagLst = ['shiny gold bag']
    # while notFound:
    #     notFound = False
    #     for rule in rules:
    #         container, stored = rule.split('contain')
    #         stored = stored.strip().strip('.').split(', ')
    #         for item in stored:
    #             if item[2:].rstrip('s') in bagLst:
    #                 # print(bagLst)
    #                 if container.strip().rstrip('s') not in bagLst:
    #                     bagLst.append(container.strip().rstrip('s'))
    #                     print(container.strip().rstrip('s'))
    #                     notFound = True
    #     count += 1
    #     # print(bagLst)
    # # print(bagLst)
    # print(len(bagLst) - 1)
    #(1, 'dark olive bag')
    # baglst = {"shiny gold bag": [
    #     (2, 'vibrant plum bag')],
    #     "vibrant plum bag": [(5, 'faded blue bag'), (6, 'dotted black bag')],
    #     "dark olive bag": [(3, 'faded blue bag'), (4, 'dotted black bag')],
    #     'faded blue bag': [],
    #     'dotted black bag': []}
    print(findnumbags('shiny gold bag', baglst))
