def filter_list(list):
    return [x for x in list if type(x) == int]

f = filter_list([1,2,'a','b',2,111,'234234','s'])
print(f)


def get_count(inputStr):
    return len([x for x in inputStr if x in ('iIeEOoAauU')])
    # your code here

f = get_count('afdsdbnqwfosdifasbvqefsadgas')
print(f)



def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i,c in enumerate(s))

print(accum('ZpglnRxqenU'))



def high(x):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    dict_alpha = {x:alpha.index(x) +1 for x in alpha}
    sum = 0
    result = ''
    result_dict = {}
    for text in x+' ':
        if text != ' ':
            sum += dict_alpha[text]
            result +=  text
        else:
            result_dict[result] = sum
            result  +=  ' '
            sum = 0
            result = ''
    return (list(result_dict.keys())[list(result_dict.values()).index(max(result_dict.values()))])


print(high('what time are we climbing up the volcano'))


def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
print(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))

def solution(s):
    return [s[i]+'_' if len(s[i:]) == 1 else s[i:i+2]
            for i in range(0, len(s), 2)]


print(solution('abc'))
print(solution('abcdef'))

def solution(s):
    return ''.join(' ' + l if l.upper() == l else l for l in s)

print(solution('breakCamelCase'))


def find_uniq(arr):
    result = {}
    for num in arr:
        if num in result:
            result[num] += 1
        else:
            result[num] = 1

    result = sorted(result.items(),key=lambda row:row[1],reverse=True)
    return result[-1][0]
print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))

def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b

print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))