lang1 = {"C", "C++", "Java", "Python"}
print ("lang1: ", lang1, "id(lang1): ", id(lang1))
lang2 = lang1.copy()
print ("lang2: ", lang2, "id(lang2): ", id(lang2))
lang1.add("PHP")
print ("After updating lang1")
print ("lang1: ", lang1, "id(lang1): ", id(lang1))
print ("lang2: ", lang2, "id(lang2): ", id(lang2))