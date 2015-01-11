def write(file_name, dict_input):
    f = None
    try:
        f = open(file_name, 'w')
        data = dict_input['data']
        f.write(data)
    except KeyError as e:
        print('





