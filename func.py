# -*- coding: utf-8 -*-
character_dict = "E:/ta_eval/character_dict.txt"
kungfu_dict = "E:/ta_eval/kungfu_dict.txt"

def split_name(character_name,kungfu_name):
    character = open(character_dict).read()
    kungfu = open(kungfu_dict).read()

    with open("name_dic","wb") as outfile:
        outfile.write(kungfu)
        outfile.write(character.replace("、","\n").replace("）","").replace("（","\n")
        .replace("：","\n"))

    print outfile

split_name(character_dict, kungfu_dict)
