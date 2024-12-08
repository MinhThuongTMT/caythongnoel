from turtle import *
import random as r
#
#cài đặt trang màn hình hiển thị
s= Screen()
s.title('Christmas tree 2023')
bgcolor('black') # màu nền nha
speed(3) # tốc độ vẽ 
pen(shown = False, pencolor='black', pensize=2, outline=10) # set up bút vẽ
pu() # nhấc bút lên
goto(-30,-130)
pd() # đặt bút xuống
ht()# dấu bút vẽ 

# Thân cây
fillcolor('brown') # thân cây tô màu nâu
begin_fill()
for i in range(2):
    fd(60)
    rt(90)
    fd(50)
    rt(90)
end_fill()

# Nhánh cây
fillcolor('green')
# Nhánh dưới cùng
pu()
goto(-150,-130) # xác định tọa độ cần vẽ
pd()
begin_fill()
goto(150, -130)
goto(90, -40)
goto(-90, -40)
goto(-150, -130)
end_fill()

# nhánh giữa
pu()
goto(-110, -40)
pd()
begin_fill()
goto(110, -40)
goto(50, 50)
goto(-50, 50)
goto(-110, -40)
end_fill()

# Nhánh trên cùng
pu()
goto(-70, 50)
pd()
begin_fill()
goto(70, 50)
goto(0, 150)
goto(-70, 50)
end_fill()

# vẽ quả bóng trang trí
centers = [(-110, -130), (110, -130), ( -50, -90), (40, -80), 
           (-30, -40),(90, -20),(-70,0),(40, 60)] # tọa độ vẽ bóng
# tô màu cho bóng
colors = ['yellow', 'purple', 'white', 'pink', 'yellow', 'white', 'red', 'blue']
i = 0
for c in centers:
    pu()
    goto(c)
    pd()
    fillcolor(colors[i]) # tô màu quả bóng
    pencolor(colors[i]) #màu viền bóng
    begin_fill()
    circle(15)# kích thước bóng
    end_fill()
    i +=1

# vẽ ngôi sao trên đầu cây thông
pu()
goto(-25, 165)  # Điều chỉnh vị trí của ngôi sao nằm đúng đỉnh cây
pensize(3)
color('red', 'yellow')
pd()
begin_fill()
for i in range(5):
    fd(50)
    rt(144)
end_fill()

# ghi thông điệp
def message(xcor, ycor):
    pu()
    goto(xcor, ycor)
    pd()
    pencolor('red')
    write('Merry Christmas 2024!', font=['vladimir script', 50, 'bold'])
    return()
# hộp quà
pu()
goto(200, -180)
pd()
color('red', 'orange')
begin_fill()
for i in range(4):
    fd(40)
    lt(90)
end_fill()
pu()
goto(220, -140)
color('red')
pd()
goto(200, -130)
goto(210, -120)
goto(220, -140)
goto(240, -130)
goto(230, -120)
goto(220, -140)

onclick(message(-250, 180))

# vẽ thêm tuyết rơi cho đẹp nha :)
def snow():
    ht()
    pensize(2)
    for i in range(50): # 50 bông tuyết
        pencolor('white')
        pu()
        setx(r.randint(-350, 350)) # set tọa độ trục x
        sety(r.randint(-100, 350)) # tọa độ trục y
        pd()
        dens = 6 # số cánh bông tuyết
        snowsize = r.randint(1, 10) # kích thước bông tuyết
        for j in range(dens):
            fd(int(snowsize))
            backward(int(snowsize))
            right(int(360/dens)) # góc quay cho bông
snow()
done()
