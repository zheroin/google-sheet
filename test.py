import pysheets

gc = pysheets.authorize()
wks = gc.open_by_key('18WX-VFi_yaZ6LkXWLH856sgAsH5CQHgzxjA5T2PGxIY')
s1 = wks.sheet1
# s1.update_acell('A1',"yoyo")
print s1.col_values(2,"cell")
#s1.update_cell(5,5,"again yoypo")