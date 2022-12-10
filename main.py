
def uygun_mu(matrix, satir, sutun, sayi_degeri):

    # bulunduğumuz satırda sayının aynısı var mı?
    for sayi in range(9):
        if matrix[satir][sayi] == sayi_degeri:
            return False

    # bulunduğumuz sütunda sayının aynısı var mı?
    for sayi in range(9):
        if matrix[sayi][sutun] == sayi_degeri:
            return False

    # içinde bulunduğumuz 3x3'lük matrixte sayının aynısı var mı?
    yeni_satir = satir - satir % 3
    yeni_sutun = sutun - sutun % 3
    for i in range(3):
        for j in range(3):
            if matrix[yeni_satir + i][yeni_sutun + j] == sayi_degeri:
                return False

    return True


def solver(matrix, satir = 0, sutun = 0):
    # tüm satır ve sütunları gezmek için oluşturduğumuz kontrol
    if sutun == 9:
        satir += 1
        sutun = 0
        if satir == 9:
            return True

    # bulunduğumuz yerde hali hazırda sayı verilmişse recursion yapıp yeni sütuna geçelim
    if matrix[satir][sutun] > 0:
        return solver(matrix, satir, sutun + 1)

    # 1 den 9'a kadar olan sayılardan biri uygunsa onu ilgili yere atıyoruz
    for sayi_degeri in range(1,10):
        if uygun_mu(matrix, satir, sutun, sayi_degeri):
            matrix[satir][sutun] = sayi_degeri

            # bulunduğumuz sayıyı atadık. Sağına atayacağımız sayı uygun mu diye recursion ile yeni sütuna geçiyoruz
            if solver(matrix, satir, sutun + 1):
                return True

        matrix[satir][sutun] = 0

    return False




if __name__ == "__main__":
    sudoku = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    if solver(sudoku):
        for i in range(9):
            for j in range(9):
                print(sudoku[i][j], end=' ')
            print("")
    else:
        print("Bu sudoku yanlıştır, çözülemez")