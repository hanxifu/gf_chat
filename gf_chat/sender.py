import datetime
import random
import time

import itchat


class GirlfriendWechatBot:
    """
    A wechat sender class.
    """

    def __init__(self,
                 gf_remark_name,
                 love_words_at_day,
                 love_words_at_night,
                 wake_up_hour: int = 7,
                 fall_asleep_hour: int = 23,
                 sender_cd: int = 3600):
        """
        Config the wechat sender.

        Args:
            gf_remark_name: Your girlfriend's wechat remark name.
            love_words_at_day: File includes love words sent randomly at day,
                one sentence per line.
            love_words_at_night: File includes Love words send randomly at
                night, one sentence per line.
            wake_up_hour: Set the hour you start send love words.
            fall_asleep_hour: Set the hour to start use love_words_at_night.
            sender_cd: Wait seconds between your love word messages.

        """
        itchat.auto_login(hotReload=True)
        self.gf = itchat.search_friends(remarkName=gf_remark_name)
        if len(self.gf) > 1:
            raise Exception('More than one girlfriend was found by remark name.'
                            'What\'s your problem?')
        elif len(self.gf) < 1:
            raise Exception('No girlfriend was found. Do you have a girlfriend?'
                            'Or have you set correct remark name?')
        else:
            self.gf = self.gf[0]
        self.day_words = open(love_words_at_day).readlines()
        self.night_words = open(love_words_at_night).readlines()
        self.wake_up_hour = wake_up_hour
        self.fall_asleep_hour = fall_asleep_hour
        self.sender_cd = sender_cd

    def __str__(self):
        return f'Love you :) {self.gf["userName"]}'

    def chat_bot(self):
        curr_hour = datetime.datetime.now().hour
        while True:
            if curr_hour > self.wake_up_hour:
                if curr_hour < self.fall_asleep_hour:
                    msg = self.day_words[random.randint(0, len(self.day_words) - 1)]
                else:
                    msg = self.night_words[random.randint(0, len(self.night_words) - 1)]

                itchat.send_msg(msg, self.gf['UserName'])
                time.sleep(self.sender_cd + random.randint(-100, 100))
