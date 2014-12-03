'''
Created on Nov 29, 2014

@author: rene
'''
import autopep8
from collections import defaultdict
from docformatter import format_code
import multiprocessing
import Queue
from generator import generate_class, generate_helper
from generator import generate_idf
from iddparser import IDDParser
num_worker_threads = 4


def worker(q, worker):
    while True:
        try:
            fname, objs = q.get(timeout=4)
            create_file(fname, objs)
        except Queue.Empty:
            print worker, " Worker finished"
            break


def create_file(fname, objs):
    source_files = [
        "from collections import OrderedDict\nimport logging\nimport re\n\nlogger = logging.getLogger(__name__)\nlogger.addHandler(logging.NullHandler())\n\n"]
    for obj in objs:
        class_source = generate_class(obj)
#         class_source = autopep8.fix_code(
#             class_source, options=autopep8.parse_args(['--aggressive',
#                                                       '--aggressive',
#                                                       '--aggressive',
#                                                       '']))
#         class_source = format_code(class_source)
        source_files.append(class_source)

    source_file = "\n\n".join(source_files)
    with open("../pyidf/{}.py".format(fname), 'w') as f:
        f.write(source_file)

if __name__ == '__main__':
    parser1 = IDDParser()
    objsalt = parser1.parse("V8-2-0-Energy+Alt.idd")
    parser2 = IDDParser()
    objsorg = parser2.parse("V8-2-0-Energy+.idd")

    for a in objsalt:
        objsorg[a] = objsalt[a]

    objs = objsorg.values()
    files = defaultdict(list)
    for obj in objs:
        files[obj.file_name].append(obj)

    q = multiprocessing.Queue()
    for fname in files:
        q.put((fname, files[fname]))

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
    source_file = autopep8.fix_code(
        source_file, options=autopep8.parse_args(['--aggressive',
                                                  '--aggressive',
                                                  '--aggressive',
                                                  '']))
    source_file = format_code(source_file)

    with open("../pyidf/idf.py", 'w') as f:
        f.write(source_file)

    helper_source = generate_helper(objs)
    with open("../pyidf/helper.py", 'w') as f:
        f.write(helper_source)