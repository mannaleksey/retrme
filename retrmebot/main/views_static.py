import time
import requests
import json
from .models import DataCase
from rytrme_api_python import get_text_from_rytr_me_api

API_KEY = 'UE6OU0PK3STQZFEL0U_XM'


def create_object_db(person, response):
    c = 0
    while True:
        c += 1
        if c == 100:
            break
        try:
            DataCase.objects.create(person=person, response=response)
            break
        except:
            time.sleep(0.1)


def get_object_from_db(person):
    c = 0
    while True:
        c += 1
        if c == 100:
            return False
        try:
            data = DataCase.objects.get(person=person)
            return data
        except:
            time.sleep(0.1)


def delete_from_db(data):
    c = 0
    while True:
        c += 1
        if c == 100:
            break
        try:
            data.delete()
            break
        except:
            time.sleep(0.1)


def request_to_retrme(topic, mood, person):
    input_contexts = {"SECTION_TOPIC_LABEL": f"{topic}"}
    response = get_text_from_rytr_me_api(api_key=API_KEY, input_contexts=input_contexts, tone=mood)
    create_object_db(person, response[0]['text'])


def request_to_retrme2():
    # try:
        def useCaseDetail(useCaseId):
            try:
                headers = {'Authentication': 'Bearer ' + API_KEY}
                r = requests.get(API_URL + '/use-cases/' + useCaseId, headers=headers)
                data = r.json()
                return data['data']
            except:
                print('An exception occurred')
            return None

        def ryte(languageId, toneId, useCaseId, inputContexts):
            try:
                data = {
                    'languageId': languageId,
                    'toneId': toneId,
                    'useCaseId': useCaseId,
                    'inputContexts': inputContexts,
                    'variations': 1,
                    'userId': 'USER1',
                    'format': 'html'
                }
                headers = {'Authentication': 'Bearer ' + API_KEY}
                r = requests.post(API_URL + '/ryte', json=data, headers=headers)
                data = r.json()
                return data
            except:
                print('An exception occurred')
            return None

        languageIdEnglish = '607adc2f6f8fe5000c1e637a'
        toneIdConvincing = '60572a639bdd4272b8fe358b'
        useCaseIdJobDescription = '60586b31cdebbb000c21058d'
        # useCaseJobDescription = useCaseDetail(useCaseIdJobDescription)
        key = 'JOB_ROLE_LABEL'
        inputContexts = {key: 'Product Manager'}
        outputs = ryte(
            languageIdEnglish,
            toneIdConvincing,
            useCaseIdJobDescription,
            inputContexts
        )
        if outputs['success']:
            create_object_db('1', outputs['data'][0]['text'])
    # except:
    #     pass