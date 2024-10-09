# Dry run logic:
# i = 0, j = 0, print "i= 0 and j= 0"
# i = 0, j = 1, print "i= 0 and j= 1"
# i = 0, j = 2, print "i= 0 and j= 2"
# i = 0, j = 3, print "i= 0 and j= 3"
# i = 1, j = 0, print "i= 1 and j= 0"
# i = 1, j = 1, print "i= 1 and j= 1"
# i = 1, j = 2, print "i= 1 and j= 2"
# i = 1, j = 3, print "i= 1 and j= 3"
# i = 2, j = 0, print "i= 2 and j= 0"
# i = 2, j = 1, print "i= 2 and j= 1"
# i = 2, j = 2, print "i= 2 and j= 2"
# i = 2, j = 3, print "i= 2 and j= 3"
# i = 3, j = 0, print "i= 3 and j= 0"
# i = 3, j = 1, print "i= 3 and j= 1"
# i = 3, j = 2, print "i= 3 and j= 2"
# i = 3, j = 3, print "i= 3 and j= 3"
for i in range(4):
    for j in range(4):
        print("i=",i," and j=",j)