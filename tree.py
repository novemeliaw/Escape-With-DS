class Node:
    def __init__(self, value, text: list, choice: list, nextVal : list) -> None:
        self.data = value
        self.gameData = []
        self.gameData.append(text)
        self.gameData.append(choice)
        self.gameData.append(nextVal)
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self) -> None:
        # Merupakan kepala paling atas
        self.root = None

    def insert(self, value, text, choice, nextValue):
        #check if root is empty
        if self.root == None :
            self.root = Node
        else :
            self.root = DFS(self.root, value)
        
        #traverse
        def DFS(curr, value):
            if curr == None:
                return Node(value)

            #insert left
            if value < curr.data :
                curr.left = DFS(curr.left, value)
            #insert right
            elif value > curr.data:
                curr.right = DFS(curr.right, value)
            return curr
        

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

dialogueTree = BinaryTree()
# Root
asset = ['persimpangan jalan.avif']
text = ['Wah ada dua jalan aku harus pilih yang mana ya?']
choice = ['Jalan kiri', 'Jalan kanan']
nextVal = [66,  194]
dialogueTree.insert(130,text,choice,nextVal)

#Binary Tree 66
asset = ['hutan siang.jpg', 'prince2.png', 'ds scratch 2.png']
text = ['Apa ini?', 'Halo Halo Loha, aku DS, yang akan menemani mu di perjalanan ini.', 'Kamu kenapa bisa ada disini?', 'Aku diciptakan untuk membantu orang” yang tersesat di hutan ini.', 'Baiklah.']
choice = ['Queue', 'Stack']
nextVal = [34,  98]
dialogueTree.insert(66,text,choice,nextVal, asset)

#Binary Tree 34
asset = ['hutan siang.jpg', 'prince2.png', 'ds scratch 2.png']
text = ['Lihat… aku berhasil mendapatkan 1 digit.', 'Selamat, kamu hanya perlu mencari 1 digit lagi.', 'Aku tidak sabar untuk segera pulang, mari kita lanjutkan perjalanan ini.']
choice = ['Queue', 'Stack']
nextVal = [18,  50]
dialogueTree.insert(34,text,choice,nextVal, asset)

#Binary Tree 18
asset = ['dalam rumah kosong.png', 'prince2.png']
text = ['Ayo cari pangeran itu, dia pasti tidak jauh dari sini.', 'Kita sudah mencari semalaman dan tidak menemukannya. Apa mungkin dia sudah berhasil kembali ke kerajaannya?', 'Tidak mungkin! Cepat cari lagi, kita harus menemukannya.', 'Itu adalah orang-orang yang menculikku! Aku harus kabur dari sini.', 'Aku harus menyeberangi sungai ini. Bagaimana caraku untuk menyeberang?']
choice = ['Root', 'Leaf']
nextVal = [10,  26]
dialogueTree.insert(18,text,choice,nextVal, asset)

#Binary Tree 10
asset = ['sungai.jpg', 'row boat.png']
text = []
choice = ['Undirected', 'Directed']
nextVal = [6,  14]
dialogueTree.insert(10,text,choice,nextVal, asset)

#Binary Tree 6
asset = ['prince2.png', 'ds scratch 2.png']
text = ['Aku mendapatkan digit kedua dalam perjalanan ini!', 'Selamat, kamu sudah berhasil mengumpulkan semua digit yang diperlukan!', 'Ayo kita berjalan lagi, jalan ini sudah dekat dengan kerajaanku!']
choice = []
nextVal = [4,8]
dialogueTree.insert(6,text,choice,nextVal, asset)

#Binary Tree 4
asset = ['prince2.png']
text = ['Akhirnya aku bisa pulang! Aku akan segera menginterogasi pengawal ku yang tidak becus menjagaku ini' ]
choice = []
nextVal = []
dialogueTree.insert(4,text,choice,nextVal, asset)

#Binary Tree 8
asset = ['prince2.png']
text = ['Ternyata benar dia ada di sini.', 'Untung saja dia belum sempat masuk. Ayo tangkap dia!', 'Tidakkk!!!']
choice = []
nextVal = []
dialogueTree.insert(8,text,choice,nextVal, asset)

