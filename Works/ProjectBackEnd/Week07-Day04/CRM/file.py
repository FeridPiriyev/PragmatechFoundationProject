file=open("sample.json","a")

name=input("ad :")
surname=input("ad :")


stud={
    "ad":name,
    "soyad":surname
}

file.write(f"{stud["ad"]} | {stud["soyad"]} \n")


