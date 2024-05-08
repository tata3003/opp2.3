def read_file_content(filename):
    """Функция для чтения содержимого файла."""
    with open(filename, 'r', encoding='utf-8') as file:
        return file.readlines()


def main():
    """Основная функция программы."""
    file_contents = []
    
    # Читаем содержимое всех файлов и сохраняем информацию о количестве строк и содержимом
    for i in range(1, 4):  # Используем цикл от 1 до 3, так как у нас три файла
        filename = f"{i}.txt"
        content = read_file_content(filename)
        file_contents.append((filename, len(content), content))
    
    # Сортируем список по количеству строк в файлах
    file_contents.sort(key=lambda x: x[1])

    # Записываем содержимое файлов в результирующий файл
    with open('result.txt', 'w') as result_file:
        for file_info in file_contents:
            filename, num_lines, content = file_info
            result_file.write(f"{filename}\n{num_lines}\n")
            result_file.writelines(content)

if __name__ == "__main__":
    main()
