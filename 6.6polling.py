favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }   

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

coders = ['jen', 'sarah', 'edward', 'alex', 'phil', 'flor']

for coder in coders:
    if coder in favorite_languages:
        print (f"Thank you for taking the poll, {coder.title()}.")
    else:
        print(f"{coder.title()}, please take our poll.")