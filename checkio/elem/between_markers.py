def between_markers(text, begin, end):
    """
        returns substring between two given markers
    """
    begin_index=text.find(begin)+len(begin)
    end_index=text.find(end)
    if begin not in text and end in text:
        return text[0:end_index]
    elif begin in text and end not in text:
        return text[begin_index:]
    elif begin not in text and end not in text:
        return text
    else:
        return text[begin_index:end_index]


print(between_markers("<head><title>My new site</title></head>","<title>", "</title>"))
print(between_markers('No[/b] hi', '[b]', '[/b]'))
print(between_markers('No [b]hi', '[b]', '[/b]'))
print(between_markers('No hi', '[b]', '[/b]'))
print(between_markers('No <hi>', '>', '<'))
print(between_markers("No <hi> one",">","<"))
