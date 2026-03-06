#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Обновление цен в wines.json из Excel таблицы
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
    # Читаем текущий JSON
    print("📖 Чтение wines.json...")
    with open('wines.json', 'r', encoding='utf-8') as f:
        wines = json.load(f)
    
    # Читаем Excel с новыми ценами
    print("📖 Чтение wines.xlsx...")
    df = pd.read_excel('wines.xlsx')
    
    # Счётчик обновлений
    updated = 0
    
    for index, row in df.iterrows():
        key = create_wine_key(row['product-full-name'])
        new_price = row['price-value-price']
        
        if key in wines:
            old_price = wines[key].get('price-value-price', '—')
            if old_price != new_price:
                wines[key]['price-value-price'] = new_price
                print(f"  🔄 {row['wine-card-title']}: {old_price} → {new_price}")
                updated += 1
        else:
            print(f"  ⚠️ Не найдено: {row['wine-card-title']}")
    
    # Сохраняем обновлённый JSON
    print(f"\n💾 Сохранение wines.json...")
    with open('wines.json', 'w', encoding='utf-8') as f:
        json.dump(wines, f, ensure_ascii=False, indent=2)
    
    print(f"\n🎉 Готово! Обновлено {updated} цен")

if __name__ == '__main__':
    main()