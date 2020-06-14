from math import isnan

import os

import pandas as pd

from app.models import Wine


def isinteger(a):
    try:
        int(a)
        return True
    except ValueError:
        return False


def read_terroir_excel(file_name, sheet_name):

    df = pd.read_excel(open(os.path.join(os.getcwd(), 'app', file_name), 'rb'), sheet_name=sheet_name)

    for _, row in df.iterrows():
        d = row.to_dict()
        name = d['제품명(영문)']
        name_ko = d['제품명']
        location = d['지역']
        extra_info = d['비고']

        official_price = d['권장소비자가'] if isinteger(d['권장소비자가']) else None
        reduced_price = d['떼루아 행사가'] if isinteger(d['떼루아 행사가']) else None

        wine = Wine(
            name=name, name_ko=name_ko, location=location,
            reduced_price=reduced_price,
            official_price=official_price,
            extra_info=extra_info, shop='떼루아',
        )
        wine.save()


if __name__ == '__main__':
    read_terroir_excel()
