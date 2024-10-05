print("Welcome to the average of the player in cricket by runs")
tr = []
mn = 1
q = 0

while True:
    runofm = input(f"Enter the runs of him in {mn} match(enter q to stop)")
    if runofm=="q":
        break
    runofm = int(runofm)
    mn = mn+1
    tr.append(runofm)
while True:
    tn = tr[q] + tr[q+1]
    q+1
print(tn)
average = int(tn/(len(tr)+1))
print(f"The average of player is {average}")