#Binary Tree 14
asset = ['prince2.png', 'ds scratch 2.png']
text = ['Aku mendapatkan digit kedua dalam perjalanan ini!', 'Selamat, kamu sudah berhasil mengumpulkan semua digit yang diperlukan!', 'Ayo kita berjalan lagi, jalan ini sudah dekat dengan kerajaanku!']
choice = []
nextVal = [12,16]
dialogueTree.insert(14,text,choice,nextVal, asset)

#Binary Tree 12
asset = ['prince2.png']
text = ['Akhirnya aku bisa pulang! Aku akan segera menginterogasi pengawal ku yang tidak becus menjagaku ini' ]
choice = []
nextVal = []
dialogueTree.insert(12,text,choice,nextVal, asset)

#Binary Tree 16
asset = ['prince2.png']
text = ['Ternyata benar dia ada di sini.', 'Untung saja dia belum sempat masuk. Ayo tangkap dia!', 'Tidakkk!!!']
choice = []
nextVal = []
dialogueTree.insert(11,text,choice,nextVal, asset)

#Binary Tree 26
asset = ['sungai.png', 'prince2.png']
text = ['Air sungai ini sangat dingin! Tetapi sepertinya aku tidak punya pilihan lain selain berenang.']
choice = ['Majemuk', 'Sederhana']
nextVal = [22,  30]
dialogueTree.insert(26,text,choice,nextVal, asset)

#Binary Tree 22
asset = ['sungai.png', 'prince2.png']
text = ['Tidak sia-sia aku berenang ke sini, ternyata aku mendapatkan digit terakhir yang kuperlukan! Tetapi aku sangat kedinginan.', 'Ah, aku akan menghangatkan diri sebentar dengan menyalakan api unggun.', ]
choice = ['folding', 'carry']
nextVal = [20,  24]
dialogueTree.insert(22,text,choice,nextVal, asset)

#Binary Tree 20
asset = ['sungai.png', 'prince2.png']
text = ['Akhirnya aku bisa pulang! Aku akan segera menginterogasi pengawal ku yang tidak becus menjagaku ini']
choice = []
nextVal = []
dialogueTree.insert(20,text,choice,nextVal, asset)

#Binary Tree 24
asset = ['sungai.png', 'prince2.png']
text = ['Ah kenapa membuat api unggun begitu sulit', 'Ternyata benar dia ada di sini.', 'Untung saja dia belum sempat masuk. Ayo tangkap dia!', 'Tidakkk!!!']
choice = []
nextVal = []
dialogueTree.insert(24,text,choice,nextVal, asset)

#Binary Tree 30
asset = ['sungai.png', 'prince2.png']
text = ['Tidak sia-sia aku berenang ke sini, ternyata aku mendapatkan digit terakhir yang kuperlukan! Tetapi aku sangat kedinginan..', 'Ah, aku akan menghangatkan diri sebentar dengan menyalakan api unggun.']
choice = ['Inorder', 'Postorder']
nextVal = [28,32]
dialogueTree.insert(30,text,choice,nextVal, asset)

#Binary Tree 28
asset = ['sungai.png', 'prince2.png']
text = ['Akhirnya aku bisa pulang! Aku akan segera menginterogasi pengawal ku yang tidak becus menjagaku ini']
choice = []
nextVal = []
dialogueTree.insert(28,text,choice,nextVal, asset)

#Binary Tree 53
asset = ['sungai.png', 'prince2.png']
text = ['Ah kenapa membuat api unggun begitu sulit', '']
choice = []
nextVal = []
dialogueTree.insert(53,text,choice,nextVal, asset)

#Binary Tree 50
asset = ['rumah kosong.jpg', 'prince2.png', 'hutan pagi.jpg', 'blackpanther.jpg']
text = ['Ayo cari pangeran itu, dia pasti tidak jauh dari sini.', 'Kita sudah mencari semalaman dan tidak menemukannya. Apa mungkin dia sudah berhasil kembali ke kerajaannya?', 'Tidak mungkin! Cepat cari lagi, kita harus menemukannya.', 'Itu adalah orang-orang yang menculikku! Aku harus kabur dari sini.', 'Aku harus menyeberangi sungai ini. Bagaimana caraku untuk menyeberang?']
choice = ['Min', 'Max']
nextVal = [42,  58]
dialogueTree.insert(50,text,choice,nextVal, asset)

