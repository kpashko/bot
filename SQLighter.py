import sqlite3


class SQLighter:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def select_all(self):
        """ Получаем все строки """
        with self.connection:
            return self.cursor.execute('SELECT * FROM healthy_day').fetchall()

    def select_single(self, rownum):
        """ Получаем одну строку с номером rownum """
        with self.connection:
            return self.cursor.execute('SELECT * FROM healthy_day WHERE id = ?', (rownum,)).fetchall()[0]

    def count_rows(self):
        """ Считаем количество строк """
        with self.connection:
            result = self.cursor.execute('SELECT * FROM healthy_day').fetchall()
            return len(result)

    def close(self):
        """ Закрываем текущее соединение с БД """
        self.connection.close()

    def get_rand(self):
        """ Получаем рандомную строку"""
        with self.connection:
            return self.cursor.execute('SELECT * FROM healthy_day ORDER BY RANDOM() LIMIT 1').fetchone()

    def get_morning(self):
        """ Получаем масив утренних упражнений, вида file_id, name, description"""
        with self.connection:
            return self.cursor.execute('SELECT file_id, name, description FROM healthy_day INNER JOIN taggings ON taggings.fileID = healthy_day.id WHERE taggings.tagID == 1')

    def get_core(self):
        """ Получаем утре строку"""
        with self.connection:
            return self.cursor.execute('SELECT file_id, name, description FROM healthy_day INNER JOIN taggings ON taggings.fileID = healthy_day.id WHERE taggings.tagID == 4')
