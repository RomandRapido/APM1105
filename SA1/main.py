import requests
url = 'https://raw.githubusercontent.com/AllenDowney/ThinkPython2/master/code/words.txt'
response = requests.get(url)
if response.status_code == 200:
    with open('words.txt', 'wb') as f:
        f.write(response.content)
        print('Dataset saved to file.')
else:
    print('Failed to download dataset.')

with open('words.txt', 'r') as file:
    contents = file.read()
    print('A. Print the total number of words in the file.')
    words = contents.split()
    print(f'Total no. of words: {len(words)}')

    print('B. Print the longest word in the file.')
    longest_word = max(words, key=len)
    print(f'Longest word: {longest_word}')

    print('C. Print the number of words that start with a certain letter (use user input).')
    let_start = input("Enter a letter: ").lower()[0]
    count_start = 0
    for word in words:
        if word.startswith(let_start):
            count_start += 1
    print(f'No. of words that starts with {let_start}: {count_start}')

    print('D. Print all the words that contain a certain substring (use user input).')
    sub_string = input("Input sub-string: ").lower()
    string_with_sub_string = [print(word) for word in words if sub_string in word]

    print('E. Print all the words that are palindromes (i.e., read the same backwards and forwards).')
    palindromes = [print(word) for word in words if word == word[::-1]]

    print(f'F. Count the frequency of each letter.')
    alpha_count = {}
    for word in words:
        for letter in word:
            if letter in alpha_count:
                alpha_count[letter] += 1
            else:
                alpha_count[letter] = 1
    sorted_alpha_count_key = sorted(alpha_count.keys())
    sorted_alpha_count = {key: alpha_count[key] for key in sorted_alpha_count_key}
    print(sorted_alpha_count)