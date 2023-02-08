def unique_chars(s):

    st = str(s)
    i = 0
    for c in st:
        if st.rfind(c,i+1) > 0:
            return "DUPES!"
        i = i + 1
    return "UNIQUE!"

print(unique_chars("ENGINEER"))
print(unique_chars("ABCD"))
print(unique_chars("BNGINEER"))