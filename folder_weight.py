import os
import os.path


def get_weight(a):
    s = 0
    # распечатать все файлы и папки рекурсивно
    for dirpath, dirnames, filenames in os.walk(a):
        # перебрать каталоги
        # for dirname in dirnames:
            # s1 = rec(os.path.join(dirpath, dirname))
            # s += s1
            # print(os.path.join(dirpath, dirname))
        # перебрать файлы
        for filename in filenames:
            try:
                s2 = os.path.getsize(os.path.join(dirpath, filename))
                s += s2
            except:
                # print('-err:', filename)
                pass
            # print(os.path.join(dirpath, filename), ': ', s2)
    return s


def get_name(a):
    return a['name']


def convert_from_bytes(b, is_full=False):
    if b >= 1024:
        kb_ = b // 1024
        byte_ = b % 1024
        byte_str = '' if byte_ == 0 else str(byte_) + ' байт'
        kb_str = ''
        mb_str = ''
        gb_str = ''
        if kb_ >= 1024:
            mb_ = kb_ // 1024
            kb_ = kb_ % 1024

            if mb_ >= 1024:
                gb_ = mb_ // 1024
                mb_ = mb_ % 1024
                gb_str = str(gb_) + 'Гб, '
            mb_str = '' if mb_ == 0 else str(mb_) + ' Мб, '
        kb_str = '' if kb_ == 0 else str(kb_) + ' Кб, '

        if not is_full:
            if gb_str != '':
                return gb_str + mb_str.replace(',', '')
            elif mb_str != '':
                return mb_str.replace(',', '')
            elif kb_str != '':
                return kb_str.replace(',', '')
            return byte_str
        else:
            return gb_str + mb_str + kb_str + byte_str
    else:
        return str(b) + ' байт'


def show(d):
    print('\n' + d + ':')

    res_dir = []
    res_file = []
    t = os.listdir(d)
    sum_w = 0
    max_len = 0
    for i in t:
        current_dir = os.path.join(d, i)
        if os.path.isdir(current_dir):
            s1 = get_weight(current_dir)
            sum_w += s1
            max_len = max(max_len, len(i))
            res_dir.append({'name': i, 'weight': s1})
        else:
            s2 = os.path.getsize(current_dir)
            sum_w += s2
            max_len = max(max_len, len(i))
            res_file.append({'name': i, 'weight': s2})

    res_dir.sort(key=get_name)
    res_file.sort(key=get_name)
    for r in res_dir:
        if r['weight'] > 1024 * 1024 * 512:
            print(r['name'].ljust(max_len) + ' |', convert_from_bytes(r['weight']))
    for r in res_file:
        if r['weight'] > 1024 * 1024 * 512:
            print(r['name'].ljust(max_len) + ' |', convert_from_bytes(r['weight']))
    print(convert_from_bytes(sum_w, True))


if __name__ == '__main__':
    p = os.getcwd()
    show(p)
    raw = ''
    while raw != 'exit':
        raw = input('\n<%s># ' % p).strip()
        inp = raw.split()

        if len(inp) == 1:
            if raw == '.':
                show(p)
            elif raw == '\\':
                p = os.path.dirname(p)
                show(p)
            else:
                if os.path.exists(os.path.join(p, inp[0])):
                    p = os.path.join(p, inp[0])
                    show(p)
                else:
                    print('not exist!')
        elif len(inp) == 2:
            if inp[0] == 'cd':
                if os.path.exists(inp[1]):
                    p = inp[1]
                    show(p)
                else:
                    print('not exist!')


