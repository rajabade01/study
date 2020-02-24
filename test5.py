# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

#Example 1:
#Input: [2,2,1]
#Output: 1

#Example 2:
#Input: [4,1,2,1,2]
#Output: 4


def return_single_interger_list(li):
    output = []
    for element in li:
        if(li.count(element) == 1):
            output.append(element)
    return output

if __name__ == "__main__":
    li = [-1,0,1,1,1.5,1.5]
    output = return_single_interger_list(li)
    print(output)