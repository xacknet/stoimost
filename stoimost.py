import streamlit as st

# Функция расчета кадастровой стоимости земель
def calc_cadastral_value(area, coefficient, productivity):
    cadastral_value = area * coefficient * productivity
    return cadastral_value

# Основная часть приложения
st.title('Калькулятор кадастровой стоимости земель')
st.write('Введите данные для расчета кадастровой стоимости земель сельскохозяйственного назначения:')

# Поля для ввода данных
area = st.number_input('Площадь земельного участка, га', min_value=0.0, step=0.01)
coefficient = st.number_input('Коэффициент кадастровой стоимости, руб./га', min_value=0.0, step=0.01)
productivity = st.number_input('Удельная производительность, ц/га', min_value=0.0, step=0.01)

# Расчет кадастровой стоимости земель и вывод результата
if st.button('Рассчитать'):
    cadastral_value = calc_cadastral_value(area, coefficient, productivity)
    st.write(f'Кадастровая стоимость земель составляет {cadastral_value:.2f} руб.')
