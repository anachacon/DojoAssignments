# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}


def tuplesOut(my_dict):
    my_List=[]
    for key, value in my_dict.items():
        my_List.append((key, value))
    return (my_List)

print(tuplesOut(my_dict))

#function output
#[("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]