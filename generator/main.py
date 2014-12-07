'''
Created on Nov 29, 2014

@author: rene
'''
import autopep8
from collections import defaultdict
from docformatter import format_code
import multiprocessing
import Queue
from generator import generate_class, generate_helper, generate_test
from generator import generate_idf, generate_init, generate_group
from iddparser import IDDParser

num_worker_threads = 8
tidy = True

version = "0.1.1"


def worker(q, worker):
    while True:
        try:
            fname, objs, group = q.get(timeout=4)
            create_file(fname, group, objs)
        except Queue.Empty:
            print worker, " Worker finished"
            break


def create_file(fname, group, objs):
    source_files = []
    for obj in objs:
        class_source = generate_class(obj)
        if tidy:
            class_source = autopep8.fix_code(
                class_source, options=autopep8.parse_args(['--aggressive',
                                                          '--aggressive',
                                                          '--aggressive',
                                                          '']))
            class_source = format_code(class_source)
        source_files.append(class_source)

    source = generate_group(group, source_files)

    with open("../pyidf/{}.py".format(fname), 'w') as f:
        f.write(source)

if __name__ == '__main__':
    parser1 = IDDParser()
    objsalt = parser1.parse("V8-2-0-Energy+Alt.idd")
    parser2 = IDDParser()
    objsorg = parser2.parse("V8-2-0-Energy+.idd")

    for a in objsalt:
        objsorg[a] = objsalt[a]

    objs = objsorg.values()
    files = defaultdict(list)
    groups = {}
    for obj in objs:
        groups[obj.file_name] = obj.group
        files[obj.file_name].append(obj)

    q = multiprocessing.Queue()
    for fname in files:
        q.put((fname, files[fname], groups[fname]))
 
    ps = [
        multiprocessing.Process(
            target=worker,
            args=(
                q,
                i)) for i in range(num_worker_threads)]
    for p in ps:
        p.start()
    for p in ps:
        p.join()
 
    source_file = generate_idf(objs)
    if tidy:
        source_file = autopep8.fix_code(
            source_file, options=autopep8.parse_args(['--aggressive',
                                                      '--aggressive',
                                                      '--aggressive',
                                                      '']))
        source_file = format_code(source_file)
 
    with open("../pyidf/idf.py", 'w') as f:
        f.write(source_file)
 
    helper_source = generate_helper(objs)
    if tidy:
        helper_source = autopep8.fix_code(
            helper_source, options=autopep8.parse_args(['--aggressive',
                                                      '--aggressive',
                                                      '--aggressive',
                                                      '']))
        helper_source = format_code(helper_source)
    with open("../pyidf/helper.py", 'w') as f:
        f.write(helper_source)
 
    init_source = generate_init(version)
    if tidy:
        init_source = autopep8.fix_code(
            init_source, options=autopep8.parse_args(['--aggressive',
                                                      '--aggressive',
                                                      '--aggressive',
                                                      '']))
        init_source = format_code(init_source)
    with open("../pyidf/__init__.py", 'w') as f:
        f.write(init_source)

    for obj in objs:
        test_source = generate_test(obj)
        with open("../tests/test_{}.py".format(obj.var_name), 'w') as f:
            f.write(test_source)