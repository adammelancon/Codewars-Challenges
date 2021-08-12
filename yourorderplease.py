# https://www.codewars.com/kata/55c45be3b2079eccff00010f

def order(sentence):
  words = sentence.split()
  #numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  wordindex = []
  for i in words:
      for x in i:
          if x.isdigit():
              wordindex.append(x)
  sortedwords = sorted(zip(wordindex, words))
  sentence = []
  for x in sortedwords:
      sentence.append(str((x[1])))
  print(" ".join(sentence))
  output = " ".join(sentence)
  return output
  

order("is2 Thi1s T4est 3a")#, "Thi1s is2 3a T4est")
order("4of Fo1r pe6ople g3ood th5e the2")#, "Fo1r the2 g3ood 4of th5e pe6ople")
order("")#, "")