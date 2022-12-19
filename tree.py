class Node:
    def __init__(self, value, text: list, choice: list, nextVal : list, asset : list):
        self.data = value
        self.gameData = []
        self.gameData.append(text)
        self.gameData.append(choice)
        self.gameData.append(nextVal)
        self.gameData.append(asset)
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
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
asset = ['persimpangan jalan.avif']
text = ['Wah ada dua jalan aku harus pilih yang mana ya?']
choice = ['Jalan kiri', 'Jalan kanan']
nextVal = [6,  64]
dialogueTree.insert(7,text,choice,nextVal, asset)

#Binary Tree 6
asset = ['hutan siang.jpg', 'prince2.png', 'ds scratch 2.png']
text = ['Apa ini?', 'Halo Halo Loha, aku DS, yang akan menemani mu di perjalanan ini.', 'Kamu kenapa bisa ada disini?', 'Aku diciptakan untuk membantu orang” yang tersesat di hutan ini.', 'Baiklah.']
choice = ['Queue', 'Stack']
nextVal = [5,  43]
dialogueTree.insert(6,text,choice,nextVal, asset)

#Binary Tree 5
asset = ['hutan siang.jpg', 'prince2.png', 'ds scratch 2.png']
text = ['Lihat… aku berhasil mendapatkan 1 digit.', 'Selamat, kamu hanya perlu mencari 1 digit lagi.', 'Aku tidak sabar untuk segera pulang, mari kita lanjutkan perjalanan ini.']
choice = ['Queue', 'Stack']
nextVal = [4,  31]
dialogueTree.insert(5,text,choice,nextVal, asset)

#Binary Tree 4
asset = ['dalam rumah kosong.png', 'prince2.png']
text = ['Ayo cari pangeran itu, dia pasti tidak jauh dari sini.', 'Kita sudah mencari semalaman dan tidak menemukannya. Apa mungkin dia sudah berhasil kembali ke kerajaannya?', 'Tidak mungkin! Cepat cari lagi, kita harus menemukannya.', 'Itu adalah orang-orang yang menculikku! Aku harus kabur dari sini.', 'Aku harus menyeberangi sungai ini. Bagaimana caraku untuk menyeberang?']
choice = ['Root', 'Leaf']
nextVal = [3,  14]
dialogueTree.insert(4,text,choice,nextVal, asset)

#Binary Tree 3
asset = ['sungai.jpg', 'row boat.png']
text = []
choice = ['Undirected', 'Directed']
nextVal = [2,  10]
dialogueTree.insert(3,text,choice,nextVal, asset)

#Binary Tree 2
asset = ['prince2.png', 'ds scratch 2.png']
text = ['Aku mendapatkan digit kedua dalam perjalanan ini!', 'Selamat, kamu sudah berhasil mengumpulkan semua digit yang diperlukan!', 'Ayo kita berjalan lagi, jalan ini sudah dekat dengan kerajaanku!']
choice = []
nextVal = [1,8]
dialogueTree.insert(2,text,choice,nextVal, asset)

#Binary Tree 1
asset = ['prince2.png']
text = ['Akhirnya aku bisa pulang! Aku akan segera menginterogasi pengawal ku yang tidak becus menjagaku ini' ]
choice = []
nextVal = []
dialogueTree.insert(1,text,choice,nextVal, asset)

#Binary Tree 8
asset = ['prince2.png']
text = ['Ternyata benar dia ada di sini.', 'Untung saja dia belum sempat masuk. Ayo tangkap dia!', 'Tidakkk!!!']
choice = []
nextVal = []
dialogueTree.insert(8,text,choice,nextVal, asset)

#Binary Tree 10
asset = ['prince2.png', 'ds scratch 2.png']
text = ['Aku mendapatkan digit kedua dalam perjalanan ini!', 'Selamat, kamu sudah berhasil mengumpulkan semua digit yang diperlukan!', 'Ayo kita berjalan lagi, jalan ini sudah dekat dengan kerajaanku!']
choice = []
nextVal = [9,11]
dialogueTree.insert(10,text,choice,nextVal, asset)

