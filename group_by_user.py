# user id is index 7
# cluster is 23

users = {}

with open("data/train.csv", "r") as f:
  for line in f:
    print "..."
    cols = line.split(",")
    userid = cols[7]
    cluster = cols[23]

    if userid in users:
      users[userid].append(line)
    else:
      users[userid] = [line]

print len(users)