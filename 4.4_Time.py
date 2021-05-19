
def gen_secs():
    for i in range(60):
        yield i


def gen_minutes():
    for i in range(60):
        yield i


def gen_hours():
    for i in range(24):
        yield i


def gen_time():
    for hours in gen_hours():
        for minutes in gen_minutes():
            for seconds in gen_secs():
                yield (f'{hours:02}:{minutes:02}:{seconds:02}')

for gt in gen_time():
    print(gt)