#Binary Tree 9
asset = ['prince2.png']
text = ['Akhirnya aku bisa pulang! Aku akan segera menginterogasi pengawal ku yang tidak becus menjagaku ini' ]
choice = []
nextVal = []
dialogueTree.insert(9,text,choice,nextVal, asset)

#Binary Tree 11
asset = ['prince2.png']
text = ['Ternyata benar dia ada di sini.', 'Untung saja dia belum sempat masuk. Ayo tangkap dia!', 'Tidakkk!!!']
choice = []
nextVal = []
dialogueTree.insert(11,text,choice,nextVal, asset)

#Binary Tree 14
asset = ['sungai.png', 'prince2.png']
text = ['Air sungai ini sangat dingin! Tetapi sepertinya aku tidak punya pilihan lain selain berenang.']
choice = ['Majemuk', 'Sederhana']
nextVal = [13,  17]
dialogueTree.insert(14,text,choice,nextVal, asset)

#Binary Tree 13
asset = ['sungai.png', 'prince2.png']
text = ['Tidak sia-sia aku berenang ke sini, ternyata aku mendapatkan digit terakhir yang kuperlukan! Tetapi aku sangat kedinginan.', 'Ah, aku akan menghangatkan diri sebentar dengan menyalakan api unggun.', ]
choice = ['folding', 'carry']
nextVal = [12,  15]
dialogueTree.insert(13,text,choice,nextVal, asset)

#Binary Tree 12
asset = ['sungai.png', 'prince2.png']
text = ['Akhirnya aku bisa pulang! Aku akan segera menginterogasi pengawal ku yang tidak becus menjagaku ini']
choice = []
nextVal = [9,11]
dialogueTree.insert(12,text,choice,nextVal, asset)

#Binary Tree 15
asset = ['sungai.png', 'prince2.png']
text = ['Ah kenapa membuat api unggun begitu sulit']
choice = []
nextVal = []
dialogueTree.insert(15,text,choice,nextVal, asset)

#Binary Tree 17
asset = ['sungai.png', 'prince2.png']
text = ['Tidak sia-sia aku berenang ke sini, ternyata aku mendapatkan digit terakhir yang kuperlukan! Tetapi aku sangat kedinginan..', 'Ah, aku akan menghangatkan diri sebentar dengan menyalakan api unggun.']
choice = ['Inorder', 'Postorder']
nextVal = [16,18]
dialogueTree.insert(17,text,choice,nextVal, asset)

#Binary Tree 16
asset = ['sungai.png', 'prince2.png']
text = ['Akhirnya aku bisa pulang! Aku akan segera menginterogasi pengawal ku yang tidak becus menjagaku ini']
choice = []
nextVal = []
dialogueTree.insert(16,text,choice,nextVal, asset)

#Binary Tree 18
asset = ['sungai.png', 'prince2.png']
text = ['Ah kenapa membuat api unggun begitu sulit', '']
choice = []
nextVal = []
dialogueTree.insert(18,text,choice,nextVal, asset)

#Binary Tree 31
asset = ['rumah kosong.jpg', 'prince2.png', 'hutan pagi.jpg', 'blackpanther.jpg']
text = ['Ayo cari pangeran itu, dia pasti tidak jauh dari sini.', 'Kita sudah mencari semalaman dan tidak menemukannya. Apa mungkin dia sudah berhasil kembali ke kerajaannya?', 'Tidak mungkin! Cepat cari lagi, kita harus menemukannya.', 'Itu adalah orang-orang yang menculikku! Aku harus kabur dari sini.', 'Aku harus menyeberangi sungai ini. Bagaimana caraku untuk menyeberang?']
choice = ['Min', 'Max']
nextVal = [21,  30]
dialogueTree.insert(31,text,choice,nextVal, asset)

#Binary Tree 21
asset = ['prince2.png', 'hutan pagi.jpg', 'blackpanther.jpg']
text = []
choice = ['Single', 'Linear']
nextVal = [20,  25]
dialogueTree.insert(21,text,choice,nextVal, asset)

