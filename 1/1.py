alphabet = ''.join([chr(i) for i in range(ord('a'), ord('z') + 1)])

def count_uniq(s):
    return len(set(s))

def numbers_sum(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number = number // 10
    return sum


def hash(params) -> int:
    h = count_uniq(''.join(params[0:3]))
    h += numbers_sum(int(''.join(params[3:5]))) * 64
    h += (alphabet.find(params[0][0].lower()) + 1) * 256
    h = format(h, 'X')[-3:].zfill(3)
    return h
ans = []
count_candidats = int(input())
for _ in range(count_candidats):
    candidate_params = input().split(',')
    ans.append(hash(candidate_params))

print(' '.join(ans))
