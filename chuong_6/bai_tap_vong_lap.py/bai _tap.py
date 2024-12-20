print("MENU:")
print("1. Xem danh sach sinh vien")
print("2. Nhap thong tin sinh moi vao danh sach")
print("3. Chinh sua thong tin sinh vien ung voi ma sinh vien")
print("4. Xoa thong tin sinh vien ung voi ma sinh vien")
print("5. Thoat chuong trinh")
lua_chon = input("Nhap lua chon ban muon su dung:")
if lua_chon.isdlgit() == False :
   print("yeu cau nhap lai")
else :
   lua_chon = int(lua_chon)