#Binary Tree 20
asset = ['prince2.png']
text = ['Akhirnya aku mendapatkan digit kedua. Sekarang aku hanya perlu mencari jalan ke kerajaanku.']
choice = []
nextVal = [19,  23]
dialogueTree.insert(20,text,choice,nextVal, asset)

#Binary Tree 19
asset = ['prince2.png']
text = ['Akhirnya aku bisa pulang! Aku akan segera menginterogasi pengawal ku yang tidak becus menjagaku ini' ]
choice = []
nextVal = []
dialogueTree.insert(19,text,choice,nextVal, asset)

#Binary Tree 23
asset = ['prince2.png']
text = ['Ternyata benar dia ada di sini.', 'Untung saja dia belum sempat masuk. Ayo tangkap dia!', 'Tidakkk!!!']
choice = []
nextVal = []
dialogueTree.insert(23,text,choice,nextVal, asset)

#Binary Tree 25
asset = ['prince2.png', 'ds scratch 2.png']
text = ['Aku mendapatkan digit kedua dalam perjalanan ini!', 'Selamat, kamu sudah berhasil mengumpulkan semua digit yang diperlukan!', 'Ayo kita berjalan lagi, jalan ini sudah dekat dengan kerajaanku!']
choice = []
nextVal = [24,26]
dialogueTree.insert(25,text,choice,nextVal, asset)

#Binary Tree 24
asset = ['prince2.png']
text = ['Akhirnya aku bisa pulang! Aku akan segera menginterogasi pengawal ku yang tidak becus menjagaku ini']
choice = []
nextVal = []
dialogueTree.insert(24,text,choice,nextVal, asset)

#Binary Tree 26
asset = ['prince2.png']
text = ['Ternyata benar dia ada di sini.', 'Untung saja dia belum sempat masuk. Ayo tangkap dia!', 'Tidakkk!!!']
choice = []
nextVal = []
dialogueTree.insert(26,text,choice,nextVal, asset)

#Binary Tree 30
asset = ['prince2.png']
text = []
choice = ['Circular', 'Double']
nextVal = [29, 36]
dialogueTree.insert(30,text,choice,nextVal, asset)

#Binary Tree 29
asset = ['prince2.png']
text = ['Wah, aku mendapatkan digit kedua..tetapi aku terluka cukup parah, aku harus segera mengobatinya.', 'Tanaman obat yang mana ya yang benar?']
choice = ['dequeue', 'enqueue']
nextVal = [27, 33]
dialogueTree.insert(29,text,choice,nextVal, asset)

#Binary Tree 28
asset = ['prince2.png']
text = ['Hebat sekali tanaman obat ini! Sekarang aku harus mencari kerajaanku.']
choice = ['dequeue', 'enqueue']
nextVal = [27, 32]
dialogueTree.insert(28,text,choice,nextVal, asset)

#Binary Tree 27
asset = ['prince2.png']
text = ['Akhirnya aku bisa pulang! Aku akan segera menginterogasi pengawal ku yang tidak becus menjagaku ini' ]
choice = []
nextVal = []
dialogueTree.insert(27,text,choice,nextVal, asset)

#Binary Tree 32
asset = ['prince2.png']
text = ['Ternyata benar dia ada di sini.', 'Untung saja dia belum sempat masuk. Ayo tangkap dia!', 'Tidakkk!!!']
choice = []
nextVal = []
dialogueTree.insert(32,text,choice,nextVal, asset)

#Binary Tree 33
asset = ['prince2.png']
text = []
choice = []
nextVal = []
dialogueTree.insert(33,text,choice,nextVal, asset)


#Binary Tree 36
asset = ['prince2.png']
text = []
choice = ['LISCH', 'ELICH']
nextVal = [35, 38]
dialogueTree.insert(36,text,choice,nextVal, asset)

#Binary Tree 35
asset = ['prince2.png']
text = ['Hebat sekali tanaman obat ini! Sekarang aku harus mencari kerajaanku.']
choice = []
nextVal = [34, 37]
dialogueTree.insert(35,text,choice,nextVal, asset)

#Binary Tree 34
asset = ['prince2.png']
text = ['Akhirnya aku bisa pulang! Aku akan segera menginterogasi pengawal ku yang tidak becus menjagaku ini']
choice = []
nextVal = []
dialogueTree.insert(34,text,choice,nextVal, asset)

