
import threading

def reverse_string(s):
    return s[::-1]

def reverse_word(word, result_list):
    reversed_word = reverse_string(word)
    result_list.append(reversed_word)

def reverse_paragraph(paragraph):
    words = paragraph.split()
    result = []
    threads = []
    for word in words:
        thread = threading.Thread(target=reverse_word, args=(word, result))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    return " ".join(result)

paragraph = input("Enter your string that to be reversed:")
reversed_paragraph = reverse_paragraph(paragraph)
print(reversed_paragraph)
