# -*- coding: utf-8 -*-
"""Funciones"""
import pandas as pd
from datetime import datetime

def calculadora_precio(cantidad, prc_unitario):
    df_params = pd.read_excel(io=r'/home/gondaviza/Escritorio/agilebyte/ejemplo_parametros/ejemplo_parametros/src/extras/ejemplo_parametros.xlsx')
    today = datetime.now().strftime('%A')

    df_params = df_params[df_params["dia"]==today][['coef_ajuste']].reset_index(drop=True)
    coef = df_params["coef_ajuste"].values[0]
    resultado = cantidad * prc_unitario * coef
    return resultado



#res = calculadora_precio(3,5)