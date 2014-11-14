s1 = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
]

s2 = [
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen'
]

s3 = [
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety'
]

s4 = [x+'hundred' for x in s1]

sum_s1 = sum(len(x) for x in s1)
sum_s2 = sum(len(x) for x in s2)
sum_s3 = sum(len(x) for x in s3)
sum_s4 = sum(len(x) for x in s4)

print 10*(9*sum_s1 + sum_s2 + 10*sum_s3) + 100*sum_s4 + 9*99*len('and') + len('onethousand')
