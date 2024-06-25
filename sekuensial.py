def sequential_search(books, title):
   
    for i in range(len(books)):
        if books[i]['title'].lower() == title.lower():
            return i 
    return -1 

def add_book(books):
   
    title = input("Masukkan judul buku: ")
    new_book = {
        'title': title
    }
    books.append(new_book)
    print(f"Buku '{title}' berhasil ditambahkan.\n")

def search_book(books):
   
    title = input("Masukkan judul buku yang ingin dicari: ")
    index = sequential_search(books, title)
    if index != -1:
        print(f"Buku '{books[index]['title']}' ditemukan.")
    else:
        print(f"Buku dengan judul '{title}' tidak ditemukan.")

def display_books(books):
   
    if not books:
        print("Belum ada buku dalam daftar.")
    else:
        print("Daftar Buku:")
        for idx, book in enumerate(books):
            print(f"{idx+1}. '{book['title']}'")
        print()

def main():
    books = []

    while True:
        print("===== MENU =====")
        print("1. Tambahkan buku")
        print("2. Cari buku")
        print("3. Tampilkan semua buku")
        print("4. Keluar")

        choice = input("Pilih menu (1/2/3/4): ")

        if choice == '1':
            add_book(books)
        elif choice == '2':
            search_book(books)
        elif choice == '3':
            display_books(books)
        elif choice == '4':
            print("Matur suwun .")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

if __name__ == "__main__":
    main()
