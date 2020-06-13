#!/usr/bin/env python
import sys
import os
from piazza_api import Piazza
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from pprint import pprint

def main():
    p = Piazza()
    p.user_login(email=os.environ['EMAIL'], password=os.environ['PASSWORD'])

    piazza_url = urlparse(sys.argv[1])

    class_id = piazza_url.path.split('/')[2]
    post_num = piazza_url.query.split('=')[1]
    
    # Returns a class network
    class_net = p.network(class_id)

    post = class_net.get_post(post_num)

    question = post["history"][0]["content"]
    subject = post["history"][0]["subject"]

    print("QUESTION JSON")
    print('-----------------')
    print(post["history"][0])
    print()

    print("SUBJECT")
    print('-----------------')
    print(subject)
    print()

    # Content of post that includes html tags
    #
    # print("CONTENT")
    # print('-----------------')
    # print(question)
    # print()

    print("CONTENT")
    print('-----------------')
    question_text = BeautifulSoup(question, features='lxml').text
    print(question_text)

    answers = post["children"]
    print()

    print("ANSWERS")
    print('-----------------')
    pprint(answers)

if __name__ == "__main__":
    main()