def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
    
        elif arr[mid] > target:
            right = mid - 1

        else:
            left = mid + 1
    
    return -1

def get_user_input():
    arr = []
    while True:
        user_input = input("Masukkan angka (atau ketik 'urutkan' untuk selesai): ")
        if user_input.lower() == 'urutkan':
            break
        try:
            number = int(user_input)
            arr.append(number)
        except ValueError:
            print("Masukkan angka yang valid.")
    return arr

arr = get_user_input()
arr.sort()
print(f"Array yang diurutkan: {arr}")

target = int(input("Masukkan angka yang ingin dicari: "))

result = binary_search(arr, target)

if result != -1:
    print(f"Elemen ditemukan di indeks {result}")
else:
    print("Elemen tidak ditemukan di array")
