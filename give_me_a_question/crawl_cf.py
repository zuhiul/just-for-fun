import urllib.request
import re
import time
import csv
from bs4 import BeautifulSoup

headers = ['question_id', 'rating', 'pass_people_cnt', 'has_pass']


def get_question_page_number():
    submission_url = 'http://codeforces.com/problemset/page/%d' % 1
    print('handle this:%s' % submission_url)

    # load bs
    page = urllib.request.urlopen(submission_url)
    soup = BeautifulSoup(page)
    for buf in soup.find_all(name='div', attrs={"class": 'pagination'}):
        if buf.ul:
            pages = buf.ul.find_all(name='li')
            return int(pages[len(pages) - 2].span.a.get_text())


def get_all_question_and_score(has_pass_list):
    # const define
    question_pages = get_question_page_number()
    print(question_pages)

    # export to csv file
    with open('problem.csv', 'w+') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)

        # get_all_info
        for i in range(1, question_pages + 1):
            # read page
            if i % 10 == 0:
                time.sleep(20)
            question_url = 'http://codeforces.com/problemset/page/%d' % i
            print('handle this:%s' % question_url)
            page = urllib.request.urlopen(question_url)
            soup = BeautifulSoup(page)

            # get question id
            question_id = []
            for link in soup.find_all(name='td', attrs={"class": 'id'}):
                name = link.a.string.strip()
                question_id.append(name)

            # get rating
            rating = []
            for link in soup.find_all(name='td', attrs={"style": 'font-size: 1.1rem'}):
                name = link.span
                if not name:
                    rating.append(-1)
                else:
                    rating.append(name.string.strip())

            # get pass_people_cnt
            pass_people_cnt = []
            for link in soup.find_all(name='td', attrs={"style": 'font-size: 1.1rem;'}):
                if link.a and len(link.a.get_text()) > 2:
                    pass_people_cnt.append(link.a.get_text()[2:])
                else:
                    pass_people_cnt.append(0)

            # check msg len
            if len(question_id) != len(rating) or len(rating) != len(pass_people_cnt):
                print('question_id:', len(question_id), '\t', 'rating:', len(rating), '\t', 'pass_people_cnt:',
                      pass_people_cnt)
                return

            # write to csv file
            for i in range(len(question_id)):
                passed = 0
                if question_id[i] in has_pass_list.keys():
                    passed = 1
                writer.writerow([question_id[i], rating[i], pass_people_cnt[i], passed])
    csv_file.close()


def get_submission_page_number():
    submission_url = 'http://codeforces.com/submissions/%s/page/%d' % ('zuhiul', 1)
    print('handle this:%s' % submission_url)

    # load bs
    page = urllib.request.urlopen(submission_url)
    soup = BeautifulSoup(page)
    for buf in soup.find_all(name='div', attrs={"class": 'pagination'}):
        if buf.ul:
            pages = buf.ul.find_all(name='li')
            return int(pages[len(pages) - 2].span.a.get_text())


def get_all_submission():
    # consts
    handle = 'zuhiul'
    max_page = get_submission_page_number()

    # get submission
    pass_problem_list = {}
    for i in range(1, max_page + 1):
        if i % 5 == 0:
            time.sleep(10)
        submission_url = 'http://codeforces.com/submissions/%s/page/%d' % (handle, i)
        print('handle this:%s' % submission_url)

        # load bs
        page = urllib.request.urlopen(submission_url)
        soup = BeautifulSoup(page)

        # load submission
        for submission in soup.find_all(name='td'):
            if submission.span and submission.span.span and submission.span.span.get_text() == 'Accepted':
                problem_link = submission.previous_sibling.previous_sibling.previous_sibling.previous_sibling.a[
                    'href']
                buf = problem_link.split('/')
                pass_problem_list[buf[2] + buf[4]] = True
    return pass_problem_list


if __name__ == '__main__':
    get_all_question_and_score(get_all_submission())
