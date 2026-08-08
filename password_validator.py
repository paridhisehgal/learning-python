while True:
   password =input("\nEnter your password ->")
   failures = []

   if len(password ) < 8:
    failures.append("Password must contain atleast 8 characters.")
   if not any(char.isdigit() for char in password):
     failures.append("Password must contain atleast one digit.")
   if not any(char.isupper() for char in password):
    failures.append("Password must contain atleast one uppercase letter.")
   if failures:
     for message in failures:
      print("\n",message)
   else:
    print("Password accepted!")
    break