#Binary Tree 37
asset = ['prince2.png']
text = ['Ternyata benar dia ada di sini.', 'Untung saja dia belum sempat masuk. Ayo tangkap dia!', 'Tidakkk!!!']
choice = []
nextVal = []
dialogueTree.insert(37,text,choice,nextVal, asset)

#Binary Tree 38
asset = ['prince2.png']
text = []
choice = []
nextVal = []
dialogueTree.insert(38,text,choice,nextVal, asset)

#Binary Tree 43
asset = ['prince2.png', 'ds scratch 2.png']
text = ['Lihat… aku berhasil mendapatkan 1 digit.', 'Selamat, kamu hanya perlu mencari 1 digit lagi.', 'Aku tidak sabar untuk segera pulang, mari kita lanjutkan perjalanan ini.']
choice = ['Tunggal', 'Majemuk']
nextVal = [42, 56]
dialogueTree.insert(43,text,choice,nextVal, asset)

#Binary Tree 42
asset = ['hutan malam.png', 'prince2.png']
text = ['Rumah ini sepertinya tidak berpenghuni, aku akan beristirahat di sini malam ini.']
choice = ['Edge', 'Node']
nextVal = [41, 48]
dialogueTree.insert(42,text,choice,nextVal, asset)

#Binary Tree 41
asset = ['hutan malam.png', 'prince2.png']
text = []
choice = ['Ya', 'Tidak']
nextVal = [40, 45]
dialogueTree.insert(41,text,choice,nextVal, asset)

#Binary Tree 40
asset = ['hutan malam.png', 'prince2.png']
text = ['Loh kok aku tidak mendapatkan digit lagi? Bagaimana aku bisa pulang?', 'Kamu harus mencari jalan lain selain lewat gerbang', 'Hah? Bagaimana caranya?', 'Sudah liat saja nanti, kita temukan dulu kerajaanmu']
choice = ['Push', 'Pop']
nextVal = [39,44]
dialogueTree.insert(40,text,choice,nextVal, asset)

#Binary Tree 39
asset = ['hutan malam.png', 'prince2.png']
text = ['Aha! Aku akan memanjat pagar tembok kerajaanku dengan tangga ini!', 'Akhirnya aku bisa pulang! Aku akan segera menginterogasi pengawal ku yang tidak becus menjagaku ini']
choice = ['Pop', 'Push']
nextVal = []
dialogueTree.insert(39,text,choice,nextVal, asset)

#Binary Tree 44
asset = ['hutan malam.png', 'prince2.png']
text = ['Ternyata benar dia ada di sini.', 'Untung saja dia belum sempat masuk. Ayo tangkap dia!', 'Tidakkk!!!']
nextVal = []
dialogueTree.insert(44,text,choice,nextVal, asset)

#Binary Tree 45
asset = ['hutan malam.png', 'prince2.png']
text = ['Bagus sekali, aku mendapatkan digit kedua. Sekarang aku hanya perlu menemukan kerajaanku, seharusnya ada di dekat sini.', 'Kenapa tidak bisa dibuka ya?', 'Ternyata benar dia ada di sini.', 'Untung saja dia belum sempat masuk. Ayo tangkap dia!', 'Tidakkk!!!'] 
choice = []
nextVal = []
dialogueTree.insert(45,text,choice,nextVal, asset)

#Binary Tree 48
asset = ['hutan malam.png', 'prince2.png']
text = ['Rumah ini sepertinya tidak berpenghuni, aku akan beristirahat di sini malam ini.']
choice = ['Prefix', 'Postfix']
nextVal = [47, 52]
dialogueTree.insert(48,text,choice,nextVal, asset)

#Binary Tree 47
asset = ['hutan malam.png', 'prince2.png']
text = ['Pas sekali di situ ada kayu dan korek api! Aku akan menyalakan api untuk menghangatkan tubuh.']
choice = ['1', '2']
nextVal = [46, 50]
dialogueTree.insert(47,text,choice,nextVal, asset)

