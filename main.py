import keyboard
import win32clipboard
import win32con
import win32api
import time
import datetime
def trans(n):
    a = str(datetime.timedelta(seconds=n))
    b = a[-2:]
    c = a[2:4]
    corrent_time = c + 'min' + b + 's'
    return corrent_time
def clipboard_set(data):
    """设置剪贴板数据"""
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, data)
    win32clipboard.CloseClipboard()
def top_0():
    global start_time
    now_time = int(time.time()) - start_time
    next_time = now_time+cd[0]
    correct_time = trans(next_time)
    payload = '对面'+hero[0]+'的'+skill[0]+'将在'+correct_time+'时结束冷却'
    clipboard_set(payload)
    # print(payload)
def top_1():
    global start_time
    now_time = int(time.time()) - start_time
    next_time = now_time+cd[0]
    correct_time = trans(next_time)
    payload = '对面'+hero[0]+'的'+skill[4]+'将在'+correct_time+'时结束冷却'
    clipboard_set(payload)

def top_2():
    global start_time
    now_time = int(time.time()) - start_time
    next_time = now_time+cd[0]
    correct_time = trans(next_time)
    payload = '对面'+hero[0]+'的'+skill[1]+'将在'+correct_time+'时结束冷却'
    clipboard_set(payload)
def mid_0():
    global start_time
    now_time = int(time.time()) - start_time
    next_time = now_time+cd[0]
    correct_time = trans(next_time)
    payload = '对面'+hero[1]+'的'+skill[0]+'将在'+correct_time+'时结束冷却'
    clipboard_set(payload)
def mid_1():
    global start_time
    now_time = int(time.time()) - start_time
    next_time = now_time+cd[0]
    correct_time = trans(next_time)
    payload = '对面'+hero[1]+'的'+skill[4]+'将在'+correct_time+'时结束冷却'
    clipboard_set(payload)
def mid_2():
    global start_time
    now_time = int(time.time()) - start_time
    next_time = now_time+cd[0]
    correct_time = trans(next_time)
    payload = '对面'+hero[1]+'的'+skill[1]+'将在'+correct_time+'时结束冷却'
    clipboard_set(payload)
def bot_0():
    global start_time
    now_time = int(time.time()) - start_time
    next_time = now_time+cd[0]
    correct_time = trans(next_time)
    payload = '对面'+hero[2]+'的'+skill[0]+'将在'+correct_time+'时结束冷却'
    clipboard_set(payload)
def bot_1():
    global start_time
    now_time = int(time.time()) - start_time
    next_time = now_time+cd[0]
    correct_time = trans(next_time)
    payload = '对面'+hero[2]+'的'+skill[2]+'将在'+correct_time+'时结束冷却'
    clipboard_set(payload)
def bot_2():
    global start_time
    now_time = int(time.time()) - start_time
    next_time = now_time+cd[0]
    correct_time = trans(next_time)
    payload = '对面'+hero[2]+'的'+skill[3]+'将在'+correct_time+'时结束冷却'
    clipboard_set(payload)
def ye_0():
    global start_time
    now_time = int(time.time()) - start_time
    next_time = now_time+cd[0]
    correct_time = trans(next_time)
    payload = '对面'+hero[3]+'的'+skill[0]+'将在'+correct_time+'时结束冷却'
    clipboard_set(payload)
def fu_0():
    global start_time
    now_time = int(time.time()) - start_time
    next_time = now_time+cd[0]
    correct_time = trans(next_time)
    payload = '对面'+hero[4]+'的'+skill[0]+'将在'+correct_time+'时结束冷却'
    clipboard_set(payload)
def fu_1():
    global start_time
    now_time = int(time.time()) - start_time
    next_time = now_time+cd[0]
    correct_time = trans(next_time)
    payload = '对面'+hero[4]+'的'+skill[1]+'将在'+correct_time+'时结束冷却'
    clipboard_set(payload)
def fu_2():
    global start_time
    now_time = int(time.time()) - start_time
    next_time = now_time+cd[0]
    correct_time = trans(next_time)
    payload = '对面'+hero[4]+'的'+skill[2]+'将在'+correct_time+'时结束冷却'
    clipboard_set(payload)
def gg():
    global start_time
    start_time = int(time.time())
    print('gg')
def get_key():
    keyboard.wait()


keyboard.add_hotkey('8+0',top_0)
keyboard.add_hotkey('8+1',top_1)
keyboard.add_hotkey('8+3',top_2)
keyboard.add_hotkey('5+0',mid_0)
keyboard.add_hotkey('5+1',mid_1)
keyboard.add_hotkey('5+3',mid_2)
keyboard.add_hotkey('2+0',bot_0)
keyboard.add_hotkey('2+7',bot_1)
keyboard.add_hotkey('2+9',bot_2)
keyboard.add_hotkey('4+0',ye_0)
keyboard.add_hotkey('6+0',fu_0)
keyboard.add_hotkey('6+3',fu_1)
keyboard.add_hotkey('6+7',fu_2)
keyboard.add_hotkey('+',gg)
global start_time
start_time = int(time.time())
hero = ['上单','中单','AD','打野','辅助']
skill = ['闪现','引燃','治疗','净化','传送']
cd = [300,240,210,360]
get_key()
#0:闪现 1:传送 3:引燃 7:治疗 9:净化
