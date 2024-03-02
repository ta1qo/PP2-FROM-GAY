def test(testTuple, testNumber):
    if all(testTuple):
        print(testNumber + " is passed!")
    else:
       print(testNumber + " is not passed!")
        
test((True, True, None), "test1")
test((False, True, False), "test2")
test((True, True, True), "test3")

