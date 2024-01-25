line = input('Enter the String: ')
n = int(input('Enter the number of words: '))

words= []
print('Input the dictionary: ')
for i in range (n):
    word = input()
    words.append(word)

input_len = len(line)

print('\n')

# def split_string_line(line, words):
#     for i in range(input_len):
#         word1 = line[(slice(0, i))]
#         word2 = line[(slice(i, input_len-1))]
#         if(word1 in words):
#             if((word2 in words) or len(word2)==0):
#                 return True
#             elif split_string_line(word2, words):
#                 return True
#         else:
#             return False

def split_string_line(line, words):
    if not line:
        return True  # An empty string can always be segmented

    for i in range(1, len(line) + 1):
        word1 = line[:i]
        word2 = line[i:]
        if word1 in words and split_string_line(word2, words):
            return True

    return False

if split_string_line(line, words):
    print('Yes')
else:
    print('No')