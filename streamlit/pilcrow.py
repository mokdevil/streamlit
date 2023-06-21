def remove_pilcrow(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    #¶
    content = content.replace('�', '')
    
    with open(file_path, 'w') as f:
        f.write(content)
        

file_path = "Bible_King_James_Version.txt"
remove_pilcrow(file_path)