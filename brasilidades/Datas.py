from datetime import datetime as d_t, timedelta as t_d

from sympy import re

class Datas:
    def __init__(self):
        self.momento_cadastro = d_t.today()

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 
                'Ago', 'Set', 'Out', 'Nov', 'Dez']
        mes_cadastro = self.momento_cadastro.month
        # meses retorna o inice de mes_cadastro como indice
        return meses[mes_cadastro -1]
        # o range do mes tem inicio no 1 e vai ate 12, 
        # a lista começa com 0 e vai ate 11
        # por isso usa-se -1

    def semana_dia(self):
        dias = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom']
        semana_dia = self.momento_cadastro.weekday()
        return dias[semana_dia]

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime('%d-%m-%Y %H:%M')
        return data_formatada

    def tempo_cadastro(self):
        tempo_cadstro = (d_t.today() + t_d(days = 30)) - self.momento_cadastro
        return tempo_cadstro