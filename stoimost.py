import streamlit as st

st.title('Калькулятор кадастровой стоимости земель сельскохозяйственного назначения')

# Получение данных от пользователя
ploshad = st.number_input('Введите площадь земельного участка, га:', min_value=0.0, step=0.1)
kategoria = st.selectbox('Выберите категорию земельного участка:', ('I', 'II', 'III', 'IV', 'V', 'VI'))
uchastok = st.selectbox('Выберите тип земельного участка:', ('Земли сельскохозяйственного назначения', 'Земли населенных пунктов'))

# Расчет кадастровой стоимости
if kategoria == 'I':
    if uchastok == 'Земли сельскохозяйственного назначения':
        stoimost = ploshad * 115000
    else:
        stoimost = ploshad * 460000
elif kategoria == 'II':
    if uchastok == 'Земли сельскохозяйственного назначения':
        stoimost = ploshad * 75000
    else:
        stoimost = ploshad * 300000
elif kategoria == 'III':
    if uchastok == 'Земли сельскохозяйственного назначения':
        stoimost = ploshad * 45000
    else:
        stoimost = ploshad * 180000
elif kategoria == 'IV':
    if uchastok == 'Земли сельскохозяйственного назначения':
        stoimost = ploshad * 25000
    else:
        stoimost = ploshad * 100000
elif kategoria == 'V':
    if uchastok == 'Земли сельскохозяйственного назначения':
        stoimost = ploshad * 15000
    else:
        stoimost = ploshad * 60000
else:
    if uchastok == 'Земли сельскохозяйственного назначения':
        stoimost = ploshad * 7500
    else:
        stoimost = ploshad * 30000

# Вывод результата
st.write('Кадастровая стоимость земельного участка составляет:', stoimost, '