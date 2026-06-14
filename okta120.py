class matrix3:
    def __init__(self,arr):
        self.row = len(arr)
        self.col = len(arr[0])
        self.data = arr
            
    def ukuran(self):
        print(f"Ukuran matrix: {self.row} x {self.col}")

    def T(self):
        trans = [[0 for _ in range(self.row)] for _ in range(self.col)]
        for i in range(self.row):
            for j in range(self.col):
                trans[j][i]=self.data[i][j]

        self.data = trans
        self.row, self.col = self.col, self.row
        print(f"transpose: {trans}")
        return trans

    def tambah(self, arr1, arr2):
        if arr1.row != arr2.row or arr1.col != arr2.col:
            print("error, jumlah matrix  tidak sama")
            return None
        hasil = [[0 for _ in range(self.col)] for _ in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                hasil[i][j]= arr1.data[i][j]+ arr2.data[i][j]
        return hasil        
    
    def kurang(self, arr1,  arr2):
        if arr1.row != arr2.row or arr1.col != arr2.col:
            print("error, jumlah matrix  tidak sama")
            return None
        hasil = [[0 for _ in range(self.col)] for _ in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                hasil[i][j]= arr1.data[i][j]- arr2.data[i][j]
        return hasil   
    
    def kali(self, arr1, arr2):
        if arr1.row != arr2.row or arr1.col != arr2.col:
            print("error, jumlah matrix  tidak sama")
            return None
        
        hasil = [[0 for _ in range(arr2.col)] for _ in range(arr1.row)]
        for i in range(arr1.row):
            for j in range(arr2.col):
                for l in range(arr1.col):
                    hasil[i][j] += arr1.data[i][l] * arr2.data[l][j]
        return hasil 
        
    def minor(self):
        hasil = [[0 for _ in range(3)] for _ in range(3)]
        for i in range (3):
            for j in range(3):
                ordo= [row[:j] + row[j+1:] for row in (self.data[:i] + self.data[i+1:])]
                hasil[i][j]= (ordo[0][0]*ordo[1][1]) - (ordo[0][1]*ordo[1][0])
        return hasil

    def detm(self):
        kof1 = [[0 for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                ordo= [row[:j] + row[j+1:] for row in (self.data[:i] + self.data[i+1:])]
                kof1[i][j] = self.data[0][j]*((ordo[0][0]*ordo[1][1]) - (ordo[1][0]*ordo[0][1]))

        det = kof1[0][0]-kof1[0][1]+kof1[0][2]
        return det

    def kof(self):
        minor = self.minor()
        kofak =[[0 for _ in range(self.col)] for _ in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                if (i+j) %2 != 0:
                    kofak[i][j]=minor[i][j] * (-1)
                else:
                    kofak[i][j]=minor[i][j] 
        return kofak
    
    def adj(self):
        kof= self.kof()
        kofm = matrix3(kof)
        adj = kofm.T()
        return adj
    
    def invers(self):
        det = self.detm()
        adj = self.adj()
        matriks = [[0 for _ in range(self.col)] for _ in range(self.row)]
        if det == 0:
            print("matriks tidak memiliki invers")
            return None
        
        for i in range(self.row):
            for j in range(self.col):
                matriks[i][j]= adj[i][j]/det
        return matriks