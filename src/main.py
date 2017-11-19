import requests
from operator import itemgetter

r = requests.get('https://leetcode.com/api/problems/all/')
json = r.json()
statList = json['stat_status_pairs']
stats = [x['stat'] for x in statList]

problemSet = [(x['question_id'], x['question__title']) for x in stats]
sort = sorted(problemSet)
maxStrLen = max([len(x[-1]) for x in sort])

for p in sort:
    formatStr = "LeetCode {:>3}. {}"
    formatMe = formatStr.format(p[0], p[1])
    print(formatMe)
