#7. Remove dollar sign
def remove_dollar_sign(s):
    if "$" in s:
        s_new = s.replace("$","")
    else:
        pass
    return(s_new)
# print(remove_dollar_sign("$abcd"))

#8. Debug code
string_with_no_dollars = remove_dollar_sign("$80% percent of $life is to show $up")
if string_with_no_dollars == "80% percent of life is to show up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")

#9. Extract item from integer list

def get_even_list(a_list):
    even_list = []
    for i in a_list:
        if i%2 == 0:
            even_list.append(i)
    return(even_list)
int_list = [4,3,2,1]

# print(get_even_list(int_list))

#10. Check function get_even_list:

string_with_no_dollars = remove_dollar_sign("$80% percent of $life is to show $up")
if string_with_no_dollars == "80% percent of life is to show up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")

#11. Write a function named is_inside

def is_inside(x=[0,0],y=[0,0,0,0]):
    if (len(x)==2 and len(y)==4) == False:
        return False
    else:
        x_axis = (x[0]>y[0]) and (x[0]<y[0]+y[2])
        y_axis = (x[1]>y[1]) and (x[1]<y[1]+y[3])
        if (x_axis and y_axis) == False:
            return False
        else:
            return True
print(is_inside([200, 120], [140, 60, 100, 200]))
print(is_inside([100, 120], [140, 60,  ] ))