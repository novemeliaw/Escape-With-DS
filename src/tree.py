class Node:
    def __init__(self, value, text: list, choice: list, nextVal : list, asset : list) -> None:
        self.data = value
        self.text = text
        self.choice = choice
        self.nextVal = nextVal
        self.asset = asset
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self)-> None:
        # Merupakan kepala paling atas
        self.root = None

    def insert(self, value, text, choice, nextValue, asset):
        #traverse
        def DFS(curr, value, text, choice, nextValue, asset):
            if curr == None:
                return Node(value, text, choice, nextValue, asset)
            # print(curr.data)
            #insert left
            if value < curr.data :
                curr.left = DFS(curr.left, value, text, choice, nextValue, asset)
            #insert right
            elif value > curr.data:
                curr.right = DFS(curr.right, value, text, choice, nextValue, asset)
            return curr

        #check if root is empty
        if self.root == None :
            self.root = Node(value, text, choice, nextValue, asset)
        else :
            self.root = DFS(self.root, value, text, choice, nextValue, asset)
        

    def search(self, value):
        def DFS(curr, value):
            if curr.data == value or curr.data == None:
                return curr 
            
            #search left
            if value < curr.data:
                return DFS(curr.left, value)
            #search right
            elif value > curr.data:
                return DFS(curr.right,value)
        return DFS(self.root,value)
    
    def printIn(self):
        if self.left:
            self.left.printIn()
        print(self.data, end = " -> ")

        if self.right:
            self.right.printIn()

    def print_tree(self, val="data", left="left", right="right"):
        def display(root, val=val, left=left, right=right):
            """Returns list of strings, width, height, and horizontal coordinate of the root."""
            # No child.
            if getattr(root, right) is None and getattr(root, left) is None:
                line = '%s' % getattr(root, val)
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            # Only left child.
            if getattr(root, right) is None:
                lines, n, p, x = display(getattr(root, left))
                s = '%s' % getattr(root, val)
                u = len(s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

            # Only right child.
            if getattr(root, left) is None:
                lines, n, p, x = display(getattr(root, right))
                s = '%s' % getattr(root, val)
                u = len(s)
                first_line = s + x * '_' + (n - x) * ' '
                second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

            # Two children.
            left, n, p, x = display(getattr(root, left))
            right, m, q, y = display(getattr(root, right))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * \
                '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + \
                (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + \
                [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2

        lines, *_ = display(self.root, val, left, right)
        for line in lines:
            print(line)

dialogueTree = BinaryTree()
# Root
asset = ['Background/persimpangan jalan.jpg', 'Character/prince2.png']
text = ['Gawat, aku harus mencari jalan pulang.', 'Bisa-bisanya keamanan kerajaan ku lemah seperti ini,', 'saat kembali aku harus menginterogasi pengawalku', 'Wah ada dua jalan aku harus pilih yang mana ya?']
choice = ['Jalan kiri', 'Jalan kanan']
nextVal = [66,  194]
dialogueTree.insert(130,text,choice,nextVal, asset)

#Binary Tree 66
asset = ['Background/hutan siang.jpg', 'Character/prince2.png', 'Character/ds-icon.png']
text = ['Apa ini?', 'Halo Halo Loha, aku DS, yang akan menemani mu di perjalanan ini.', 'Kamu kenapa bisa ada disini?', 'Aku diciptakan untuk membantu mereka yang tersesat di hutan ini.', 'Baiklah.', 'Struktur data yang menyimpan elemen dengan konsep fifo']
choice = ['Queue', 'Stack']
nextVal = [34,  98]
dialogueTree.insert(66,text,choice,nextVal, asset)

#Binary Tree 34
asset = ['Background/hutan siang.jpg', 'Character/prince2.png', 'Character/ds-icon.png']
text = ['Lihat!!! Aku berhasil mendapatkan 1 digit.', 'Selamat, kamu hanya perlu mencari 1 digit lagi.', 'Aku tidak sabar untuk segera pulang', 'mari kita lanjutkan perjalanan ini.', 'Integer merupakan tipe data apa?']
choice = ['Tunggal', ' Majemuk']
nextVal = [18,  50]
dialogueTree.insert(34,text,choice,nextVal, asset)

#Binary Tree 18
asset = ['Background/dalam rumah kosong.png', 'Character/prince2.png', 'Character/villain1.png', 'Character/villain2.png']
text = ['Ayo cari pangeran itu, dia pasti tidak jauh dari sini.', 'Kita sudah mencari semalaman dan tidak menemukannya.', 'Apa mungkin dia sudah berhasil kembali ke kerajaannya?', 'Tidak mungkin! Cepat cari lagi, kita harus menemukannya.', 'Itu adalah orang-orang yang menculikku! Aku harus kabur dari sini.',  'Node tidak memiliki parent node, hanya memiliki children disebut?']
choice = ['Root', 'Leaf']
nextVal = [10,  26]
dialogueTree.insert(18,text,choice,nextVal, asset)

#Binary Tree 10
asset = ['Background/sungai.jpg', 'Others/row boat.png']
text = ['Aku harus menyeberangi sungai ini.', 'Bagaimana caraku untuk menyeberang?', 'Jenis graph yang dapat menjelajah 2 arah adalah']
choice = ['Undirected', 'Directed']
nextVal = [4,  8]
dialogueTree.insert(10,text,choice,nextVal, asset)

#Binary Tree 6
asset = ['Background/kerajaan di kejauhan.jpg', 'Character/prince2.png', ' Character/ds-icon.png']
text = ['Aku mendapatkan digit kedua dalam perjalanan ini!', 'Selamat, kamu sudah berhasil mengumpulkan semua digit yang diperlukan!', 'Ayo kita berjalan lagi, jalan ini sudah dekat dengan kerajaanku!']
choice = ['Lanjut','']
nextVal = [4,0]
dialogueTree.insert(6,text,choice,nextVal, asset)

#Binary Tree 4
asset = ['Background/castle.jpg', 'Character/prince2.png']
text = ['Akhirnya aku bisa pulang!', 'Aku akan segera menginterogasi pengawal ku yang tidak becus menjagaku ini', 'Welcome Home' ]
choice = ['', '']
nextVal = [0, 0]
dialogueTree.insert(4,text,choice,nextVal, asset)

#Binary Tree 8
asset = ['Background/castle.jpg', 'Character/prince2.png']
text = ['Ternyata benar dia ada di sini.', 'Untung saja dia belum sempat masuk. Ayo tangkap dia!', 'Tidakkk!!!', 'Game Over']
choice = ['', '']
nextVal = [0, 0]
dialogueTree.insert(8,text,choice,nextVal, asset)

#Binary Tree 14
asset = ['Background/kerajaan di kejauhan.jpg', 'Character/prince2.png', 'Character/ds-icon.png']
text = ['Aku mendapatkan digit kedua dalam perjalanan ini!', 'Selamat, kamu sudah berhasil mengumpulkan semua digit yang diperlukan!', 'Ayo kita berjalan lagi, jalan ini sudah dekat dengan kerajaanku!']
choice = ['', '']
nextVal = [12,16]
dialogueTree.insert(14,text,choice,nextVal, asset)

#Binary Tree 12
asset = ['Background/castle.jpg', 'Character/prince2.png']
text = ['Akhirnya aku bisa pulang! Aku akan segera menginterogasi pengawal ku yang tidak becus menjagaku ini', 'Welcome Home']
choice = ['', '']
nextVal = [0, 0]
dialogueTree.insert(12,text,choice,nextVal, asset)

#Binary Tree 16
asset = ['Background/castle.jpg', 'Character/prince2.png', 'Character/villain1.png', 'Character/villain2.png']
text = ['Ternyata benar dia ada di sini.', 'Untung saja dia belum sempat masuk. Ayo tangkap dia!', 'Tidakkk!!!', 'Game Over']
choice = ['', '']
nextVal = [0, 0]
dialogueTree.insert(16,text,choice,nextVal, asset)

#Binary Tree 26
asset = ['Background/sungai.jpg', 'Character/prince2.png']
text = ['Air sungai ini sangat dingin!', 'Tetapi sepertinya aku tidak punya pilihan lain selain berenang.', 'Queue merupakan struktur data apa?']
choice = ['Majemuk', 'Sederhana']
nextVal = [22,  30]
dialogueTree.insert(26,text,choice,nextVal, asset)

#Binary Tree 22
asset = ['Background/sungai.jpg', 'Character/prince2.png']
text = ['Tidak sia-sia aku berenang ke sini,' , 'ternyata aku mendapatkan digit terakhir yang kuperlukan! Tetapi aku sangat kedinginan.', 'Ah, aku akan menghangatkan diri sebentar dengan menyalakan api unggun.', ' "by boundary" dan "by shifting" merupakan jenis dari']
choice = ['folding', 'carry']
nextVal = [20,  24]
dialogueTree.insert(22,text,choice,nextVal, asset)

#Binary Tree 20
asset = ['Background/castle.jpg', 'Character/prince2.png']
text = ['Akhirnya aku bisa pulang! Aku akan segera menginterogasi pengawal ku yang tidak becus menjagaku ini', 'Welcome Home']
choice = ['', '']
nextVal = [0, 0]
dialogueTree.insert(20,text,choice,nextVal, asset)

#Binary Tree 24
asset = ['Background/castle.jpg', 'Character/prince2.png', 'Character/villain1.png', 'villain2.png']
text = ['Ternyata benar dia ada di sini.', 'Untung saja dia belum sempat masuk. Ayo tangkap dia!', 'Tidakkk!!!', 'Game Over']
choice = ['', '']
nextVal = [0, 0]
dialogueTree.insert(24,text,choice,nextVal, asset)

#Binary Tree 30
asset = ['Background/sungai.jpg', 'Character/prince2.png']
text = ['Tidak sia-sia aku berenang ke sini,','ternyata aku mendapatkan digit terakhir yang kuperlukan!','Tetapi aku sangat kedinginan.', 'Ah, aku akan menghangatkan diri sebentar dengan menyalakan api unggun.', 'Salah satu metode transversal tree']
choice = ['Inorder', 'Postorder']
nextVal = [28,32]
dialogueTree.insert(30,text,choice,nextVal, asset)

#Binary Tree 28
asset = ['Background/castle.jpg', 'Character/prince2.png']
text = ['Akhirnya aku bisa pulang!','Aku akan segera menginterogasi pengawalku yang tidak becus menjagaku ini', 'Welcome Home']
choice = ['', '']
nextVal = [0, 0]
dialogueTree.insert(28,text,choice,nextVal, asset)

#Binary Tree 32
asset = ['Background/castle.jpg', 'Character/prince2.png', 'Character/villain1.png', 'Character/villain2.png']
text = ['Ternyata benar dia ada di sini.', 'Untung saja dia belum sempat masuk. Ayo tangkap dia!', 'Tidakkk!!!', 'Game Over']
choice = ['', '']
nextVal = [0, 0]
dialogueTree.insert(32,text,choice,nextVal, asset)

#Binary Tree 50
asset = ['Background/rumah kosong.jpg', 'Character/prince2.png', 'Character/villain1.png', 'Character/villain2.png']
text = ['Ayo cari pangeran itu, dia pasti tidak jauh dari sini.', 'Kita sudah mencari semalaman dan tidak menemukannya.', 'Apa mungkin dia sudah berhasil kembali ke kerajaannya?', 'Tidak mungkin! Cepat cari lagi, kita harus menemukannya.', 'Itu adalah orang-orang yang menculikku! Aku harus kabur dari sini.', 'Heap dimana root-nya memiliki value paling kecil adalah?']
choice = ['Min', 'Max']
nextVal = [42,  58]
dialogueTree.insert(50,text,choice,nextVal, asset)

#Binary Tree 58
asset = ['Background/black panther.jpg','Character/prince2.png']
text = ['Linked List yang semua pointernya menunjuk pada', 'sebuah node atau tidak ada yang bernilai NULL adalah?']
choice = ['Circular', 'Double']
nextVal = [54, 62]
dialogueTree.insert(58,text,choice,nextVal, asset)

#Binary Tree 54
asset = ['Character/prince2.png', 'Others/tanaman obat.png']
text = ['Wah, aku mendapatkan digit kedua..tetapi aku terluka cukup parah,', 'aku harus segera mengobatinya.', 'tanaman obat yang mana ya yang benar?', 'Proses mengeluarkan sebuah elemen', 'dari queue disebut dengan?']
choice = ['dequeue', 'enqueue']
nextVal = [52, 56]
dialogueTree.insert(54,text,choice,nextVal, asset)

#Binary Tree 42
asset = ['Background/black panther.jpg','Character/prince2.png']
text = ['Jenis linked list yang memiliki 1 pointer adalah?']
choice = ['Single', 'Linear']
nextVal = [38,  46]
dialogueTree.insert(42,text,choice,nextVal, asset)

#Binary Tree 38
asset = ['Background/kerajaan di kejauhan.jpg', 'Character/prince2.png']
text = ['Akhirnya aku mendapatkan digit kedua.','Sekarang aku hanya perlu mencari jalan ke kerajaanku.']
choice = ['', '']
nextVal = [36,  40]
dialogueTree.insert(38,text,choice,nextVal, asset)

#Binary Tree 36
asset = ['Background/castle.jpg', 'Character/prince2.png']
text = ['Akhirnya aku bisa pulang!','Aku akan segera menginterogasi pengawal ku yang tidak becus menjagaku ini', 'Welcome Home']
choice = ['', '']
nextVal = [0, 0]
dialogueTree.insert(36,text,choice,nextVal, asset)

#Binary Tree 40
asset = ['Background/castle.jpg', 'Character/prince2.png', 'Character/villain1.png', 'Character/villain2.png']
text = ['Ternyata benar dia ada di sini.', 'Untung saja dia belum sempat masuk. Ayo tangkap dia!', 'Tidakkk!!!', 'Game Over']
choice = ['', '']
nextVal = [0, 0]
dialogueTree.insert(40,text,choice,nextVal, asset)

#Binary Tree 46
asset = ['Background/kerajaan di kejauhan.jpg', 'Character/prince2.png', 'Character/ds-icon.png']
text = ['Aku mendapatkan digit kedua dalam perjalanan ini!', 'Selamat, kamu sudah berhasil mengumpulkan semua digit yang diperlukan!', 'Ayo kita berjalan lagi, jalan ini sudah dekat dengan kerajaanku!']
choice = ['', '']
nextVal = [44,48]
dialogueTree.insert(46,text,choice,nextVal, asset)

#Binary Tree 44
asset = ['Background/castle.jpg', 'Character/prince2.png']
text = ['Akhirnya aku bisa pulang! Aku akan segera menginterogasi pengawal ku yang tidak becus menjagaku ini', 'Welcome Home']
choice = ['', '']
nextVal = [0, 0]
dialogueTree.insert(44,text,choice,nextVal, asset)

#Binary Tree 48
asset = ['Background/castle.jpg','Character/prince2.png', 'Character/villain1.png', 'Character/villain2.png']
text = ['Ternyata benar dia ada di sini.', 'Untung saja dia belum sempat masuk. Ayo tangkap dia!', 'Tidakkk!!!', 'Game Over']
choice = ['', '']
nextVal = [0, 0]
dialogueTree.insert(48,text,choice,nextVal, asset)

#Binary Tree 52
asset = ['Background/siang-sore.jpg','Character/prince2.png', 'Others/tanaman obat.png']
text = ['Hebat sekali tanaman obat ini! Sekarang aku harus mencari kerajaanku.']
choice = ['dequeue', 'enqueue']
nextVal = [51, 53]
dialogueTree.insert(52,text,choice,nextVal, asset)

#Binary Tree 53
asset = ['Background/sungai.jpg', 'Character/prince2.png']
text = ['Ah kenapa membuat api unggun begitu sulit', 'Mati kedinginan']
choice = ['', '']
nextVal = [0, 0]
dialogueTree.insert(53,text,choice,nextVal, asset)

#Binary Tree 51
asset = ['Background/castle.jpg','Character/prince2.png']
text = ['Akhirnya aku bisa pulang! Aku akan segera menginterogasi pengawal ku yang tidak becus menjagaku ini', 'Welcome Home']
choice = ['', '']
nextVal = [0, 0]
dialogueTree.insert(51,text,choice,nextVal, asset)

#Binary Tree 53
asset = ['Background/castle.jpg','Character/prince2.png','Character/villain1.png','Character/villain2.png']
text = ['Ternyata benar dia ada di sini.', 'Untung saja dia belum sempat masuk. Ayo tangkap dia!', 'Tidakkk!!!', 'Game Over']
choice = ['', '']
nextVal = [0, 0]
dialogueTree.insert(53,text,choice,nextVal, asset)

#Binary Tree 56
asset = ['Character/prince2.png']
text = ['Oh tidak, apakah aku keracunan?', 'Apakah hidupku akan berakhir disini', 'Game Over']
choice = ['', '']
nextVal = [0, 0]
dialogueTree.insert(56,text,choice,nextVal, asset)


#Binary Tree 62
asset = ['Character/prince2.png']
text = [' Salah satu metode untuk mengatasi collision dengan menggunakan pointer']
choice = ['LISCH', 'ELICH']
nextVal = [60, 64]
dialogueTree.insert(62,text,choice,nextVal, asset)

#Binary Tree 60
asset = ['Character/prince2.png','Others/tanaman obat.png']
text = ['Hebat sekali tanaman obat ini! Sekarang aku harus mencari kerajaanku.']
choice = ['', '']
nextVal = [59, 61]
dialogueTree.insert(60,text,choice,nextVal, asset)

#Binary Tree 59
asset = ['Background/castle.jpg','Character/prince2.png']
text = ['Akhirnya aku bisa pulang!','Aku akan segera menginterogasi pengawal ku yang tidak becus menjagaku ini', 'Welcome Home']
choice = ['', '']
nextVal = [0, 0]
dialogueTree.insert(59,text,choice,nextVal, asset)

#Binary Tree 61
asset = ['Background/castle.jpg','Character/prince2.png','Character/villain1.png','Character/villain2.png']
text = ['Ternyata benar dia ada di sini.', 'Untung saja dia belum sempat masuk. Ayo tangkap dia!', 'Tidakkk!!!', 'Game Over']
choice = ['', '']
nextVal = [0, 0]
dialogueTree.insert(61,text,choice,nextVal, asset)

#Binary Tree 64
asset = ['Character/prince2.png']
text = ['Oh tidak, apakah aku keracunan?', 'Apakah hidupku akan berakhir disini', 'Game Over']
choice = ['', '']
nextVal = [0, 0]
dialogueTree.insert(64,text,choice,nextVal, asset)

#Binary Tree 98
asset = ['Background/hutan siang.jpg','Character/prince2.png', 'Character/ds-icon.png']
text = ['Lihat!! Aku berhasil mendapatkan 1 digit.', 'Selamat! kamu hanya perlu mencari 1 digit lagi.', 'Aku tidak sabar untuk segera pulang', 'mari kita lanjutkan perjalanan ini.', 'Integer merupakan tipe data apa?']
choice = ['Tunggal', 'Majemuk']
nextVal = [82, 114]
dialogueTree.insert(98,text,choice,nextVal, asset)

#Binary Tree 82
asset = ['Background/rumah kosong.jpg', 'Character/prince2.png']
text = ['Rumah ini sepertinya tidak berpenghuni,', 'aku akan beristirahat di sini malam ini.', 'Penghubung data-data pada graph disebut dengan?']
choice = ['Edge', 'Node']
nextVal = [74, 90]
dialogueTree.insert(82,text,choice,nextVal, asset)

#Binary Tree 74
asset = ['Background/jurang sungai.jpg', 'Character/prince2.png']
text = ['Apakah binary tree boleh memiliki cabang lebih dari 2?']
choice = ['Ya', 'Tidak']
nextVal = [70, 78]
dialogueTree.insert(74,text,choice,nextVal, asset)

#Binary Tree 70
asset = ['Background/jurang sungai.jpg', 'Character/prince2.png']
text = ['Loh kok aku tidak mendapatkan digit lagi? Bagaimana aku bisa pulang?', 'Kamu harus mencari jalan lain selain lewat gerbang', 'Hah? Bagaimana caranya?', 'Sudah liat saja nanti, kita temukan dulu kerajaanmu', '   Fungsi untuk menambahkan sebuah elemen ke dalam stack disebut dengan?']
choice = ['Push', 'Pop']
nextVal = [68,72]
dialogueTree.insert(70,text,choice,nextVal, asset)

#Binary Tree 68
asset = ['Background/castle.jpg', 'Character/prince2.png','Others/ladder.png']
text = ['Aha! Aku akan memanjat pagar tembok kerajaanku dengan tangga ini!', 'Akhirnya aku bisa pulang! Aku akan segera menginterogasi pengawal ku yang tidak becus menjagaku ini', 'Welcome Home']
choice = ['Pop', 'Push']
nextVal = [0, 0]
dialogueTree.insert(68,text,choice,nextVal, asset)

#Binary Tree 72
asset = ['Background/castle.jpg','Character/prince2.png','Character/villain1.png','Character/villain2.png']
text = ['Ternyata benar dia ada di sini.', 'Untung saja dia belum sempat masuk. Ayo tangkap dia!', 'Tidakkk!!!', 'Game Over']
nextVal = [0, 0]
dialogueTree.insert(72,text,choice,nextVal, asset)

#Binary Tree 78
asset = ['Background/castle.jpg','Character/prince2.png','Character/villain1.png','Character/villain2.png']
text = ['Bagus sekali, aku mendapatkan digit kedua. Sekarang aku hanya perlu menemukan kerajaanku, seharusnya ada di dekat sini.', 'Kenapa tidak bisa dibuka ya?', 'Ternyata benar dia ada di sini.', 'Untung saja dia belum sempat masuk. Ayo tangkap dia!', 'Tidakkk!!!', 'Game Over'] 
choice = ['', '']
nextVal = [0, 0]
dialogueTree.insert(78,text,choice,nextVal, asset)

#Binary Tree 90
asset = ['Background/jurang sungai.jpg', 'Character/prince2.png']
text = ['Karena tidak melihat ada jembatan untuk diseberangi,', 'Pangeran memutuskan untuk menyeberang dengan cara', 'terjun ke sungai di bawah jurang', 'Setelah berenang ke tepi..', 'Jika operator berada di depan operands,','maka notasi tersebut disebut dengan?']
choice = ['Prefix', 'Postfix']
nextVal = [86, 94]
dialogueTree.insert(90,text,choice,nextVal, asset)

#Binary Tree 86
asset = ['Background/sungai.jpg', 'Character/prince2.png']
text = ['Pas sekali di situ ada kayu dan korek api!', 'Aku akan menyalakan api untuk menghangatkan tubuh.', 'Pada AVL Tree, tree dikatakan seimbang bila,' ,'selisih jumlah node kiri dan kanan tidak lebih dari?']
choice = ['1', '2']
nextVal = [84, 88]
dialogueTree.insert(86,text,choice,nextVal, asset)

#Binary Tree 84
asset = ['Background/castle.jpg','Character/prince2.png','Character/villain1.png','Character/villain2.png']
text = ['Kenapa tidak bisa dibuka ya?', 'Ternyata benar dia ada di sini.', 'Untung saja dia belum sempat masuk. Ayo tangkap dia!', 'Tidakkk!!!', 'Game Over']
choice = ['', '']
nextVal = [0, 0]
dialogueTree.insert(84,text,choice,nextVal, asset)

#Binary Tree 88
asset = ['Background/castle.jpg', 'Character/prince2.png']
text = ['Waduh, gawat! Aku hanya punya 1 digit, tidak bisa membuka gerbang ini!', 'Kamu harus mencari jalan lain selain lewat gerbang', 'Hah? Bagaimana caranya?', 'Di antara array dan linked list,', 'manakah yang lebih fleksibel?']
choice = ['Linked List', 'Array']
nextVal = [87, 89]
dialogueTree.insert(88,text,choice,nextVal, asset)

#Binary Tree 87
asset = ['Background/castle.jpg', 'Character/prince2.png', 'Others/ladder.png']
text = ['Aha! Aku akan memanjat pagar tembok kerajaanku dengan tangga ini!', 'Akhirnya aku bisa pulang! Aku akan segera menginterogasi pengawal ku yang tidak becus menjagaku ini', 'Welcome Home']
choice = ['', '']
nextVal = [0, 0]
dialogueTree.insert(87,text,choice,nextVal, asset)

#Binary Tree 89
asset = ['Background/castle.jpg','Character/prince2.png','Character/villain1.png','Character/villain2.png']
text = ['Ternyata benar dia ada di sini.', 'Untung saja dia belum sempat masuk. Ayo tangkap dia!', 'Tidakkk!!!', 'Game Over']
choice = ['', '']
nextVal = [0, 0]
dialogueTree.insert(89,text,choice,nextVal, asset)

#Binary Tree 94
asset = ['Background/sungai.jpg', 'Character/prince2.png']
text = ['']
choice = ['', '']
nextVal = [0, 0]
dialogueTree.insert(94,text,choice,nextVal, asset)

#Binary Tree 114
asset = ['Background/hutan malam.jpg','Character/prince2.png']
text = ['Malang sekali nasibku!' , 'Tidak menemukan makanan,','kini mau beristirahat pun tidak ada tempat berteduh.', '(menghela nafas) hm..aku akan tidur di bawah pohon saja malam ini.', 'Gawat mereka menemukan keberadaan ku. Aku harus segera lari.', 'Apakah binary tree boleh memiliki cabang lebih dari 2?']
choice = ['Tidak', 'Ya']
nextVal = [106, 122]
dialogueTree.insert(114,text,choice,nextVal, asset)

#Binary Tree 106
asset = ['Background/jurang sungai.jpg','Character/prince2.png']
text = ['Hmm, sepertinya aku harus terjun ke sana', 'Jika operator berada di depan operands,' 'maka notasi tersebut disebut dengan?']
choice = ['Prefix', 'Postfix']
nextVal = [102, 110]
dialogueTree.insert(106,text,choice,nextVal, asset)

#Binary Tree 102
asset = ['Background/sungai.jpg','Character/prince2.png']
text = ['Astaga betapa beruntungnya aku menemukan kayu dan korek api ditempat ini,', 'aku harus segera menghangatkan diri.', 'Pada AVL Tree, tree dikatakan seimbang bila,', 'selisih jumlah node kiri dan kanan tidak lebih dari?']
choice = ['1', '2']
nextVal = [100,104]
dialogueTree.insert(102,text,choice,nextVal, asset)

#Binary Tree 110
asset = ['Background/sungai.jpg','Character/prince2.png']
text = ['Oh Tuhan, jika ini kehendakmu', 'aku akan berserah mati kedinginan di tempat ini.', 'Game Over']
choice = ['', '']
nextVal = [0, 0]
dialogueTree.insert(110,text,choice,nextVal, asset)

#Binary Tree 100
asset = ['Background/castle.jpg','Character/prince2.png','Character/villain1.png','Character/villain2.png']
text = ['Kenapa tidak bisa dibuka ya?', 'Ternyata benar dia ada di sini.', 'Untung saja dia belum sempat masuk. Ayo tangkap dia!', 'Tidakkk!!!', 'Game Over']
choice = ['', '']
nextVal = [0, 0]
dialogueTree.insert(100,text,choice,nextVal, asset)

#Binary Tree 104
asset = ['Background/castle.jpg','Character/prince2.png']
text = ['Waduh, gawat! Aku hanya punya 1 digit, tidak bisa membuka gerbang ini!', 'Kamu harus mencari jalan lain selain lewat gerbang', 'Hah? Bagaimana caranya?', 'Di antara array dan linked list,', 'manakah yang lebih fleksibel?']
choice = ['Linked List', 'Array']
nextVal = [57,59]
dialogueTree.insert(104,text,choice,nextVal, asset)

#Binary Tree 103
asset = ['Background/castle.jpg','Character/prince2.png', 'Others/ladder.png']
text = ['Aha! Aku akan memanjat pagar tembok kerajaanku dengan tangga ini!', 'Akhirnya aku bisa pulang! Aku akan segera menginterogasi pengawal ku yang tidak becus menjagaku ini']
choice = ['', '']
nextVal = [0, 0]
dialogueTree.insert(103,text,choice,nextVal, asset)

#Binary Tree 105
asset = ['Background/castle.jpg','Character/prince2.png','Character/villain1.png','Character/villain2.png']
text = ['Ternyata benar dia ada di sini.', 'Untung saja dia belum sempat masuk. Ayo tangkap dia!', 'Tidakkk!!!', 'Game Over']
choice = ['', '']
nextVal = [0, 0]
dialogueTree.insert(105,text,choice,nextVal, asset)

#Binary Tree 122
asset = ['Background/jurang sungai.jpg', 'Character/prince2.png','Character/villain1.png','Character/villain2.png']
text = ['Lepaskan aku. Tidak ada untungnya kalian menangkap aku.', 'Seperti katamu, karena kamu tidak untung nya,', 'maka akan aku buat kamu menghilang saja dari dunia ini.', 'Game Over']
choice = ['Kiri', 'Kanan']
nextVal = [0, 126]
dialogueTree.insert(122,text,choice,nextVal, asset)

#Binary Tree 194
asset = ['Background/hutan siang.jpg', 'Character/prince2.png']
text = ['Dimana aku berada? Kenapa hutannya semakin gelap padahal masih siang?', 'Oh, pertanyaan apa ini', 'Struktur data yang menyimpan elemen dengan konsep fifo?']
choice = ['Stack', 'Queue']
nextVal = [162,  226]
dialogueTree.insert(194,text,choice,nextVal, asset)

#Binary Tree 162
asset = ['Background/hutan siang.jpg', 'Character/prince2.png', 'Character/ds-icon.png']
text = ['Apa ini?', 'Halo Halo Loha, aku DS, yang akan menemani mu di perjalanan ini.', 'Kamu kenapa bisa ada disini?', 'Aku diciptakan untuk membantu orang” yang tersesat di hutan ini.', 'Baiklah.']
choice = ['Queue', 'Stack']
nextVal = [34,  98]
dialogueTree.insert(162,text,choice,nextVal, asset)

#Binary Tree 226
asset = ['Background/hutan pagi.jpg', 'Character/prince2.png']
text = ['Gawat ada orang yang mau menculikku di sana, ','sebelum mereka sadar akan keberadaan ku aku harus segera bersembunyi.', 'String merupakan tipe data apa?']
choice = ['Majemuk', 'Tunggal']
nextVal = [210,  242]
dialogueTree.insert(226,text,choice,nextVal, asset)

#Binary Tree 210
asset = ['Background/hutan siang.jpg', 'Character/prince2.png', 'Character/ds-icon.png']
text = ['Apa ini?', 'Halo Halo Loha, aku DS, yang akan menemani mu di perjalanan ini.', 'Kamu kenapa bisa ada disini?', 'Aku diciptakan untuk membantu orang” yang tersesat di hutan ini.', 'Baiklah.']
choice = ['Queue','Stack']
nextVal = [34, 98]
dialogueTree.insert(210,text,choice,nextVal, asset)

#Binary Tree 242
asset = ['Background/semak-semak.jpg', 'Character/prince2.png','Character/villain1.png']
text = ['Lepaskan aku, jangan ikat aku di pohon, pohon ini banyak semut nya.', 'Sudah diam saja, jangan banyak bicara. Awas saja kalau kau kabur lagi.', ' Array merupakan struktur data apa?']
choice = ['Sederhana', 'Majemuk']
nextVal = [234,  250]
dialogueTree.insert(242,text,choice,nextVal, asset)

#Binary Tree 234
asset = ['Background/semak-semak.jpg', 'Character/prince2.png']
text = ['Hore! Aku bisa membebaskan diri', 'Sekarang aku harus kemana', 'You are lost in the woods']
choice = ['', '']
nextVal = [0, 0]
dialogueTree.insert(234,text,choice,nextVal, asset)

#Binary Tree 250
asset = ['Background/semak-semak.jpg', 'Character/prince2.png', 'Character/villain1.png']
text = ['Hoi, sudah kubilang jangan bermain-main dengan diriku,', 'sekarang rasakan akibatnya.', 'Game Over']
choice = ['', '']
nextVal = [0, 0]
dialogueTree.insert(250,text,choice,nextVal, asset)

#Binary Tree 126 (Tambahan saat demo)
asset = ['Background/semak-semak.jpg', 'Character/prince2.png', 'Character/villain1.png']
text = ['Haloooo']
choice = ['', '']
nextVal = [0, 0]
dialogueTree.insert(126,text,choice,nextVal, asset)

# dialogueTree.printIn()
dialogueTree.print_tree()

