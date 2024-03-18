import os

#set the environment variable HELLO_WORLD
job1_output = os.environ.get('JOB1_OUTPUT')

# print the value of the environment variable HELLO_WORLD: should be chacha
print(f'The value of HELLO_WORLD is: {job1_output}')