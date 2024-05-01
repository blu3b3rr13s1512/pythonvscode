import streamlit as st
st.set_page_config(layout='wide')
bill = 0
st.title ("Get Eat Restaurant")
st.image('https://cdn.pixabay.com/photo/2017/10/09/19/29/eat-2834549_1280.jpg')

st.header('Meals')
food1,food2,food3,food4 = st.columns(4)

with food1:
    st.image('https://cdn.pixabay.com/photo/2015/11/08/01/22/quesadilla-1032985_1280.jpg')
    if st.checkbox ('Chicken Quesadillas : $46'):
        bill+=46
        st.success('Added to Cart')

with food2:
    st.image('https://cdn.pixabay.com/photo/2020/07/18/11/20/chia-5416921_1280.jpg')
    if st.checkbox ("Chia salad: $45"):
        bill+=45
        st.success ("Added to Cart")

with food3:
    st.image('https://cdn.pixabay.com/photo/2021/06/28/08/58/curry-6370998_960_720.jpg')
    if st.checkbox ("Japanese Curry:$37"):
        bill+=37
        st.success("Added to cart")

with food4:
    st.image('https://cdn.pixabay.com/photo/2015/09/09/22/01/steak-933667_1280.jpg')
    if st.checkbox ("Steak with fries : $ 50"):
        bill+=50
        st.success("Added to cart")


st.header('Side Meals')
side1,side2,side3,side4 = st.columns(4)
with side1:
    st.image('https://cdn.pixabay.com/photo/2019/08/15/10/46/mozzarella-sticks-4407742_1280.jpg')
    if st.checkbox("Mozzarella Sticks : $25"):
        bill+=25
        st.success("Added to cart")

with side2:
    st.image('https://cdn.pixabay.com/photo/2014/08/26/15/24/sausage-428067_1280.jpg')
    if st.checkbox("Sausages: $24"):
        bill+=24
        st.success("Added to cart")

with side3:
    st.image('https://cdn.pixabay.com/photo/2015/03/06/12/14/garlic-bread-661578_960_720.jpg')
    if st.checkbox("Baguette with Garlic Butter : $26"):
        bill+=26
        st.success("Added to Cart")

with side4:
    st.image('https://cdn.pixabay.com/photo/2020/08/05/19/33/crunchy-5466250_1280.jpg')
    if st.checkbox ("Onion Rings: $22"):
        bill+=22
        st.success("Added to Cart")

st.header('Drinks')
drink1,drink2,drink3,drink4 = st.columns(4)
with drink1:
    st.image('https://cdn.pixabay.com/photo/2014/09/26/19/51/drink-462776_1280.jpg')
    if st.checkbox("Soft Drink (Coke, Sprite, Fanta): $15"):
        bill+=15
        st.success("Added to Cart")
with drink2:
    st.image('https://cdn.pixabay.com/photo/2018/07/18/07/56/drink-3545791_1280.jpg')
    if st.checkbox("Bubble Tea : $35"):
        bill+=35
        st.success ("Added to Cart")
with drink3:
    st.images('https://cdn.pixabay.com/photo/2012/11/28/09/31/orange-juice-67556_1280.jpg')
    if st.checkbox("Orange Juice: $20"):
        bill+=20
        st.success("Added to Cart")
with drink4:
    st.image ('https://cdn.pixabay.com/photo/2023/11/14/17/58/coffee-8388244_1280.jpg')
    if st.checkbox("Espresso Coffee : $30"):
        bill+=30
        st.success("Added to Cart")

st.header("Dessert")
dessert1,dessert2,dessert3,dessert4, = st.columns(4)
with dessert1:
    st.image('https://cdn.pixabay.com/photo/2016/08/23/08/53/ice-cream-1613798_1280.jpg')
    if st.checkbox("Brownie with Ice Cream : $36"):
        bill+=36
        st.success("Added to Cart")
with dessert2: 
    st.image('https://cdn.pixabay.com/photo/2022/10/21/18/50/apple-cake-7537812_960_720.jpg')
    if st.checkbox("Apple Crumble: $40"):
        bill+=40
        st.success("Added to Cart")
with dessert3:
    st.image('https://cdn.pixabay.com/photo/2017/09/19/02/57/key-2763884_1280.jpg')   
    if st.checkbox("Key Lime Pie : $36"):
        bill+=36
        st.success("added to Cart")
with dessert4:
    st.image('https://cdn.pixabay.com/photo/2021/04/12/10/42/tiramisu-6172170_1280.jpg')
    if st.checkbox("Tiramisu : $38"):
        bill+=38
        st.success("Added to Cart")

if st.button ("Check your total"):
    st.header(f'Your total bill is ${bill}')
    