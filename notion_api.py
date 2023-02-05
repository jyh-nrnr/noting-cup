import json, time, os
import requests
from notion_client import Client
from io import BytesIO
from PIL import Image
import cv2 
import numpy as np



def getImages(Token, DB_id):
    url = f'https://api.notion.com/v1/databases/{DB_id}/query'

    r = requests.post(
        url, 
        headers={
        "Authorization": f"Bearer {Token}",
        "Notion-Version": "2021-08-16"
        }
    )
    result_dict = r.json()
    imgs_list_result = result_dict['results']
    return imgs_list_result

def return_random_img_from_table(table):
    img = table['properties']['Files & media']['files'][0]
    url = img['file']['url']
    filename = img['name']

    res = requests.get(url)
    img = np.array(Image.open(BytesIO(res.content)))
    img=cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    return img