#Binary Tree 42
asset = ['prince2.png', 'hutan pagi.jpg', 'blackpanther.jpg']
text = []
choice = ['Single', 'Linear']
nextVal = [38,  46]
dialogueTree.insert(42,text,choice,nextVal, asset)

#Binary Tree 38
asset = ['prince2.png']
text = ['Akhirnya aku mendapatkan digit kedua. Sekarang aku hanya perlu mencari jalan ke kerajaanku.']
choice = []
nextVal = [36,  40]
dialogueTree.insert(38,text,choice,nextVal, asset)

#Binary Tree 36
asset = ['prince2.png']
text = ['Akhirnya aku bisa pulang! Aku akan segera menginterogasi pengawal ku yang tidak becus menjagaku ini' ]
choice = []
nextVal = []
dialogueTree.insert(36,text,choice,nextVal, asset)

#Binary Tree 40
asset = ['prince2.png']
text = ['Ternyata benar dia ada di sini.', 'Untung saja dia belum sempat masuk. Ayo tangkap dia!', 'Tidakkk!!!']
choice = []
nextVal = []
dialogueTree.insert(40,text,choice,nextVal, asset)

#Binary Tree 46
asset = ['prince2.png', 'ds scratch 2.png']
text = ['Aku mendapatkan digit kedua dalam perjalanan ini!', 'Selamat, kamu sudah berhasil mengumpulkan semua digit yang diperlukan!', 'Ayo kita berjalan lagi, jalan ini sudah dekat dengan kerajaanku!']
choice = []
nextVal = [44,48]
dialogueTree.insert(46,text,choice,nextVal, asset)

#Binary Tree 44
asset = ['prince2.png']
text = ['Akhirnya aku bisa pulang! Aku akan segera menginterogasi pengawal ku yang tidak becus menjagaku ini']
choice = []
nextVal = []
dialogueTree.insert(44,text,choice,nextVal, asset)

#Binary Tree 48
asset = ['prince2.png']
text = ['Ternyata benar dia ada di sini.', 'Untung saja dia belum sempat masuk. Ayo tangkap dia!', 'Tidakkk!!!']
choice = []
nextVal = []
dialogueTree.insert(48,text,choice,nextVal, asset)

#Binary Tree 58
asset = ['prince2.png']
text = []
choice = ['Circular', 'Double']
nextVal = [54, 62]
dialogueTree.insert(58,text,choice,nextVal, asset)

#Binary Tree 54
asset = ['prince2.png']
text = ['Wah, aku mendapatkan digit kedua..tetapi aku terluka cukup parah, aku harus segera mengobatinya.', 'Tanaman obat yang mana ya yang benar?']
choice = ['dequeue', 'enqueue']
nextVal = [52, 56]
dialogueTree.insert(54,text,choice,nextVal, asset)

#Binary Tree 52
asset = ['prince2.png']
text = ['Hebat sekali tanaman obat ini! Sekarang aku harus mencari kerajaanku.']
choice = ['dequeue', 'enqueue']
nextVal = [51, 53]
dialogueTree.insert(52,text,choice,nextVal, asset)

#Binary Tree 51
asset = ['prince2.png']
text = ['Akhirnya aku bisa pulang! Aku akan segera menginterogasi pengawal ku yang tidak becus menjagaku ini' ]
choice = []
nextVal = []
dialogueTree.insert(51,text,choice,nextVal, asset)

#Binary Tree 53
asset = ['prince2.png']
text = ['Ternyata benar dia ada di sini.', 'Untung saja dia belum sempat masuk. Ayo tangkap dia!', 'Tidakkk!!!']
choice = []
nextVal = []
dialogueTree.insert(53,text,choice,nextVal, asset)

#Binary Tree 56
asset = ['prince2.png']
text = []
choice = []
nextVal = []
dialogueTree.insert(56,text,choice,nextVal, asset)


#Binary Tree 62
asset = ['prince2.png']
text = []
choice = ['LISCH', 'ELICH']
nextVal = [60, 64]
dialogueTree.insert(62,text,choice,nextVal, asset)

