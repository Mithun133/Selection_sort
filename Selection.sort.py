def selection_sort(data_list):
    length = len(data_list)

    for i in range(length - 1):
        min_index = i
        for j in range(i+1 , length):
            if data_list[j] < data_list[min_index]:
                min_index =j
        if min_index != i:
            temp = data_list[i]   
            data_list[i] = data_list[min_index]
            data_list[min_index] = temp
            

if __name__ == '__main__':
    data_list = [90, 60, 40, 20, 10, 30]
    selection_sort(data_list)
    print('Sorted list: ', data_list)




def selection_sort(data_list):
    lenght = len(data_list)

    for i in range(lenght - 1):
        min_index = i
        for j in range(i+1, lenght):
            if data_list[j] < data_list[min_index]:
                min_index = j
        if min_index !=i:
            temp = data_list[i]
            data_list[i] = data_list[min_index]
            data_list[min_index] = temp

if __name__ == '__main__':
    data_list = [35, 15, 45, 25, 5]
    selection_sort(data_list)
    print('Sorted list: ', data_list)





def selection_sort(data_list):
    lenght = len(data_list)

    for i in range(lenght - 1):
        min_index = i
        for j in range(i+1, lenght):
            if data_list[j] < data_list[min_index]:
                min_index = j
        if min_index !=i:
            temp = data_list[i]
            data_list[i] = data_list[min_index]
            data_list[min_index] = temp

if __name__ == '__main__':
    data_list = [200, 180, 160, 140, 120]
    selection_sort(data_list)
    print('Sorted list: ', data_list)





def selection_sort(data_list):
    lenght = len(data_list)

    for i in range(lenght - 1):
        min_index = i
        for j in range(i+1, lenght):
            if data_list[j] < data_list[min_index]:
                min_index = j
        if min_index !=i:
            temp = data_list[i]
            data_list[i] = data_list[min_index]
            data_list[min_index] = temp

if __name__ == '__main__':
    data_list = [300, 280, 260, 240, 220]
    selection_sort(data_list)
    print('Sorted list: ', data_list)



def selection_sort(data_list):
    lenght = len(data_list)

    for i in range(lenght - 1):
        min_index = i
        for j in range(i+1, lenght):
            if data_list[j] < data_list[min_index]:
                min_index = j
        if min_index !=i:
            temp = data_list[i]
            data_list[i] = data_list[min_index]
            data_list[min_index] = temp

if __name__ == '__main__':
    data_list = [400, 380, 360, 340, 320]
    selection_sort(data_list)
    print('Sorted list: ', data_list)