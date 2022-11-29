def names(fname):
    print("The given name is ", fname)

names("shilpa")
names("adam")
names("manu")


# def kids(* fkid):
#     print("the second child is: ",fkid[2])
#
# kids("manu","shilpa","adam")

def kids(child1, child2, child3):
    print("the kids name are:",child1,child2,child3)
kids(child1="shilpa",child2="manu",child3="adam")

def babys(** childs):
    print("the babies:", childs)
babys(childs="manu")