#Binary Tree 46
asset = ['hutan malam.png', 'prince2.png']
text = ['Kenapa tidak bisa dibuka ya?', 'Ternyata benar dia ada di sini.', 'Untung saja dia belum sempat masuk. Ayo tangkap dia!', 'Tidakkk!!!']
choice = []
nextVal = []
dialogueTree.insert(46,text,choice,nextVal, asset)

#Binary Tree 50
asset = ['hutan malam.png', 'prince2.png']
text = ['Waduh, gawat! Aku hanya punya 1 digit, tidak bisa membuka gerbang ini!', 'Kamu harus mencari jalan lain selain lewat gerbang', 'Hah? Bagaimana caranya?']
choice = ['Linked List', 'Array']
nextVal = [49, 51]
dialogueTree.insert(50,text,choice,nextVal, asset)

#Binary Tree 49
asset = ['hutan malam.png', 'prince2.png']
text = ['Aha! Aku akan memanjat pagar tembok kerajaanku dengan tangga ini!', 'Akhirnya aku bisa pulang! Aku akan segera menginterogasi pengawal ku yang tidak becus menjagaku ini']
choice = []
nextVal = []
dialogueTree.insert(49,text,choice,nextVal, asset)

#Binary Tree 51
asset = ['hutan malam.png', 'prince2.png']
text = ['Ternyata benar dia ada di sini.', 'Untung saja dia belum sempat masuk. Ayo tangkap dia!', 'Tidakkk!!!']
choice = []
nextVal = []
dialogueTree.insert(51,text,choice,nextVal, asset)

#Binary Tree 52
asset = ['sungai.jpg', 'prince2.png']
text = []
choice = []
nextVal = []
dialogueTree.insert(52,text,choice,nextVal, asset)

#Binary Tree 56
asset = ['prince2.png']
text = ['Malang sekali nasibku! Tidak menemukan makanan, kini mau beristirahat pun tidak ada tempat berteduh.', '(menghela nafas) hm..aku akan tidur di bawah pohon saja malam ini.', 'Gawat mereka menemukan keberadaan ku. Aku harus segera lari.']
choice = ['Tidak', 'Ya']
nextVal = [55, 61]
dialogueTree.insert(56,text,choice,nextVal, asset)

#Binary Tree 55
asset = ['prince2.png', 'sungai.png']
text = []
choice = ['Prefix', 'Postfix']
nextVal = [54, 60]
dialogueTree.insert(55,text,choice,nextVal, asset)

#Binary Tree 54
asset = ['prince2.png', 'sungai.png']
text = ['Astaga betapa beruntungnya aku menemukan kayu dan korek api ditempat ini, aku harus segera menghangatkan diri.']
choice = ['1', '2']
nextVal = [53,58]
dialogueTree.insert(54,text,choice,nextVal, asset)

#Binary Tree 60
asset = ['hutan sore.png', 'prince2.png', 'sungai.png']
text = ['Oh Tuhan, jika ini kehendakmu aku akan berserah mati kedinginan di tempat ini.']
choice = []
nextVal = []
dialogueTree.insert(60,text,choice,nextVal, asset)

#Binary Tree 53
asset = ['prince2.png', 'sungai.png']
text = ['Kenapa tidak bisa dibuka ya?', 'Ternyata benar dia ada di sini.', 'Untung saja dia belum sempat masuk. Ayo tangkap dia!', 'Tidakkk!!!']
choice = []
nextVal = []
dialogueTree.insert(53,text,choice,nextVal, asset)

#Binary Tree 58
asset = ['prince2.png', 'sungai.png']
text = ['Waduh, gawat! Aku hanya punya 1 digit, tidak bisa membuka gerbang ini!', 'Kamu harus mencari jalan lain selain lewat gerbang', 'Hah? Bagaimana caranya?']
choice = ['Linked List', 'Array']
nextVal = [57,59]
dialogueTree.insert(58,text,choice,nextVal, asset)

#Binary Tree 57
asset = ['prince2.png', 'sungai.png']
text = ['Aha! Aku akan memanjat pagar tembok kerajaanku dengan tangga ini!', 'Akhirnya aku bisa pulang! Aku akan segera menginterogasi pengawal ku yang tidak becus menjagaku ini']
choice = []
nextVal = []
dialogueTree.insert(57,text,choice,nextVal, asset)

