import os

def replace_text_in_html_files(directory, old_text, new_text):
    # Перебираем все файлы в указанной директории
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                try:
                    # Читаем содержимое файла
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Заменяем текст
                    new_content = content.replace(old_text, new_text)
                    
                    # Записываем обратно в файл
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    
                    print(f"Processed file: {file_path}")
                except Exception as e:
                    print(f"Failed to process file: {file_path} with error: {e}")

# Укажите здесь путь к директории с HTML-файлами, текст который нужно заменить, и новый текст
directory = './'
old_text = 'allfordj.ru'
new_text = 'fotobuffer.ru'
#new_text = 'https://www.allfordij.ru/bitrix/'

replace_text_in_html_files(directory, old_text, new_text)
