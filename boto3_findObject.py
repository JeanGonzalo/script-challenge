# Back-end Challenge
# In the Python file, write a program to get all the files 
# from a public S3 bucket named coderbytechallengesandbox. 
# In there there might be multiple files, 
# but your program should find the file with the prefix __cb__,
# and then output the full name of the file. You should use the boto3 module to solve this challenge.

# You do not need any access keys to access the bucket because it is public. This post might help you with how to access the bucket.

# Example Output
# __cb__name.txt
# Example Output with ChallengeToken
# __c___n_me._xth_42n_k69

import requests
import boto3

s3 = boto3.client('s3')

bucket = s3.Bucket('coderbytechallengesandbox')
for obj in bucket.objects.filter(Prefix='__cb__'):
    print(obj.key)

print(s3)