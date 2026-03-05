disceta = 1.44 # Информационный объем дискеты равен 1,44 Мб
kol_vo_str = 100 # Количество страниц в книге - 100
chisl_strok_na_str = 50 # Число строк на странице - 50
kol_vo_simv_v_stroke = 25 # Количество символов в строке - 25
obiom_simv = 4 # Для хранения кода одного символа нужно 4 байта.
disceta *= 1024 # Перевод из МБ в КБ
disceta *= 1024 # Перевод из КБ в байты
ves_knigi = kol_vo_str * chisl_strok_na_str * kol_vo_simv_v_stroke * obiom_simv # Считаем общий объём книги
kol_vo_knig = disceta // ves_knigi # считаем количество книг
print("Количество книг, помещающихся на дискету:", int(kol_vo_knig)) # int создает целочисленное значение

