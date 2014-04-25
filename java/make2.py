#encoding:utf-8
#to do:
#support Chinese File name yet...  [ok]
#support paging yet[ok]
#support sort the diaries by time [ok]
__author__ = 'Jayin Ton'

import os
import re
import json
import copy
import time

"""
  项目文件目录结构换了，这是最新的生成脚本
"""
#config
limit = 10
ignore = [
    'README.md',
    '.+\.json',
    '.+\.py',
    '.+\.db'
]


def generation(page, l, cwd):
    file_name = cwd + os.path.sep + str(page) + ".json"
    with open(file_name, mode="w") as f:
        if len(l) > 0:
            f.write(json.dumps({
                'result': ','.join(l).decode('gbk').split(',')
            }))
        else:
            f.write(json.dumps({'result': []}))


def cleanup(cwd):
    """
    clean up the `json` files
    """
    l = list(os.listdir(cwd))
    pattern = re.compile(r'.+\.json', re.IGNORECASE)
    for x in l:
        #
        if re.findall(pattern, x):
            os.remove(cwd + os.path.sep + x)
            print 'remove file--', cwd + os.path.sep + x
    print 'clean up .json files finished'


def main_work(cwd):
    """
     cwd : the current working directory.
    """
    cleanup(cwd)
    l = list(os.listdir(cwd))
    raw = copy.deepcopy(l)
    for ig in ignore:
        pattern = re.compile(ig, re.IGNORECASE)
        for t in l:
            if re.findall(pattern, t):
                raw.remove(t)
    raw.sort(reverse=False)
    size = len(raw)
    # print size
    page = 1
    while page * limit <= size:
        # print page, '--> ', raw[(page - 1) * limit:page * limit]
        generation(page, raw[(page - 1) * limit:page * limit], cwd)
        page += 1
    # print page, '--> ', raw[(page - 1) * limit:]
    generation(page, raw[(page - 1) * limit:], cwd)

    with open(cwd + os.path.sep + 'info.json', mode='w') as f:
        f.write(json.dumps({'pages': page, 'last_motify': long(time.time() * 1000)}))
    print 'total=', size, 'pages=', page
    print "Build finished."
    print ""


def main(cwd):
    cwd_list = list(os.listdir(cwd))
    print 'deal with dir: ', cwd
    for file_name in cwd_list:
        if os.path.isdir(os.path.join(cwd, file_name)):
            print os.path.join(cwd, file_name)
            main_work(os.path.join(cwd, file_name))

    print 'finish: ', cwd


def t(d):
    print d


if __name__ == "__main__":
    # main()
    #[os.path.isdir(p) for p in os.listdir(os.getcwd())]
    for f in filter(lambda _dir: os.path.isdir(_dir), os.listdir(os.getcwd())):
        main(os.path.join(os.getcwd(), f))