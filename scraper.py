import requests
import json
import pandas as pd
from selectolax.parser import HTMLParser
import datetime
from bs4 import BeautifulSoup
from constants import HEADERS
from utils import save_to_csv


def make_request(url, headers, params):
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def get_question_details(question_id):
    question_url = f'https://www.zhihu.com/question/{question_id}'
    response = requests.get(question_url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')
    script_tag = soup.find('script', {'id': 'js-initialData'})
    data = json.loads(script_tag.string)
    data_source = data['initialState']['entities']['questions'][f'{question_id}']
    return {
        "question_created_time": datetime.datetime.fromtimestamp(data_source['created']),
        "question_updated_time": datetime.datetime.fromtimestamp(data_source['updatedTime']),
        "question_title": data_source['title'],
        "question_comment_count": data_source['commentCount'],
        "question_voteup_count": data_source['voteupCount'],
        "question_follower_count": data_source['followerCount'],
        "question_viewed_count": data_source['visitCount']
    }

def fetch_answers_for_question(question_id, start_offset=0):
    api_url = f"https://api.zhihu.com/questions/{question_id}/answers"
    params = {
        "include": "data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,question,excerpt,is_labeled,paid_info,paid_info_content,relationship.is_authorized,voting,is_author,is_thanked,is_nothelp,is_recognized,mark_infos[*].url;data[*].author.follower_count,vip_info,badge[*].topics;data[*].settings.table_of_content.enabled",
        "limit": 20, # the largetest request can be sent before been blocked by Zhihu
        "offset": start_offset
    }
    data = make_request(api_url, HEADERS, params)
    if not data or "data" not in data:
        return []

    answers_data = []
    for answer in data["data"]:
        answer_content = HTMLParser(answer['content']).text()
        answer_info = {
            "answer_author": answer["author"]["name"],
            "answer_follower_count": answer["author"]["follower_count"],
            "answer_content": answer_content,
            "answer_created_time": datetime.datetime.fromtimestamp(answer['created_time']),
            "answer_updated_time": datetime.datetime.fromtimestamp(answer['updated_time']),
            "answer_comment_count": answer["comment_count"],
            "answer_voteup_count": answer["voteup_count"],
            "answer_url": answer["url"]
        }
        answers_data.append(answer_info)

    return answers_data

def split_data(question_ids):
    all_data = []
    for qid in question_ids:
        question_data = get_question_details(qid)
        offset = 0
        while True:
            answers_data = fetch_answers_for_question(qid, offset)
            if not answers_data:
                break
            for answer in answers_data:
                merged_data = {**question_data, **answer}
                all_data.append(merged_data)
            offset += 20

    df_result = pd.DataFrame(all_data)
    save_to_csv(df_result)
