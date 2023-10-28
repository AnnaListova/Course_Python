disk = 1.44 #Мб
pages = 100
strings = 50
symbols = 25
one_code_symbol = 4 #байта

disk_mb = disk * 1024 * 1024 #байтов в Мбайтах
all_symbols = pages * strings * symbols #количество всех символов в одной книге
volume_all_symbols = one_code_symbol * all_symbols #объем в байтах всех символов в одной книге
books = int (disk_mb // volume_all_symbols)


print("Количество книг, помещающихся на дискету:", books)
