Sorting dictionary in python

foo = {1:{'user': {'username':'user_a', 'date_joined':'2018-11-03'}, 'other_stuff':{}}, 2:{'user': {'username':'user_a', 'date_joined':'2018-10-03'}, 'other_stuff':{} }}

sorted(foo.values(), key=lambda obj: obj['user']['date_joined'], reverse=True)
