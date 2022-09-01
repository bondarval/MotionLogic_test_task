import pandas as pd

restaurant_df = pd.read_csv('restaurants.csv')
# список франшиз фаст фуда
restaurant_df['franchise'].tolist()
# выборка по ресторанам КФС
kfc_number = restaurant_df[restaurant_df['franchise'].isin(['KFC'])]
# kfc_number_malls
# kfc_number_stations
# kfc_number_aeroports
# выборка по заведениям "Бургер Кинг"
bk_number = restaurant_df[restaurant_df['franchise'].isin(['BurgerKing'])]
# bk_number_malls
# bk_number_stations
# bk_number_aeroports
# выборка по заведениям бывш. "МакДональдс" ныне "Вкусно - и точка"
mcd_number = restaurant_df[restaurant_df['franchise'].isin(['Вкусно — и точка'])]
# mcd_number_malls
# mcd_number_stations
# mcd_number_aeroports
