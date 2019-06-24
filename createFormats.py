import itertools


def tupleToString(tup, seperator):
    str = seperator.join(tup)
    return str


date_seperators = ["-", "/", ".", " ", ""]
time_seperators = [":", ""]


##### Time dates ######
time_input_1 = ["H", "HH", "h", "hh"]
time_input_2 = ["m", "mm"]
time_input_3 = ["s", "ss"]
time_input_4 = ["S"]
time_input_5 = ["SS"]
time_input_6 = ["SSS"]
time_input_7 = ["a", "A", "Z", "ZZ"]

# print(list(itertools.product(time_input_1, time_input_2)))
# print(list(itertools.product(time_input_2, time_input_3)))
# print(list(itertools.product(time_input_1, time_input_2, time_input_3)))
# print(list(itertools.product(time_input_1, time_input_2, time_input_3, time_input_4)))
# print(list(itertools.product(time_input_1, time_input_2, time_input_3, time_input_4, time_input_5)))
# print(list(itertools.product(time_input_1, time_input_2, time_input_3, time_input_4, time_input_5, time_input_6)))

time_tuples = [
    # 1 and 2
    ('H', 'm'), ('H', 'mm'), ('HH', 'm'), ('HH', 'mm'), ('h',
                                                         'm'), ('h', 'mm'), ('hh', 'm'), ('hh', 'mm'),
    # 2 and 3
    ('m', 's'), ('m', 'ss'), ('mm', 's'), ('mm', 'ss'),
    # 1, 2, 3
    ('H', 'm', 's'), ('H', 'm', 'ss'), ('H', 'mm', 's'), ('H', 'mm', 'ss'), ('HH', 'm', 's'), ('HH', 'm', 'ss'
                                                                                               ), ('HH', 'mm', 's'), ('HH', 'mm', 'ss'), ('h', 'm', 's'), ('h', 'm', 'ss'), ('h', 'mm', 's'), ('h', 'mm',
                                                                                                                                                                                               'ss'), ('hh', 'm', 's'), ('hh', 'm', 'ss'), ('hh', 'mm', 's'), ('hh', 'mm', 'ss'),
    #1, 2, 3, 4
    ('H', 'm', 's', 'S'), ('H', 'm', 'ss', 'S'), ('H', 'mm', 's', 'S'), ('H', 'mm', 'ss', 'S'), ('HH', 'm', 's', 'S'), ('HH', 'm', 'ss', 'S'), ('HH', 'mm', 's', 'S'), ('HH', 'mm', 'ss', 'S'), ('h', 'm', 's', 'S'), ('h', 'm', 'ss', 'S'), ('h', 'mm', 's', 'S'), ('h', 'mm', 'ss', 'S'), ('hh', 'm', 's', 'S'), ('hh', 'm', 'ss',
                                                                                                                                                                                                                                                                                                                    'S'), ('hh', 'mm', 's', 'S'), ('hh', 'mm', 'ss', 'S'),
    #1, 2, 3, 4, 5
    ('H', 'm', 's', 'S', 'SS'), ('H', 'm', 'ss', 'S', 'SS'), ('H', 'mm', 's', 'S', 'SS'), ('H', 'mm', 'ss', 'S', 'SS'), ('HH', 'm', 's', 'S', 'SS'), ('HH', 'm', 'ss', 'S', 'SS'), ('HH', 'mm', 's', 'S', 'SS'), ('HH', 'mm', 'ss', 'S', 'SS'), ('h', 'm', 's', 'S', 'SS'), ('h', 'm', 'ss', 'S', 'SS'), ('h', 'mm', 's', 'S', 'SS'), ('h', 'mm', 'ss', 'S', 'SS'), ('hh', 'm', 's', 'S', 'SS'), ('hh', 'm', 'ss', 'S',
                                                                                                                                                                                                                                                                                                                                                                                                  'SS'), ('hh', 'mm', 's', 'S', 'SS'), ('hh', 'mm', 'ss', 'S', 'SS'),
    #1, 2,3,4,5,6
    ('H', 'm', 's', 'S', 'SS', 'SSS'), ('H', 'm', 'ss',
                                        'S', 'SS', 'SSS'), ('H', 'mm', 's', 'S', 'SS', 'SSS'),
    ('H', 'mm', 'ss', 'S', 'SS', 'SSS'), ('HH', 'm', 's', 'S', 'SS', 'SSS'), ('HH', 'm', 'ss', 'S', 'SS', 'SSS'), ('HH', 'mm', 's', 'S', 'SS', 'SSS'), ('HH', 'mm', 'ss', 'S', 'SS', 'SSS'), ('h', 'm', 's', 'S', 'SS', 'SSS'), ('h', 'm', 'ss', 'S', 'SS', 'SSS'), ('h', 'mm', 's', 'S', 'SS', 'SSS'), ('h', 'mm', 'ss', 'S', 'SS',
                                                                                                                                                                                                                                                                                                         'SSS'), ('hh', 'm', 's', 'S', 'SS', 'SSS'), ('hh', 'm', 'ss', 'S', 'SS', 'SSS'), ('hh', 'mm', 's', 'S', 'SS', 'SSS'), ('hh', 'mm', 'ss', 'S', 'SS', 'SSS'),
]


