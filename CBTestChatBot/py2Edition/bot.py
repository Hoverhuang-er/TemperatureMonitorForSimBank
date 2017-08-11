#!/usr/bin/env python
# coding: utf-8


import myredispool
import recomend
from wxbot import *


class TulingWXBot(WXBot):
    def __init__(self):
        WXBot.__init__(self)

        self.tuling_key = ""
        self.robot_switch = True
        self.redis = myredispool.RedisCache()
        self.master_id = ''
        self.master_mode = 0

        try:
            cf = ConfigParser.ConfigParser()
            cf.read('conf.ini')
            self.tuling_key = cf.get('main', 'key')
        except Exception:
            pass
        print ('tuling_key:', self.tuling_key)

    def tuling_auto_reply(self, uid, msg):
        if self.tuling_key:
            url = "1853bbe33adc4da2912fb9875541d19f"
            user_id = uid.replace('@', '')[:30]
            body = {'key': self.tuling_key, 'info': msg.encode('utf8'), 'userid': user_id}
            r = requests.post(url, data=body)
            respond = json.loads(r.text)
            result = ''
            if respond['code'] == 100000:
                result = respond['text'].replace('<br>', '  ')
            elif respond['code'] == 200000:
                result = respond['url']
            elif respond['code'] == 302000:
                for k in respond['list']:
                    result = result + u"【" + k['source'] + u"】 " +\
                        k['article'] + "\t" + k['detailurl'] + "\n"
            else:
                result = respond['text'].replace('<br>', '  ')

            print ('    ROBOT:', result)
            return result
        else:
            return u"知道啦"

    def auto_switch(self, msg):
        msg_data = msg['content']['data']
        stop_cmd = [u'退下', u'走开', u'关闭', u'关掉', u'休息', u'滚开']
        start_cmd = [u'出来', u'启动', u'工作']
        if self.robot_switch:
            for i in stop_cmd:
                if i == msg_data:
                    self.robot_switch = False
                    self.send_msg_by_uid(u'[Robot]' + u'小C机器人已关闭！', msg['to_user_id'])
        else:
            for i in start_cmd:
                if i == msg_data:
                    self.robot_switch = True
                    self.send_msg_by_uid(u'[Robot]' + u'小C机器人已开启！', msg['to_user_id'])

    def recommend(self, userid, msg_data):
        movie_cmd = [u'租用路由', u'ROUTER', u'router', u'机场wifi', u'旅行wifi', u'路由器', u'去旅行', u'wifirouter']
        smallmovie_cmd = [u'我要wifi', u'日本', u'JR']
        for i in movie_cmd:
            if i == msg_data:
                try:
                    reply = recomend.recommend_movie()
                    self.send_msg_by_uid(reply, userid)
                except:
                    self.send_msg_by_uid(u'请点开：https://www.changirecommends.com/', userid)
                return True
        for i in smallmovie_cmd:
            if i == msg_data:
                try:
                    reply = recomend.recommend_smallmovie()
                    self.send_msg_by_uid(reply, userid)
                except:
                    self.send_msg_by_uid(u'小C累了。休息一下', userid)
                return True
        return False

    def handle_msg_all(self, msg):

        if not self.robot_switch and msg['msg_type_id'] != 1:
            return
        if msg['msg_type_id'] == 1 and msg['content']['type'] == 0:  # reply to self
            self.auto_switch(msg)
        elif msg['msg_type_id'] == 4 and (msg['content']['type'] == 0 or msg['content']['type'] == 6):  # text message from contact
            print (msg['user']['id'])
            if msg['content']['data'] == 'open the console':
                self.master_id = msg['user']['id']
                self.master_mode = 1
                self.send_msg_by_uid(u"admin", msg['user']['id'])
                return
            if msg['content']['data'] == 'close the console':
                self.master_id = ''
                self.master_mode = 0
                self.send_msg_by_uid(u"adminclose", msg['user']['id'])
                return
            if msg['user']['id'] == self.master_id and msg['content']['data'] != 'open the console':
                for group in self.group_members:
                    print (group)
                    self.send_msg_by_uid(msg['content']['data'], group)
                self.send_msg_by_uid(u"公告发送成功", msg['user']['id'])
                return
            if self.master_mode == 1:
                return

            if msg['content']['type'] == 6:
                self.send_random_emoji(msg['user']['id'])
                return

            # 处理推荐系统逻辑
            if self.recommend(msg['user']['id'], msg['content']['data']):
                return
            # 处理聊天逻辑
            self.send_msg_by_uid(self.tuling_auto_reply(msg['user']['id'], msg['content']['data']), msg['user']['id'])

        elif msg['msg_type_id'] == 3 and (msg['content']['type'] == 0 or msg['content']['type'] == 10
                                          or msg['content']['type'] ==3 or msg['content']['type']  == 6
                                          or msg['content']['type'] == 4 or msg['content']['type'] == 12):  # group text message
            if self.master_mode == 1:
                if msg['content']['data'] == 'test':
                    print ('send picture!')
                    #self.send_image('data/image/img_476620686838734673.jpg', msg['user']['id'])
                    #self.send_file('data/voice/voice_6364321762328836396.mp3', msg['user']['id'])
                return

            # 处理撤回逻辑
            print ('group message')
            if msg['content']['redraw'] == 1:
                msg_data = msg['content']['data']
                print (msg_data)
                old_msgid = re.compile('<msgid>(.*)</msgid>').findall(msg_data)[0]
                print ('old_msgid is ' + old_msgid)
                redraw_msg = self.redis.get_data(old_msgid)
                print (type(redraw_msg))

                print ('redraw_msg is ' + str(redraw_msg).replace("\\\\", "\\"))
                #redraw_json = json.loads(str(redraw_msg).replace("\\\\", "\\").replace("\'", "\""))
                #print type(redraw_json)
                #print redraw_json['data']
                username =  re.compile(': (.*), \'userid\'').findall(redraw_msg)[0]
                print (username)
                redraw_type = re.compile('\'type\': (.*)}').findall(redraw_msg)[0]
                print (redraw_type)
                data = re.compile('\'data\': (.*), \'type\'').findall(redraw_msg)[0]
                if int(redraw_type) == 3:
                    print (data.replace('u', '').replace('\'', ''))
                    self.send_image(data.replace('u', '').replace('\'', ''), msg['user']['id'])
                    reply = u'刚才'+username.decode("unicode_escape").replace("\'","").replace("u","")+u'撤回得是'+\
                        u'这张图片'
                    self.send_msg_by_uid(reply, msg['user']['id'])
                elif int(redraw_type) == 4:
                    self.send_file(data.replace('u', '').replace('\'', ''), msg['user']['id'])
                    reply = u'刚才'+username.decode("unicode_escape").replace("\'","").replace("u","")+u'撤回得是'+\
                        u'这段语音'
                    self.send_msg_by_uid(reply, msg['user']['id'])
                else:
                    reply = u'刚才'+username.decode("unicode_escape").replace("\'","").replace("u","")+u'撤回得是：'+\
                        data.decode("unicode_escape").replace("\'","").replace("u","")
                    self.send_msg_by_uid(reply, msg['user']['id'])

            # save message to redis
            msg_id = msg['msg_id']
            print (msg_id)
            redis_data = ''
            if msg['content']['type'] == 0:
                redis_data = msg['content']['desc']
            elif msg['content']['type'] == 3:
                redis_data = msg['content']['image_url']
            elif msg['content']['type'] == 4:
                redis_data = msg['content']['voice_url']
            else:
                redis_data = u'一种未知事物'
            message = {'data': redis_data, 'userid': msg['user']['id'], 'username': msg['user']['name'], 'type': msg['content']['type']}
            success = self.redis.set_data(msg_id, message)
            if success:
                print (msg_id, message)
                print (u"消息存入redis成功")

            # Process emoji
            if msg['content']['type'] == 6:
                self.send_random_emoji(msg['user']['id'])
                return


            #if msg['content']['is_entergroup'] == 1:
            #    reply = u'hello I m auto process robot for YYM CTS support。'
            #    reply += u'my function is ：1.Pls @me I will talk to you； 2.Machine will random for anyone(like heart reat pack； 3.You can ask me anyinformation.,But i dont wanna reply to you；' \
            #             u'4.It nope support emoji；5.Reply all request；6.Pls do not send red pack'
            #    self.send_msg_by_uid(reply, msg['user']['id'])
            #    return


            # 处理红包
            if msg['content']['is_hongbao'] == 1:
                reply = u'!!! '
                for member_name in self.get_all_group_member_name(msg['user']['id']):
                    reply+='@'+member_name+' '
                self.send_msg_by_uid(reply, msg['user']['id'])
                return

            if 'test' in msg['content']['desc']:
                #self.send_msg_by_uid('<span class=\"emoji emoji1f61e\">', msg['user']['id'])
                self.send_msg_by_uid(u'\ue159', msg['user']['id'])
                self.send_msg_by_uid(u'\u263A', msg['user']['id'])
                self.send_msg_by_uid(u'\uf601', msg['user']['id'])
                self.send_msg_by_uid(u'\ue412', msg['user']['id'])
                self.send_msg_by_uid(u'\u1f639', msg['user']['id'])
                self.send_msg_by_uid(u'\u1f612', msg['user']['id'])
                self.send_msg_by_uid(u'\u1233', msg['user']['id'])
                self.send_msg_by_uid(u'\ue402', msg['user']['id'])
                self.send_msg_by_uid(u'\1f60f', msg['user']['id'])
                self.send_msg_by_uid(u'\u1f60f', msg['user']['id'])
                self.send_msg_by_uid(u'\u160f', msg['user']['id'])


            #    return
            #
            #if u'@' in msg['content']['desc'] and u'全员' in msg['content']['desc']:
            #    reply = ''
            #    reply1 = ''
            #    reply2 = ''
            #    reply3 = ''
            #    reply4 = ''
            #    reply5 = ''
            #    a = ('2005',)
            #   print '@'+"member"+('\\u%s'%a).decode('unicode-escape')
            #    for member_name in self.get_all_group_member_name(msg['user']['id']):
            #        reply+=u'@'+member_name+u'\u2005'+' '
            #        reply1+='@'+u'\u2005'+member_name+ ' '
            #        reply2+='@'+member_name+('\\u%s'%a).decode('unicode-escape')
            #        reply3+='@'+member_name+('\u2005').decode('unicode-escape')
            #        reply4+='@'+('\u2005').decode('unicode-escape')+member_name
             #       reply5+= '@'+('\\u2005').decode('unicode-escape')+member_name

            #    self.send_msg_by_uid(reply,msg['user']['id'])
                #self.send_msg_by_uid(reply1,msg['user']['id'])
                #self.send_msg_by_uid(reply2,msg['user']['id'])
                #self.send_msg_by_uid(reply3,msg['user']['id'])
                #self.send_msg_by_uid(reply4,msg['user']['id'])
                #self.send_msg_by_uid(reply5,msg['user']['id'])
            #   return


            # Process text message
            if 'detail' in msg['content']:
                #my_names = self.get_group_member_name(self.my_account['UserName'], msg['user']['id'])
                my_names = self.get_group_member_name(msg['user']['id'], msg['to_user_id'])
                if my_names is None:
                    my_names = {}
                if 'NickName' in self.my_account and self.my_account['NickName']:
                    my_names['nickname2'] = self.my_account['NickName']
                if 'RemarkName' in self.my_account and self.my_account['RemarkName']:
                    my_names['remark_name2'] = self.my_account['RemarkName']



                is_at_me = False
                random_value = random.randint(1, 100)

                for detail in msg['content']['detail']:
                    if detail['type'] == 'at':
                        for k in my_names:
                            if my_names[k] and my_names[k] == detail['value']:
                                is_at_me = True
                                break

                #Process when need use robot


                ############################


                # 处理推荐系统逻辑
                if self.recommend(msg['user']['id'], msg['content']['desc']):
                    return

                if is_at_me:
                    src_name = msg['user']['name']
                    reply = '@' + src_name + ': '
                    if msg['content']['type'] == 0:  # text message
                        reply += self.tuling_auto_reply(msg['content']['user']['id'], msg['content']['desc'])
                        if random_value > 70:
                            reply += '!'
                    else:
                        reply += u"please send me format like device number and error code，,,Ծ‸Ծ,,"
                    self.send_msg_by_uid(reply, msg['user']['id'])

                print (random_value)

                index = random.randint(0, 5)
                random_say = [u'23333333', u'yo',u'lah',u'Ohmm',u'yah', u'can']

                if is_at_me is False and (random_value == 95 or random_value == 96):
                    self.send_random_emoji(msg['user']['id'])
                if is_at_me is False and random_value ==99:
                    src_name = msg['user']['name']
                    reply = ''
                    if msg['content']['type'] == 0:  # text message
                        reply += self.tuling_auto_reply(msg['content']['user']['id'], msg['content']['desc'])
                        if random_value > 98:
                            reply += '!'
                    else:
                        reply += u"I wanna know what r you talk about"
                    time.sleep(3)
                    print (u"Emm:"+reply)
                    self.send_msg_by_uid(reply, msg['user']['id'])

                if is_at_me is False and random_value ==98:
                    src_name = msg['user']['name']
                    reply = ''
                    if msg['content']['type'] == 0:  # text message
                        reply += random_say[index]
                        if random_value > 93:
                            reply += '!'
                    else:
                        reply += u"我很想知道你说的什么"
                    time.sleep(3)
                    print (u"主动发言:"+reply)
                    self.send_msg_by_uid(reply, msg['user']['id'])


def main():
    bot = TulingWXBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'tty'

    bot.run()


if __name__ == '__main__':
    main()

