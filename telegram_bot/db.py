import sqlite3
'''

'''

dic = {
    'сметана' : 2.2,
    'мука' : 10,
    'масло' : 33,
    'соль' : 100,
    'сырный' : 162,
    'сорбат' : 1000,
    'томат' : 10,
    'коробка' : 96
}

class ADD():
    def __init__(self, item=None):
        self.connect = sqlite3.connect("remainder.db")
        self.cursor = self.connect.cursor()
        self.file = "remainder"
        self.item = item

    def __check_value(self):
        self.__check = self.cursor.execute(f"SELECT product FROM {self.file}").fetchall()
        self.__flag = False
        self.k, self.v = self.item
        if len(self.__check) == 0:
            return self.__flag
        for ch in self.__check:
            if self.k in ch:
                self.__flag = True
                break
        return self.__flag

    def get_add(self):
        self.item = self.item.split()
        self.item = tuple(self.item[1:])
        if self.__check_value() == False:
            self.cursor.execute(f'INSERT INTO {self.file} VALUES(?, ?)', (self.k, self.v))
        else:
            self.cursor.execute(f"UPDATE {self.file} SET remain == ? WHERE product == ?", (self.v, self.k))
        self.connect.commit()

    #---------Вывод--------------------

    def set_output(self):
        data = self.cursor.execute(f"SELECT * FROM {self.file}").fetchall()
        temp = []
        for tup in data:
            k, v = tup
            temp.append(k + ' ' +  v)
        st = ''
        for i in temp:
            st += str(i)+ '\n'

        return st

#---------------------------УДАЛЕНИЕ--------------------------------------
    def data_delete(self):
        self.cursor.execute(f'DELETE FROM {self.file}')
        self.connect.commit()


class BUY(ADD):
    def __init__(self, item=None):
        self.item = item
        self.connect = sqlite3.connect("buy.db")
        self.cursor = self.connect.cursor()
        self.file = "buy"


    def get_sum(self, kol):
        item = self.cursor.execute(f"SELECT * from {self.file}").fetchall()
        self.sum = 0.0
        for i in item:
            k,v = i
            if k.lower() in dic.keys():
                self.sum += ((float(kol) * 0.13) / float(dic[k])) * float(v)
            elif k.lower() in 'коробка':
                self.sum += float(kol) / float(dic[k]) * float(v)
            elif k.lower() == 'платинка':
                self.sum += float(v) * float(kol)
            elif k.lower() == 'стаканчик':
                self.sum += float(v) * float(kol)
            self.sum += float(v)
        return self.sum

    def get_output(self):
        num = self.item.split()[1]
        return format(self.get_sum(num) / float(num), '.2f')
