import mystuff

# dict style
my_stuff = {'apple':'I AM APPLES!'}
print("DICT STYLE: ", my_stuff['apple'])

# module style
mystuff.apple()
print("MODULE STYLE: ", mystuff.tangerine)

# class style
thing = mystuff.MyStuff()
thing.apple()
print(thing.tangerine)