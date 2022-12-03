import sys
import string


def cleanword(s):
    temp = ""
    for letter in s:
        if letter not in string.punctuation:
            temp += letter
    return temp
    # return "".join(s.split(string.punctuation))


def has_dashdash(s):
    if "--" in s:
        return True
    return False


def cleansentence(s):
    temp = ""
    for i in s:
        if i not in string.punctuation:
            temp += i
        else:
            temp += " "
    return temp

def extract_words(s):
    return ((cleansentence(s)).lower()).split()


def wordcount(w, s):
    count = 0
    for i in range(len(s)):
        if s[i] == w:
            count += 1
    return count


def wordset(l):
    temp = []
    for i in range(len(l)):
        if l[i] not in temp:
            temp.append(l[i])
    temp.sort()
    return temp


def longestword(l):
    temp = 0
    for i in range(len(l)):
        if len(l[i]) >= temp:
            temp = len(l[i])
    return temp


def test(did_pass):
    linenum = sys._getframe(1).f_lineno  # get the caller's line number
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def test_suite():
    test(cleanword("what?") == "what")
    test(cleanword("'now!'") == "now")
    test(cleanword("?+='w-o-r-d!,@$()'") == "word")
    test(has_dashdash("distance--but"))
    test(not has_dashdash("several"))
    test(has_dashdash("spoke--"))
    test(has_dashdash("distance--but"))
    test(not has_dashdash("-yo-yo-"))
    test(extract_words("Now is the time!  'Now', is the time? Yes, now.") == ['now', 'is', 'the', 'time', 'now', 'is',
                                                                              'the', 'time', 'yes', 'now'])
    test(extract_words("she tried to curtsey as she spoke--fancy") == ['she', 'tried', 'to', 'curtsey', 'as', 'she',
                                                                       'spoke', 'fancy'])
    test(wordcount("now", ["now", "is", "time", "is", "now", "is", "is"]) == 2)
    test(wordcount("is", ["now", "is", "time", "is", "now", "the", "is"]) == 3)
    test(wordcount("time", ["now", "is", "time", "is", "now", "is", "is"]) == 1)
    test(wordcount("frog", ["now", "is", "time", "is", "now", "is", "is"]) == 0)
    test(wordset(["now", "is", "time", "is", "now", "is", "is"]) == ["is", "now", "time"])
    test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) == ["I", "a", "am", "is"])
    test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) == ["a", "am", "are", "be", "but", "is", "or"])
    test(longestword(["a", "apple", "pear", "grape"]) == 5)
    test(longestword(["a", "am", "I", "be"]) == 2)
    test(longestword(["this", "supercalifragilisticexpialidocious"]) == 34)
    test(longestword([]) == 0)


test_suite()