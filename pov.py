import os

#set the environment variable HELLO_WORLD
hello_world = os.environ.get('HELLO_WORLD')

# print the value of the environment variable HELLO_WORLD: should be chacha
print(f'The value of HELLO_WORLD is: {hello_world}')