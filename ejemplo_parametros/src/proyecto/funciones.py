# -*- coding: utf-8 -*-
"""Funciones"""
import pandas as pd
from datetime import datetime

def calculadora_precio(cantidad, prc_unitario):
    df_params = pd.read_excel(io=r'/home/gondaviza/Escritorio/agilebyte/ejemplo_parametros/ejemplo_parametros/src/extras/ejemplo_parametros.xlsx')
    day_of_week = datetime.now().strftime('%A')
    today = datetime.now()
    df_params_filtered = df_params[(df_params["dia"]==day_of_week) &
                                   (today >= df_params["dat_alta"]) &
                                   (today <= df_params["dat_baja"])
    ][['coef_ajuste']].reset_index(drop=True)
    coef = df_params_filtered["coef_ajuste"].values[0]
    resultado = cantidad * prc_unitario * coef
    return resultado



#res = calculadora_precio(3,5)
