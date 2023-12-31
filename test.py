import sys


if sys.argv[:1]:
    filename = sys.argv[1]
    filename = filename.split('.') 
    ext = filename.pop()
    fn = filename.pop()
    print(ext, fn)
else:
    print('usage:')
    