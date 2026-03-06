#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Генерация wines.json из Excel таблицы
"""

import pandas as pd
import json
import re

def create_wine_key(name):
    """Создаёт URL-безопасный ключ из названия вина"""
    key = name.lower()
    key = re.sub(r'[^a-zа-яё0-9]', '-', key)
    key = re.sub(r'-+', '-', key)
    key = key.strip('-')
    return key

def main():
    # Читаем Excel файл
    print("📖 Чтение wines.xlsx...")
    df = pd.read_excel('wines.xlsx')
    
    # Создаём словарь вин
    wines = {}
    
    for index, row in df.iterrows():
        # Создаём ключ для URL
        key = create_wine_key(row['product-full-name'])
        
        # Преобразуем строку в словарь
        wine_data = row.to_dict()
        
        # Добавляем ключ для быстрого поиска
        wine_data['wine-key'] = key
        
        wines[key] = wine_data
        print(f"  ✅ {row['wine-card-title']} ({row['price-value-price']})")
    
    # Сохраняем JSON
    print("\n💾 Сохранение wines.json...")
    with open('wines.json', 'w', encoding='utf-8') as f:
        json.dump(wines, f, ensure_ascii=False, indent=2)
    
    print(f"\n🎉 Готово! Сгенерировано {len(wines)} карточек вин")
    print(f"📁 Файл: wines.json ({len(json.dumps(wines))} байт)")

if __name__ == '__main__':
    main()