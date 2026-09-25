string_input = "this is string for token counter"
count = 0
large= 7
large_count = 0
medium = 5
medium_count = 0
small_count = 0
for i in string_input:
    if i == " ":
        if count >= large:
            large_count += 1
        elif count >= medium:
            medium_count += 1
        else:
            small_count += 1
        count = 0
    count+=1
print("large_count=",large_count)
print("medium_count=",medium_count)
print("small_count=",small_count)