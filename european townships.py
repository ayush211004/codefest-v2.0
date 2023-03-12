T=int(input("enter the no of townships"))
for i in range(1,T+1):
    N=int(input("enter no houses"))
    accent_qty = 0
    regular_qty = 0
    total_hours = 0
    for j in range(0,N):
        total_bedroom=int(input("enter total no of bed rooms"))
        R=int(input("enter no of roof bedrooms"))
        S=int(input("enter no of standard rooms"))
        H=int(input("enter the no of victorian halls"))
        area_accent_h = 1 / 3 * 6 * H
        area_regular_h = 2 / 3 * 6 * H
        area_accent_s = 1 / 3 * 4 * S
        area_regular_s = 2 / 3 * 4 * S
        area_accent_r = 1 / 3 * 3 * R
        area_regular_r = 2 / 3 * 3 * R
        accent_qty += ( area_accent_h + area_accent_s  + area_accent_r) *1.5
        regular_qty += area_regular_h * 2.25 + area_regular_s * 2.25 + area_regular_r * 2.25
        accent_time =2.5/1.5*accent_qty          #area_accent_h * 2.5 + area_accent_s * 2.5 + area_accent_r * 2.5
        regular_time = 3.25/2.25*regular_qty     #area_regular_h * 3.25 + area_regular_s * 3.25 + area_regular_r * 3.25
        total_hours=accent_time+regular_time
    print("case#", i , round(total_hours,2) , round(accent_qty,2) , round(regular_qty,2) )