#Binary Tree 60
asset = ['prince2.png']
text = ['Hebat sekali tanaman obat ini! Sekarang aku harus mencari kerajaanku.']
choice = []
nextVal = [59, 61]
dialogueTree.insert(60,text,choice,nextVal, asset)

#Binary Tree 59
asset = ['prince2.png']
text = ['Akhirnya aku bisa pulang! Aku akan segera menginterogasi pengawal ku yang tidak becus menjagaku ini']
choice = []
nextVal = []
dialogueTree.insert(59,text,choice,nextVal, asset)

#Binary Tree 61
asset = ['prince2.png']
text = ['Ternyata benar dia ada di sini.', 'Untung saja dia belum sempat masuk. Ayo tangkap dia!', 'Tidakkk!!!']
choice = []
nextVal = []
dialogueTree.insert(61,text,choice,nextVal, asset)

#Binary Tree 64
asset = ['prince2.png']
text = []
choice = []
nextVal = []
dialogueTree.insert(64,text,choice,nextVal, asset)

#Binary Tree 98
asset = ['prince2.png', 'ds scratch 2.png']
text = ['Lihat… aku berhasil mendapatkan 1 digit.', 'Selamat, kamu hanya perlu mencari 1 digit lagi.', 'Aku tidak sabar untuk segera pulang, mari kita lanjutkan perjalanan ini.']
choice = ['Tunggal', 'Majemuk']
nextVal = [82, 114]
dialogueTree.insert(98,text,choice,nextVal, asset)

#Binary Tree 82
asset = ['hutan malam.png', 'prince2.png']
text = ['Rumah ini sepertinya tidak berpenghuni, aku akan beristirahat di sini malam ini.']
choice = ['Edge', 'Node']
nextVal = [74, 90]
dialogueTree.insert(82,text,choice,nextVal, asset)

#Binary Tree 74
asset = ['hutan malam.png', 'prince2.png']
text = []
choice = ['Ya', 'Tidak']
nextVal = [70, 78]
dialogueTree.insert(74,text,choice,nextVal, asset)

#Binary Tree 70
asset = ['hutan malam.png', 'prince2.png']
text = ['Loh kok aku tidak mendapatkan digit lagi? Bagaimana aku bisa pulang?', 'Kamu harus mencari jalan lain selain lewat gerbang', 'Hah? Bagaimana caranya?', 'Sudah liat saja nanti, kita temukan dulu kerajaanmu']
choice = ['Push', 'Pop']
nextVal = [68,72]
dialogueTree.insert(70,text,choice,nextVal, asset)

#Binary Tree 68
asset = ['hutan malam.png', 'prince2.png']
text = ['Aha! Aku akan memanjat pagar tembok kerajaanku dengan tangga ini!', 'Akhirnya aku bisa pulang! Aku akan segera menginterogasi pengawal ku yang tidak becus menjagaku ini']
choice = ['Pop', 'Push']
nextVal = []
dialogueTree.insert(68,text,choice,nextVal, asset)

#Binary Tree 72
asset = ['hutan malam.png', 'prince2.png']
text = ['Ternyata benar dia ada di sini.', 'Untung saja dia belum sempat masuk. Ayo tangkap dia!', 'Tidakkk!!!']
nextVal = []
dialogueTree.insert(72,text,choice,nextVal, asset)

#Binary Tree 78
asset = ['hutan malam.png', 'prince2.png']
text = ['Bagus sekali, aku mendapatkan digit kedua. Sekarang aku hanya perlu menemukan kerajaanku, seharusnya ada di dekat sini.', 'Kenapa tidak bisa dibuka ya?', 'Ternyata benar dia ada di sini.', 'Untung saja dia belum sempat masuk. Ayo tangkap dia!', 'Tidakkk!!!'] 
choice = []
nextVal = []
dialogueTree.insert(78,text,choice,nextVal, asset)

#Binary Tree 90
asset = ['hutan malam.png', 'prince2.png']
text = ['Rumah ini sepertinya tidak berpenghuni, aku akan beristirahat di sini malam ini.']
choice = ['Prefix', 'Postfix']
nextVal = [86, 94]
dialogueTree.insert(90,text,choice,nextVal, asset)

