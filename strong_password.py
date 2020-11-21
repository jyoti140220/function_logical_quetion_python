def strong_password(s):
    if len(s)>=6 and len(s)<=16:
          if "@" in s  and 'A' in s or 'Z' in s and "2" in s or "8" in s:
	           print("strong possword")
          else:
  	         print("not strong")
    else:
	     print("not stron")
s=input("enter the password :")
strong_password(s)
