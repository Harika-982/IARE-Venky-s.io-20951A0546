
def reverse_string(s):
    return s[::-1]

def reverse_paragraph(paragraph):
    words = paragraph.split()
    if len(words) == 0:
        return ""
    elif len(words) == 1:
        return reverse_string(words[0])
    else:
        return reverse_string(words[-1]) + " " + reverse_paragraph(" ".join(words[:-1]))

paragraph = input("Enter your string that be reversed:")
reversed_paragraph = reverse_paragraph(paragraph)
print(reversed_paragraph)