#Binary Tree 86
asset = ['hutan malam.png', 'prince2.png']
text = ['Pas sekali di situ ada kayu dan korek api! Aku akan menyalakan api untuk menghangatkan tubuh.']
choice = ['1', '2']
nextVal = [84, 88]
dialogueTree.insert(86,text,choice,nextVal, asset)

#Binary Tree 84
asset = ['hutan malam.png', 'prince2.png']
text = ['Kenapa tidak bisa dibuka ya?', 'Ternyata benar dia ada di sini.', 'Untung saja dia belum sempat masuk. Ayo tangkap dia!', 'Tidakkk!!!']
choice = []
nextVal = []
dialogueTree.insert(84,text,choice,nextVal, asset)

#Binary Tree 88
asset = ['hutan malam.png', 'prince2.png']
text = ['Waduh, gawat! Aku hanya punya 1 digit, tidak bisa membuka gerbang ini!', 'Kamu harus mencari jalan lain selain lewat gerbang', 'Hah? Bagaimana caranya?']
choice = ['Linked List', 'Array']
nextVal = [87, 89]
dialogueTree.insert(88,text,choice,nextVal, asset)

#Binary Tree 87
asset = ['hutan malam.png', 'prince2.png']
text = ['Aha! Aku akan memanjat pagar tembok kerajaanku dengan tangga ini!', 'Akhirnya aku bisa pulang! Aku akan segera menginterogasi pengawal ku yang tidak becus menjagaku ini']
choice = []
nextVal = []
dialogueTree.insert(87,text,choice,nextVal, asset)

#Binary Tree 89
asset = ['hutan malam.png', 'prince2.png']
text = ['Ternyata benar dia ada di sini.', 'Untung saja dia belum sempat masuk. Ayo tangkap dia!', 'Tidakkk!!!']
choice = []
nextVal = []
dialogueTree.insert(89,text,choice,nextVal, asset)

#Binary Tree 94
asset = ['sungai.jpg', 'prince2.png']
text = []
choice = []
nextVal = []
dialogueTree.insert(94,text,choice,nextVal, asset)

#Binary Tree 114
asset = ['prince2.png']
text = ['Malang sekali nasibku! Tidak menemukan makanan, kini mau beristirahat pun tidak ada tempat berteduh.', '(menghela nafas) hm..aku akan tidur di bawah pohon saja malam ini.', 'Gawat mereka menemukan keberadaan ku. Aku harus segera lari.']
choice = ['Tidak', 'Ya']
nextVal = [106, 122]
dialogueTree.insert(114,text,choice,nextVal, asset)

#Binary Tree 106
asset = ['prince2.png', 'sungai.png']
text = []
choice = ['Prefix', 'Postfix']
nextVal = [102, 110]
dialogueTree.insert(106,text,choice,nextVal, asset)

#Binary Tree 102
asset = ['prince2.png', 'sungai.png']
text = ['Astaga betapa beruntungnya aku menemukan kayu dan korek api ditempat ini, aku harus segera menghangatkan diri.']
choice = ['1', '2']
nextVal = [100,104]
dialogueTree.insert(102,text,choice,nextVal, asset)

#Binary Tree 110
asset = ['hutan sore.png', 'prince2.png', 'sungai.png']
text = ['Oh Tuhan, jika ini kehendakmu aku akan berserah mati kedinginan di tempat ini.']
choice = []
nextVal = []
dialogueTree.insert(110,text,choice,nextVal, asset)

#Binary Tree 100
asset = ['prince2.png', 'sungai.png']
text = ['Kenapa tidak bisa dibuka ya?', 'Ternyata benar dia ada di sini.', 'Untung saja dia belum sempat masuk. Ayo tangkap dia!', 'Tidakkk!!!']
choice = []
nextVal = []
dialogueTree.insert(100,text,choice,nextVal, asset)

#Binary Tree 104
asset = ['prince2.png', 'sungai.png']
text = ['Waduh, gawat! Aku hanya punya 1 digit, tidak bisa membuka gerbang ini!', 'Kamu harus mencari jalan lain selain lewat gerbang', 'Hah? Bagaimana caranya?']
choice = ['Linked List', 'Array']
nextVal = [57,59]
dialogueTree.insert(104,text,choice,nextVal, asset)