#Binary Tree 59
asset = ['prince2.png', 'sungai.png']
text = ['Ternyata benar dia ada di sini.', 'Untung saja dia belum sempat masuk. Ayo tangkap dia!', 'Tidakkk!!!']
choice = []
nextVal = []
dialogueTree.insert(59,text,choice,nextVal, asset)

#Binary Tree 61
asset = ['hutan sore.png', 'prince2.png']
text = ['Lepaskan aku. Tidak ada untungnya kalian menangkap aku.', 'Seperti katamu, karena kamu tidak untung nya, maka akan aku buat kamu menghilang saja dari dunia ini.']
choice = []
nextVal = []
dialogueTree.insert(61,text,choice,nextVal, asset)

#Binary Tree 64
asset = ['hutan siang.png', 'prince2.png']
text = ['Dimana aku berada? Kenapa hutannya semakin gelap padahal masih siang?']
choice = ['Stack', 'Queue']
nextVal = [63,  65]
dialogueTree.insert(64,text,choice,nextVal, asset)

#Binary Tree 63
asset = ['hutan siang.jpg', 'prince2.png', 'ds scratch 2.png']
text = ['Apa ini?', 'Halo Halo Loha, aku DS, yang akan menemani mu di perjalanan ini.', 'Kamu kenapa bisa ada disini?', 'Aku diciptakan untuk membantu orang” yang tersesat di hutan ini.', 'Baiklah.']
choice = ['Queue', 'Stack']
nextVal = [5,  43]
dialogueTree.insert(63,text,choice,nextVal, asset)

#Binary Tree 65
asset = ['hutan siang.png', 'prince2.png']
text = ['Gawat ada orang yang mau menculikku disana, sebelum mereka sadar akan keberadaan ku aku harus segera bersembunyi.']
choice = ['Majemuk', 'Tunggal']
nextVal = [62,  67]
dialogueTree.insert(65,text,choice,nextVal, asset)

#Binary Tree 62
asset = ['semak-semak.png', 'prince2.png', 'ds scratch 2.png']
text = ['Apa ini?', 'Halo Halo Loha, aku DS, yang akan menemani mu di perjalanan ini.', 'Kamu kenapa bisa ada disini?', 'Aku diciptakan untuk membantu orang” yang tersesat di hutan ini.', 'Baiklah.']
choice = ['Queue', 'Stack']
nextVal = [5,  43]
dialogueTree.insert(62,text,choice,nextVal, asset)

#Binary Tree 67
asset = ['sema-semak.png', 'prince2.png']
text = ['Lepaskan aku, jangan ikat aku di pohon, pohon ini banyak semut nya.', 'Sudah diam saja, jangan banyak bicara. Awas saja kalau kau kabur lagi.']
choice = ['Sederhana', 'Majemuk']
nextVal = [66,  68]
dialogueTree.insert(67,text,choice,nextVal, asset)

#Binary Tree 66
asset = ['semak-semak.png', 'prince2.png']
text = ['Bagaimana kamu bisa terikat disini?', 'Siapa kamu, tolong lepaskan aku.', 'Nanti aku akan memperkenalkan diriku, sekarang aku akan membantumu melepaskan diri dari ikatan ini.', 'Halo Halo Loha, aku DS, yang akan menemani mu di perjalanan ini.', 'Kamu kenapa bisa ada disini?', 'Aku diciptakan untuk membantu orang” yang tersesat di hutan ini.', 'Baiklah.']
choice = ['Queue', 'Stack']
nextVal = [5,  43]
dialogueTree.insert(66,text,choice,nextVal, asset)


#Binary Tree 68
asset = ['semak-semak.png', 'prince2.png']
text = ['Hoi, sudah kubilang jangan bermain" dengan diriku, sekarang rasakan akibatnya.']
choice = []
nextVal = []
dialogueTree.insert(68,text,choice,nextVal, asset)


# dialogueTree.printIn()
dialogueTree.print_tree()

