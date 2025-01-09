translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}
f=input('enter your word: ')
print(translations.get(f, 'Unavailable'))