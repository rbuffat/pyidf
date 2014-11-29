'''
Created on Nov 29, 2014

@author: rene
'''
import autopep8
from collections import defaultdict
from docformatter import format_code
from generator import generate_class
from iddparser import IDDParser


if __name__ == '__main__':
    parser = IDDParser()
    objs = parser.parse("V8-2-0-Energy+.idd")

    files = defaultdict(list)
    for obj in objs:
        files[obj.file_name].append(obj)

    for fname in files:
        source_files = ["from collections import OrderedDict"]
        for obj in files[fname]:
            source_files.append(generate_class(obj))

        source_file = "\n\n".join(source_files)
#         source_file = autopep8.fix_code(
#                     source_file, options=autopep8.parse_args(['--aggressive',
#                                                   '--aggressive',
#                                                   '--aggressive',
#                                                   '']))
#         source_file = format_code(source_file)
        with open("../pyidf/{}.py".format(fname), 'w') as f:
            f.write(source_file)
