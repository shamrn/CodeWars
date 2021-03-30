#TASK In this example you have to validate if a user input string is alphanumeric. The given string is not nil/null/NULL/None, so you don't have to check that.
def alphanumeric(password):
    x = True if password.isalnum() else False
    return x

print(alphanumeric('Hello123'))
print(alphanumeric('Hello_123'))

#TASK сортировка пузырьком

def bubble_sort(n):
    for i in range(len(n) - 1):
        for j in range(len(n)-i-1):
            if n[j] > n[j +1]: n[j] , n[j +1] = n[j +1],n[j]
    return n

print(bubble_sort([2,3,4,1,2,2,3,3,2342,23423,1,4,5,9,1,2,3,4]))


#TASK Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:


def domain_name(url):        #????????????????????????
    import re
    res = re.findall(r'https?://(?:www\.|)([\w.-]+).*',url)
    return res

print(domain_name("http://google.com"))



#TASK
# "one" => 1
# "twenty" => 20
# "two hundred forty-six" => 246
# "seven hundred eighty-three thousand nine hundred and nineteen" => 783919


def parse_int(string): #???
    num_string = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
                "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
                "seventeen": 17, "eigthteen": 18, "nineteen": 19,"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
                  "sixty": 60, "seventy": 70, "eighty": 80,"ninety": 90,"hundred": 100, "thousand": 1000, "million": 1000000}

    for let in string.split():
        print(num_string[let])

print(parse_int('two hundred forty-six'))
