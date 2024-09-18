# MAKE IT JUST LIKE THE FOOD ORDER APP. THIS ONE IS A BOOKSTORE
# ---
# What is your name?
# **3. Book Selection:**
# Make sure you arrange your books in different categories:
# Children Books
# Teenagers Books
# Family Books
# Christian Books
# Science Books
# Books in checkboxes with images, names and prices
# **Total Amount:**
# Based on your selections, the total amount will be calculated automatically.
# Mr. tee: get purchased book and plot chart
# #

import streamlit as st
st.set_page_config(layout='wide')
totalamount = 0
st.title("Book Store")
st.image('https://cdn.pixabay.com/photo/2016/01/08/20/32/bookstore-1129183_1280.png')

st.header("Children's Books")
cbook1,cbook2,cbook3,cbook4 = st.columns(4)

with cbook1:
    st.image('https://cdn.kobo.com/book-images/d6d305ee-606c-4869-a536-0272d718e835/1200/1200/False/goodnight-moon-5.jpg')
    if st.checkbox("Goodnight Moon - Margaret Wise Brown"):
        totalamount+=50
        st.success("added to your cart :D!")

with cbook2:
    st.image('https://m.media-amazon.com/images/I/813AS1xuZiL._AC_UF894,1000_QL80_.jpg')
    if st.checkbox("Charlotte's Web - E.B White"):
        totalamount+=50
        st.success("added to your cart! :D")
    
with cbook3:
    st.image('https://cdn.kobo.com/book-images/fd0b7174-6ade-4f15-9cff-574387f522bf/1200/1200/False/the-very-hungry-caterpillar-2.jpg')
    if st.checkbox("The Very Hungry Caterpillar - Eric Carle"):
        totalamount+=50
        st.success("added to your cart! :D")


with cbook4:
    st.image('https://cdn.kobo.com/book-images/60612814-4fcb-473e-833b-6f6e30d50d22/1200/1200/False/the-giving-tree-1.jpg')
    if st.checkbox("The Giving Tree - Shel Silverstein"):
        totalamount+=50
        st.success("added to your cart! :D")



st.header("Teenager's Books")
tbook1, tbook2, tbook3, tbook4 = st.columns(4)

with tbook1:
    st.image("https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1587396413l/52439531.jpg")
    if st.checkbox("The Inheritance games - Jennifer Lynn Barnes"):
        totalamount+=60
        st.success("added to your cart! :D")

with tbook2:
    st.image("https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1469509467i/29236380.jpg")
    if st.checkbox("Girl in Pieces - Kathleen Glasgow"):
        totalamount+=60
        st.success("added to your cart! :D")

with tbook3:
    st.image("https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1611937942i/56732449.jpg")
    if st.checkbox("The Love Hypothesis - Ali Hazelwood"):
        totalamount+=60
        st.success("added to your cart ! :D")

with tbook4:
    st.image("https://m.media-amazon.com/images/I/81cOaGbJ87L._AC_UF1000,1000_QL80_.jpg")
    if st.checkbox("One of Us is Lying - Karen M. McManus"):
        totalamount+=60
        st.success("added to your cart! :D")



st.header("Family Books")
fbook1,fbook2,fbook3,fbook4 = st.columns(4)

with fbook1:
    st.image("https://cdn.kobo.com/book-images/f7c39f83-b19a-4566-88cb-c13236e6178e/1200/1200/False/little-women-159.jpg")
    if st.checkbox ("Little Women - Louisa May Alcott"):
        totalamount +=60
        st.success("added to your cart ! :D")

with fbook2:
    st.image("https://cdn.kobo.com/book-images/4e50324c-3383-41ac-bcbf-268fa304c385/1200/1200/False/wonder-4.jpg")
    if st.checkbox("Wonder- RJ. Palacio"):
        totalamount+=60
        st.success("added to your cart! :D")

with fbook3:
    st.image("https://cdn.penguin.co.uk/dam-assets/books/9780141354804/9780141354804-jacket-large.jpg")
    if st.checkbox("Goodnight Mister Tom - Michelle Magorian"):
        totalamount+=60
        st.success("added to your cart! :D")

with fbook4:
    st.image("https://cdn.kobo.com/book-images/20f0c659-1d66-4f47-b034-219eb8f9a6a2/1200/1200/False/the-lion-the-witch-and-the-wardrobe-1.jpg")
    if st.checkbox("The Lion, the Witch, and the Wardrobe - C.S Lewis"):
        totalamount+=60
        st.success("added to your cart! :D")

st.header("Christian Books")
chbook1,chbook2,chbook3,chbook4 = st.columns(4)

with chbook1:
    st.image("https://m.media-amazon.com/images/I/81daouyEBkL._AC_UF1000,1000_QL80_.jpg")
    if st.checkbox ("A quest for Godliness - J.I Packer"):
        totalamount +=60
        st.success("added to your cart ! :D")

with chbook2:
    st.image("https://m.media-amazon.com/images/I/61P3-A4ZMDL._AC_UF1000,1000_QL80_.jpg")
    if st.checkbox("Knowing God - J.I Packer"):
        totalamount+=60
        st.success("added to your cart! :D")

with chbook3:
    st.image("https://m.media-amazon.com/images/I/61GJtxtcbdL._AC_UF894,1000_QL80_.jpg")
    if st.checkbox("Sheperding a Child's Heart - Tedd Tripp"):
        totalamount+=60
        st.success("added to your cart! :D")

with chbook4:
    st.image("https://m.media-amazon.com/images/I/91HcWj7U6pL._AC_UF1000,1000_QL80_.jpg")
    if st.checkbox("The Cross of Christ - John R.W Stott"):
        totalamount+=60
        st.success("added to your cart! :D")





st.header("Science Books")
sbook1,sbook2,sbook3,sbook4 = st.columns(4)

with sbook1:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT9xR8zeAlY1IwvOZEr3OGubSKLvEajRMGBYw&s")
    if st.checkbox ("Born Curious - Martha Freeman"):
        totalamount +=60
        st.success("added to your cart ! :D")

with sbook2:
    st.image("https://m.media-amazon.com/images/I/71NME-hLeaL._AC_UF1000,1000_QL80_.jpg")
    if st.checkbox("Listening to the stars - Jodie Parachini"):
        totalamount+=60
        st.success("added to your cart! :D")

with sbook3:
    st.image("https://m.media-amazon.com/images/I/81xWxdZCbUL._AC_UF1000,1000_QL80_.jpg")
    if st.checkbox("Once upon an atom - James Carter"):
        totalamount+=60
        st.success("added to your cart! :D")

with sbook4:
    st.image("https://cdn.kobo.com/book-images/252dc032-f9c2-4cf8-8589-f7af5e9359d3/1200/1200/False/the-book-of-why-9.jpg")
    if st.checkbox("The Book of Why - Judea Pearl"):
        totalamount+=60
        st.success("added to your cart! :D")

if st.button("Check Total Price!"):
    st.write("Your total price is", totalamount)
