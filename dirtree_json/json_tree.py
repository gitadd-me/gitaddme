def path_to_dict(path):
    import os

    d = {'name': os.path.basename(path)}
    
    if os.path.isdir(path):
        d['type'] = "dir"
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir(path) if x[0] != '.']
    else:
        d['type'] = "file"
    return d

def path_to_json(Path):
    import json
    return json.dumps(path_to_dict(Path))

def path_to_txt(path):
    import platform
    platform.system()
    path = path.strip()

    if platform.system() =='Windows' :
        path = str(path.encode(encoding='UTF-8',errors='backslashreplace'))
        path = path.replace('b','',1)
        path = path.replace('\\\\','\\')
        path = path.replace("'",'')

        if path[-1] == "\\" :
            path_write = path+"git_dir.json"
            text_file = open(path_write, 'w', encoding = "utf-8")
        else :
            path_write = path+"\git_dir.json"
            text_file = open(path_write, 'w', encoding = "utf-8")
    else:
        if path[-1] == "/" :
            path_write = path+"git_dir.json"
            text_file = open(path_write, 'w', encoding = "utf-8")
        else :
            path_write = path+"/git_dir.json"
            text_file = open(path_write, 'w', encoding = "utf-8")
    json_string = path_to_json(path)
    text_file.write(json_string)
    text_file.close()