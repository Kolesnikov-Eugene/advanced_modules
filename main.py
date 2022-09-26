from application.salary import calculate_salary
from application.db.people import get_eployees
from datetime import date
import pymorphy2


today = date.today()

if __name__ == '__main__':
    get_eployees()
    calculate_salary()
    print(f'Today is {today}')

    #pymorphy example
    morph = pymorphy2.MorphAnalyzer()
    info = morph.parse('двери')
    print('ВСЯ ИНФОРМАЦИЯ О СЛОВЕ:')
    print(info)

    info = morph.parse('двери')[0]
    print('НАЧАЛЬНАЯ ФОРМА:')
    print(info.normal_form)

