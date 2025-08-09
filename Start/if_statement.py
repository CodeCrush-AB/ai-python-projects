
is_male = False

if is_male:
    print("Male")
else:
    print("not Male")

ismale = True
is_tall = True
if ismale and is_tall:
    # for 'or' either have to be true. For 'and' both have to be true
    print("tall male")
elif ismale and not is_tall:
    print("short male")
elif not ismale and is_tall:
    print("long female")
else:
    print("not Male nor Tall")