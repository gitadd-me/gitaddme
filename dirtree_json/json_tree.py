def path_to_dict(path):
    import os

    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "dir"
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir(path)]
    else:
        d['type'] = "file"
    return d

def path_to_json(Path):
    import json
    return json.dumps(path_to_dict(Path))

def path_to_txt(path):
    path = path.replace("\\","/")
    if path[-1] == "/" :
        text_file = open(path+'git_dir.json', 'w', encoding = "utf-8")
        print(path+'Example.txt')
    else:
        text_file = open(path+'/git_dir.json', 'w', encoding = "utf-8")
    json_string = path_to_json(path)
    text_file.write(json_string)
    text_file.close()