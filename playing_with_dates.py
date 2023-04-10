def convert(string):
    a,b,c = string.split(" ")
    months = {
        'Jan':1,
        'Frb':2,
        'Mar':3,
        'Apr':4,
        'May':5,
        'Jun':6,
        'Jul':7,
        'Aug':8,
        'Sep':9,
        'Oct':10,
        'Nov':11,
        'Dec':12
        }
    date =0
    try:
        month = months[b]
    except:
        print("enter valid month")

     #Conditions for year
    if year >1960 and year <2024:
        year=int(c)
    else:
        print("Please Enter valid year")
    if len(a)==3:
        date = int(a[0])
    else:
        date = int(a[0:2])

    # Error values
    if date == 0:
        print("enter valid date")
    else:
        print(str(year)+"-"+str(month)+"-"+str(date))
