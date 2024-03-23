import os

badhash = input('Enter the bad commit hash: ')
goodhash = input('Enter the good commit hash: ')
test_command = 'python manage.py test'

os.system(f'git bisect start {badhash} {goodhash}')

os.system(f'git bisect run {test_command}')

os.system(f'git bisect reset')

print('Done.')
