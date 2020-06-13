from piazza_api import Piazza
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys
import os

def main():
    p = Piazza()
    p.user_login(email=os.environ['EMAIL'], password=os.environ['PASSWORD'])

    piazza_url = urlparse(sys.argv[1])

    class_id = piazza_url.path.split('/')[2]
    post_num = piazza_url.query.split('=')[1]
    
    cse103 = p.network(class_id)

    post = cse103.get_post(post_num)

    question = post["history"][0]["content"]

    print("QUESTION")
    print(post["history"][0])

    
    question_text = BeautifulSoup(question, features='lxml')

    answers = post["children"]

    print("ANSWERS")
    print(answers)

if __name__ == "__main__":
    main()