#Binary Tree 103
asset = ['prince2.png', 'sungai.png']
text = ['Aha! Aku akan memanjat pagar tembok kerajaanku dengan tangga ini!', 'Akhirnya aku bisa pulang! Aku akan segera menginterogasi pengawal ku yang tidak becus menjagaku ini']
choice = []
nextVal = []
dialogueTree.insert(103,text,choice,nextVal, asset)

#Binary Tree 105
asset = ['prince2.png', 'sungai.png']
text = ['Ternyata benar dia ada di sini.', 'Untung saja dia belum sempat masuk. Ayo tangkap dia!', 'Tidakkk!!!']
choice = []
nextVal = []
dialogueTree.insert(105,text,choice,nextVal, asset)

#Binary Tree 122
asset = ['hutan sore.png', 'prince2.png']
text = ['Lepaskan aku. Tidak ada untungnya kalian menangkap aku.', 'Seperti katamu, karena kamu tidak untung nya, maka akan aku buat kamu menghilang saja dari dunia ini.']
choice = []
nextVal = []
dialogueTree.insert(122,text,choice,nextVal, asset)

#Binary Tree 194
asset = ['hutan siang.png', 'prince2.png']
text = ['Dimana aku berada? Kenapa hutannya semakin gelap padahal masih siang?']
choice = ['Stack', 'Queue']
nextVal = [162,  226]
dialogueTree.insert(194,text,choice,nextVal, asset)

#Binary Tree 162
asset = ['hutan siang.jpg', 'prince2.png', 'ds scratch 2.png']
text = ['Apa ini?', 'Halo Halo Loha, aku DS, yang akan menemani mu di perjalanan ini.', 'Kamu kenapa bisa ada disini?', 'Aku diciptakan untuk membantu orang” yang tersesat di hutan ini.', 'Baiklah.']
choice = ['Queue', 'Stack']
nextVal = [34,  98]
dialogueTree.insert(162,text,choice,nextVal, asset)

#Binary Tree 226
asset = ['hutan siang.png', 'prince2.png']
text = ['Gawat ada orang yang mau menculikku disana, sebelum mereka sadar akan keberadaan ku aku harus segera bersembunyi.']
choice = ['Majemuk', 'Tunggal']
nextVal = [210,  242]
dialogueTree.insert(226,text,choice,nextVal, asset)

#Binary Tree 210
asset = ['semak-semak.png', 'prince2.png', 'ds scratch 2.png']
text = ['Apa ini?', 'Halo Halo Loha, aku DS, yang akan menemani mu di perjalanan ini.', 'Kamu kenapa bisa ada disini?', 'Aku diciptakan untuk membantu orang” yang tersesat di hutan ini.', 'Baiklah.']
choice = ['Queue','Stack']
nextVal = [34, 98]
dialogueTree.insert(210,text,choice,nextVal, asset)

#Binary Tree 242
asset = ['sema-semak.png', 'prince2.png']
text = ['Lepaskan aku, jangan ikat aku di pohon, pohon ini banyak semut nya.', 'Sudah diam saja, jangan banyak bicara. Awas saja kalau kau kabur lagi.']
choice = ['Sederhana', 'Majemuk']
nextVal = [234,  250]
dialogueTree.insert(242,text,choice,nextVal, asset)

#Binary Tree 234
asset = ['semak-semak.png', 'prince2.png']
text = ['Bagaimana kamu bisa terikat disini?', 'Siapa kamu, tolong lepaskan aku.', 'Nanti aku akan memperkenalkan diriku, sekarang aku akan membantumu melepaskan diri dari ikatan ini.', 'Halo Halo Loha, aku DS, yang akan menemani mu di perjalanan ini.', 'Kamu kenapa bisa ada disini?', 'Aku diciptakan untuk membantu orang” yang tersesat di hutan ini.', 'Baiklah.']
choice = ['Queue', 'Stack']
nextVal = [34]
dialogueTree.insert(234,text,choice,nextVal, asset)


#Binary Tree 250
asset = ['sema-semak.png', 'prince2.png']
text = ['Hoi, sudah kubilang jangan bermain" dengan diriku, sekarang rasakan akibatnya.']
choice = []
nextVal = []
dialogueTree.insert(250,text,choice,nextVal, asset)


dialogueTree.printIn()


