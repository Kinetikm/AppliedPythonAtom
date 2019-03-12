import sys
import deparser
import builder

# Ваши импорты

if __name__ == '__main__':
    filename = sys.argv[1]
    try:
    	deparsed = deparser.depars(filename)
    	if deparsed[1] is "JSON":
    		callback = builder.buildJSONTable(deparsed[0], ['Оценка'])
    		#Вторым аргументом передаётся список наименований столбцов, которые будут выровнены по правому краю
    	else:
    		callback = builder.buildTSVTable(deparsed[0], [4])
    		#Вторым аргументом передаётся список номеров столбцов, которые будут выровнены по правому краю
    	if callback is False:
    		print("Формат не валиден")
    except ValueError:
    	print("Файл не валиден")

    # Ваш код