### Dates ######
date_input_1 = ["D", "Do", "DD"]
date_input_2 = ["M", "Mo", "MM", "MMM", "MMMM"]
date_input_3 = ["YY", "YYYY"]

date_input_4 = ["dd", "ddd", "dddd"]


# print(list(itertools.product(date_input_1, date_input_2)))
# print(list(itertools.product(date_input_2, date_input_3)))
# print(list(itertools.product(date_input_1, date_input_2, date_input_3)))
# print(list(itertools.product(date_input_2, date_input_1, date_input_3)))


# print(list(itertools.product(date_input_2, date_input_1)))
# print(list(itertools.product(date_input_3, date_input_2)))
# print(list(itertools.product(date_input_3, date_input_2, date_input_1)))
# print(list(itertools.product(date_input_3, date_input_1, date_input_2)))


# l = list(itertools.product(date_input_2, date_input_3))
# for elem in l:
#     print(elem)

date_tuples = [
    # 1,2
    ('D', 'M'), ('D', 'Mo'), ('D', 'MM'), ('D', 'MMM'), ('D', 'MMMM'), ('Do', 'M'), ('Do', 'Mo'), ('Do',
                                                                                                   'MM'), ('Do', 'MMM'), ('Do', 'MMMM'), ('DD', 'M'), ('DD', 'Mo'), ('DD', 'MM'), ('DD', 'MMM'), ('DD', 'MMMM'),
    # 2,3
    ('M', 'YY'), ('M', 'YYYY'), ('Mo', 'YY'), ('Mo', 'YYYY'), ('MM', 'YY'), ('MM',
                                                                             'YYYY'), ('MMM', 'YY'), ('MMM', 'YYYY'), ('MMMM', 'YY'), ('MMMM', 'YYYY'),
    # 1,2,3
    ('D', 'M', 'YY'), ('D', 'M', 'YYYY'), ('D', 'Mo', 'YY'), ('D', 'Mo', 'YYYY'), ('D', 'MM', 'YY'), ('D', 'MM', 'YYYY'), ('D', 'MMM', 'YY'), ('D', 'MMM', 'YYYY'), ('D', 'MMMM', 'YY'), ('D', 'MMMM', 'YYYY'
                                                                                                                                                                                          ), ('Do', 'M', 'YY'), ('Do', 'M', 'YYYY'), ('Do', 'Mo', 'YY'), ('Do', 'Mo', 'YYYY'), ('Do', 'MM', 'YY'), ('Do', 'MM', 'YYYY'), ('Do', 'MMM', 'YY'), ('Do', 'MMM', 'YYYY'), ('Do', 'MMMM', 'YY'), ('Do', 'MMMM', 'YYYY'), ('DD', 'M', 'YY'), ('DD', 'M', 'YYYY'), ('DD', 'Mo', 'YY'), ('DD', 'Mo', 'YYYY'), ('DD', 'MM', 'YY'), ('DD', 'MM', 'YYYY'), ('DD', 'MMM', 'YY'), ('DD', 'MMM', 'YYYY'), ('DD', 'MMMM', 'YY'), ('DD', 'MMMM', 'YYYY'),
    # 2,1,3
    ('M', 'D', 'YY'), ('M', 'D', 'YYYY'), ('M', 'Do', 'YY'), ('M', 'Do', 'YYYY'), ('M', 'DD', 'YY'), ('M', 'DD', 'YYYY'), ('Mo', 'D', 'YY'), ('Mo', 'D', 'YYYY'), ('Mo', 'Do', 'YY'), ('Mo', 'Do', 'YYYY'), (
        'Mo', 'DD', 'YY'), ('Mo', 'DD', 'YYYY'), ('MM', 'D', 'YY'), ('MM', 'D', 'YYYY'), ('MM', 'Do', 'YY'), ('MM', 'Do', 'YYYY'), ('MM', 'DD', 'YY'), ('MM', 'DD', 'YYYY'), ('MMM', 'D', 'YY'), ('MMM', 'D', 'YYYY'), ('MMM', 'Do', 'YY'), ('MMM', 'Do', 'YYYY'), ('MMM', 'DD', 'YY'), ('MMM', 'DD', 'YYYY'), ('MMMM', 'D', 'YY'), ('MMMM', 'D', 'YYYY'), ('MMMM', 'Do', 'YY'), ('MMMM', 'Do', 'YYYY'), ('MMMM', 'DD', 'YY'
                                                                                                                                                                                                                                                                                                                                                                                                          ), ('MMMM', 'DD', 'YYYY'),


    # ------

    #2, 1
    ('M', 'D'), ('M', 'Do'), ('M', 'DD'), ('Mo', 'D'), ('Mo', 'Do'), ('Mo', 'DD'), ('MM', 'D'), ('MM',
                                                                                                 'Do'), ('MM', 'DD'), ('MMM', 'D'), ('MMM', 'Do'), ('MMM', 'DD'), ('MMMM', 'D'), ('MMMM', 'Do'), ('MMMM', 'DD'),
    # 3,2
    ('YY', 'M'), ('YY', 'Mo'), ('YY', 'MM'), ('YY', 'MMM'), ('YY', 'MMMM'), ('YYYY',
                                                                             'M'), ('YYYY', 'Mo'), ('YYYY', 'MM'), ('YYYY', 'MMM'), ('YYYY', 'MMMM'),
    # 3,2,1
    ('YY', 'M', 'D'), ('YY', 'M', 'Do'), ('YY', 'M', 'DD'), ('YY', 'Mo', 'D'), ('YY', 'Mo', 'Do'), ('YY', 'Mo', 'DD'), ('YY', 'MM', 'D'), ('YY', 'MM', 'Do'), ('YY', 'MM', 'DD'), ('YY', 'MMM', 'D'), ('YY',
                                                                                                                                                                                                       'MMM', 'Do'), ('YY', 'MMM', 'DD'), ('YY', 'MMMM', 'D'), ('YY', 'MMMM', 'Do'), ('YY', 'MMMM', 'DD'), ('YYYY', 'M', 'D'), ('YYYY', 'M', 'Do'), ('YYYY', 'M', 'DD'), ('YYYY', 'Mo', 'D'), ('YYYY', 'Mo', 'Do'
                                                                                                                                                                                                                                                                                                                                                                                               ), ('YYYY', 'Mo', 'DD'), ('YYYY', 'MM', 'D'), ('YYYY', 'MM', 'Do'), ('YYYY', 'MM', 'DD'), ('YYYY', 'MMM', 'D'), ('YYYY', 'MMM', 'Do'), ('YYYY', 'MMM', 'DD'), ('YYYY', 'MMMM', 'D'), ('YYYY', 'MMMM', 'Do'
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ), ('YYYY', 'MMMM', 'DD'),
    # 3,1,2
    ('YY', 'D', 'M'), ('YY', 'D', 'Mo'), ('YY', 'D', 'MM'), ('YY', 'D', 'MMM'), ('YY', 'D', 'MMMM'), ('YY', 'Do', 'M'), ('YY', 'Do', 'Mo'), ('YY', 'Do', 'MM'), ('YY', 'Do', 'MMM'), ('YY', 'Do', 'MMMM'), ('YY', 'DD', 'M'), ('YY', 'DD', 'Mo'), ('YY', 'DD', 'MM'), ('YY', 'DD', 'MMM'), ('YY', 'DD', 'MMMM'), ('YYYY', 'D', 'M'), ('YYYY', 'D', 'Mo'), ('YYYY', 'D', 'MM'), ('YYYY', 'D', 'MMM'), ('YYYY', 'D', 'MMMM'), ('YYYY', 'Do', 'M'), ('YYYY', 'Do', 'Mo'), ('YYYY', 'Do', 'MM'), ('YYYY', 'Do', 'MMM'), ('YYYY', 'Do', 'MMMM'), ('YYYY', 'DD', 'M'), ('YYYY', 'DD', 'Mo'), ('YYYY', 'DD', 'MM'), ('YYYY', 'DD', 'MMM'
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              ), ('YYYY', 'DD', 'MMMM')
]

# for sep in time_seperators:
#     for elem in time_tuples:
#         print("\"" + tupleToString(elem, sep) + "\",")
