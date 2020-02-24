l1 = ["07895462130","919875641230","9195969878"]
l2 = []
for element in l1:
    if(element.startswith("0")):
        output = "+91 " + element[1:len(element)]
        l2.append(output)
    elif(element.startswith("91") and len(element) > 10):
        output = "+91  " + element[2:]
        l2.append(output)
    elif(element.startswith("91") and len(element) == 10):
        output = "+91  " + element
        l2.append(output)
    else:

        l2.append(element)


print (l2)
#output +91 78954 62130 +91 91959 69878  +91 98756 41230