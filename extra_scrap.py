#!/usr/bin/python3

import pandas as pd
import requests

videos = pd.read_csv('./data/USvideos.csv')
ids = videos['video_id']
# print('[')
# response = requests.get('https://www.googleapis.com/youtube/v3/videos?id=9bZkp7q19f0,kjyeCdd-dl8&part=contentDetails&key=AIzaSyD7aumbqlL9DbCOsh42wPLtZnDFIQzKTkc')
# print(response.text, ',')
# print(']')