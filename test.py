import sys, os
from piazza_api import Piazza
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from pprint import pprint

def piazza_parse(pi_url):
    '''
    Called by connect.py to get post from Piazza.
    It will format the post json into a more readable message for server.
    '''

    # Create Piazza object, login, and get the users classes
    temp = ""
    p = Piazza()
    p.user_login(email=os.environ['EMAIL'], password=os.environ['PASSWORD'])
    classes = p.get_user_classes()

    # Parse the piazza url into components
    piazza_url = urlparse(pi_url)

    # Get class id and the post number from piazza_url
    class_id = piazza_url.path.split('/')[2]
    post_num = piazza_url.query.split('=')[1]
    
    # Returns a class network
    class_net = p.network(class_id)

    # Get the piazza post from the post number and class network
    post = class_net.get_post(post_num)

    # Get class name
    class_name = "None"
    for i in classes:
        if i['nid'] == class_id:
            class_name = i['num']

    # Get question and subject of the post
    question = post["history"][0]["content"]
    subject = post["history"][0]["subject"]

    # Format class name, subject, and post content for Discord
    temp += "__**CLASS NAME**__\n"
    temp += class_name + '\n\n'
    temp += "__**SUBJECT**__\n"
    temp += subject + '\n\n'
    temp += "__**CONTENT**__\n"
    question_text = BeautifulSoup(question, features='lxml').text
    temp += question_text + '\n\n'

    # Get answers json
    answers = post["children"]
    
    # Init student and instructor json answers
    s_answer_json = None
    i_answer_json = None

    # Assign student and instructor answers if they exist
    for answer in answers:
        if answer['type'] == 's_answer':
            s_answer_json = answer
        elif answer['type'] == 'i_answer':
            i_answer_json = answer

    # Format student and/or instructor answer if they exist
    if s_answer_json is not None:
        temp += "__**STUDENT ANSWER**__\n"
        s_answer = s_answer_json['history'][0]['content']
        s_answer_text = BeautifulSoup(s_answer, features='lxml').text
        temp += s_answer_text + '\n\n'

    if i_answer_json is not None:
        temp += "__**INSTRUCTOR ANSWER**__\n"
        i_answer = i_answer_json['history'][0]['content']
        i_answer_text = BeautifulSoup(i_answer, features='lxml').text
        temp += i_answer_text

    return temp
