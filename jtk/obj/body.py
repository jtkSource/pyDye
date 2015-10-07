__author__ = 'jubin'


class Body(object):

    same_text = 'No text'

    def __init__(self, text,cnt,toe):
        self.txt = text + str(cnt)
        self.toes = toe
        self.toes = toe
        self.max_cnt = 1
        self.min_cnt = 1

    def print(self):
        print(self.txt)
        print('Toe count : ' + str(self.toes.count))
        print('Max count : ' + str(self.max_cnt))
        print('Min count : ' + str(self.min_cnt))
        print('Min count : ' + Body.same_text)
