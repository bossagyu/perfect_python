# -*- coding: utf-8 -*-
def write(file_name, dict_input):
    f = None
    try:
        f = open(file_name, 'w')
        data = dict_input['data']
        f.write(data)
    except KeyError as e:
        print('エラー種別: {0}'.format(type(e)))
        print(e)
        print ('キーが見つかりませんでした：{0}'.format(str(dict_input)))
    except (FileNotFoundError, TypeError) as e:
        print('エラー種別: {0}'.format(type(e)))
        print(e)
        print ('ファイルが開けませんでした：{0}'.format(file_name))
    else:
        print('問題なく処理ができました')
    finally:
        if f is not None:
            print('ファイルを閉じます')
            f.close()

d = {'meta':'aaaaa', 'data':'bbbbbb'}
write('test.txt',d)

