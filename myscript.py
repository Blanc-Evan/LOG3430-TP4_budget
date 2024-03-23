import os

badhash = 'c1a4be04b972b6c17db242fc37752ad517c29402'
goodhash = 'e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c'

test_command = 'python manage.py test'

os.system(f'git bisect start {badhash} {goodhash}')

os.system(f'git bisect run {test_command}')

os.system(f'git bisect reset')

print('Done.')
