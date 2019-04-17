def timer_log(time, method):
    file_name = "timer_log.txt"
    file_handler = open(file_name, 'a')
    file_handler.write(method + " : ")
    file_handler.write(str(time) + '\n')
    file_handler.close()
