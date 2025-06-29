import streamlit as st

# --------- Website Config ---------
st.set_page_config(page_title="Book Haven", page_icon="📚", layout="wide")
mode = st.sidebar.selectbox("🌓 Mode", ["Light", "Dark"])

if mode == "Dark":
    st.markdown(
        """
        <style>
        body {
            background-color: #0e1117;
            color: white;
        }
        .stApp {
            background-color: #0e1117;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
        <style>
        body {
            background-color: white;
            color: black;
        }
        .stApp {
            background-color: white;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


# --------- Sidebar (Left Panel) ---------
st.sidebar.image("images/logo.png", width=120)
st.sidebar.title("📚 Book Haven")
page = st.sidebar.selectbox("Menu", ["Home", "Books", "Search", "Contact", "About"])

st.sidebar.markdown("---")
st.sidebar.subheader("🎁 Offers")
st.sidebar.markdown("""
- 🔥 50% off Comics  
- 🚀 Buy 2 Get 1 Free  
- 💡 Programming Guide @ ₹299  
""")

st.sidebar.subheader("📰 Newsletter")
email = st.sidebar.text_input("Enter your email")
if st.sidebar.button("Subscribe"):
    st.sidebar.success("Subscribed!")

st.sidebar.subheader("📞 Contact")
st.sidebar.markdown("""
- 📧 support@bookhaven.com  
- ☎️ +91 9876543210  
""")

st.sidebar.subheader("🌐 Follow Us")
st.sidebar.markdown("""
[Instagram](https://instagram.com) | [Twitter](https://twitter.com) | [Facebook](https://facebook.com)
""")

# --------- Book Categories ---------
categories = ["All", "Comics", "Fiction", "Finance", "Programming", "Self Care"]

# --------- Book Data ---------
books = [
    # Comics
    {"title": "Marvel Encyclopedia", "author": "DK", "price": "₹999", "image": "images/Marvel.jpg", "category": "Comics"},
    {"title": "DC Comics", "author": "Melanie Scott", "price": "₹899", "image": "images/DC.jpg", "category": "Comics"},
    {"title": "Naruto", "author": "Masashi Kishimoto", "price": "₹399", "image": "images/Naruto.jpg", "category": "Comics"},
    {"title": "Attack on Titan", "author": "Hajime Isayama", "price": "₹450", "image": "images/aot.jpg", "category": "Comics"},
    {"title": "Demon Slayer", "author": "Koyoharu Gotouge", "price": "₹450", "image": "images/DemonSlayer.jpg", "category": "Comics"},
    {"title": "One Piece", "author": "Eiichiro Oda", "price": "₹450", "image": "images/OnePiece.jpg", "category": "Comics"},
    {"title": "Spiderman", "author": "Marvel", "price": "₹550", "image": "images/Spiderman.jpg", "category": "Comics"},

    # Programming
    {"title": "Intro to ML", "author": "Andriy Burkov", "price": "₹899", "image": "images/IntroToML.jpg", "category": "Programming"},
    {"title": "Design Patterns", "author": "Erich Gamma", "price": "₹799", "image": "images/DesignPatterns.jpg", "category": "Programming"},
    {"title": "Clean Code", "author": "Robert C. Martin", "price": "₹850", "image": "images/cleancode.jpg", "category": "Programming"},

    # Fiction
    {"title": "1984", "author": "George Orwell", "price": "₹499", "image": "images/1984.jpg", "category": "Fiction"},
    {"title": "Harry Potter", "author": "J.K. Rowling", "price": "₹699", "image": "images/harrypotter.jpg", "category": "Fiction"},
    {"title": "Midnight Library", "author": "Matt Haig", "price": "₹550", "image": "images/MidnightLibrary.jpg", "category": "Fiction"},
    {"title": "Percy Jackson", "author": "Rick Riordan", "price": "₹550", "image": "images/percy.jpg", "category": "Fiction"},
    {"title": "The Alchemist", "author": "Paulo Coelho", "price": "₹350", "image": "images/alchemist.jpg", "category": "Fiction"},

    # Finance
    {"title": "Psychology of Money", "author": "Morgan Housel", "price": "₹499", "image": "images/PsychologyOfMoney.jpg", "category": "Finance"},
    {"title": "Think And Grow Rich", "author": "Napoleon Hill", "price": "₹399", "image": "images/ThinkAndGrowRich.jpg", "category": "Finance"},
    {"title": "Millionaire Fastlane", "author": "MJ DeMarco", "price": "₹599", "image": "images/MillionaireFastlane.jpg", "category": "Finance"},
    {"title": "Atomic Habits", "author": "James Clear", "price": "₹499", "image": "images/AtomicHabits.jpg", "category": "Finance"},
    {"title": "Deep Work", "author": "Cal Newport", "price": "₹550", "image": "images/DeepWork.jpg", "category": "Finance"},
    {"title": "Can't Hurt Me", "author": "David Goggins", "price": "₹650", "image": "images/canthurtme.jpg", "category": "Finance"},

    # Self Care
    {"title": "Ikigai", "author": "Héctor García", "price": "₹399", "image": "images/Ikigai.jpg", "category": "Self Care"},
    {"title": "It Ends With Us", "author": "Colleen Hoover", "price": "₹499", "image": "images/ItEndsWithUs.jpg", "category": "Self Care"},
]

# --------- Layout ---------
left_spacer, main, right_panel = st.columns([0.1, 6, 2])

# --------- Home ---------
if page == "Home":
    with main:
        st.title("✨ Welcome to Book Haven ✨")
        st.image("images/banner.jpg", width=600)

        st.subheader("📚 Categories")
        cols = st.columns(6)
        cat_imgs = [
            ("Comics", "images/Comics.png"),
            ("Fiction", "images/Fiction.png"),
            ("Programming", "images/Programming.png"),
            ("Finance", "images/Finance.png"),
            ("Self Care", "images/selfHelp.png")
        ]
        for i, (cat, img) in enumerate(cat_imgs):
            with cols[i]:
                st.image(img, width=90)
                st.markdown(f"### {cat}")

        st.subheader("🔥 Book Promotion")
        st.image("images/Spiderman.jpg", width=300, caption="🔥 Check out the amazing Spiderman Series!")

        st.subheader("🎭 Top Comics")
        comics = [b for b in books if b["category"] == "Comics"][:4]
        for book in comics:
            st.image(book["image"], width=150)
            st.markdown(f"**{book['title']}**")

    with right_panel:
        st.subheader("⭐ Top Rated")
        top_rated = ["Atomic Habits", "Harry Potter", "Design Patterns"]
        for name in top_rated:
            for b in books:
                if b["title"] == name:
                    st.image(b["image"], width=120)
                    st.caption(b["title"])

        st.subheader("🆕 New Arrivals")
        new_arrivals = books[-4:]
        for book in new_arrivals:
            st.image(book["image"], width=120)
            st.caption(book["title"])

# --------- Books Page ---------
elif page == "Books":
    with main:
        st.title("📚 Explore Our Collection")
        selected_category = st.selectbox("Select Category", categories)
        filtered_books = [
            book for book in books if selected_category == "All" or book["category"] == selected_category
        ]

        cols = st.columns(2)
        for index, book in enumerate(filtered_books):
            with cols[index % 2]:
                st.image(book["image"], width=220)
                st.subheader(book["title"])
                st.write(f"**Author:** {book['author']}")
                st.write(f"**Price:** {book['price']}")
                st.write(f"**Category:** {book['category']}")
                if st.button(f"🛒 Add to Cart - {book['title']}"):
                    st.success(f"{book['title']} added to cart!")

    with right_panel:
        st.subheader("💡 Recommended")
        for book in books[:3]:
            st.image(book["image"], width=120)
            st.caption(book["title"])

# --------- Search Page ---------
elif page == "Search":
    with main:
        st.title("🔍 Search for Books")
        search_query = st.text_input("Enter book name:")
        if search_query:
            found = False
            for book in books:
                if search_query.lower() in book["title"].lower():
                    st.image(book["image"], width=200)
                    st.subheader(book["title"])
                    st.write(f"**Author:** {book['author']}")
                    st.write(f"**Price:** {book['price']}")
                    found = True
            if not found:
                st.error("No book found 😢")

    with right_panel:
        st.subheader("💥 Popular Picks")
        for book in books[-3:]:
            st.image(book["image"], width=120)
            st.caption(book["title"])

# --------- Contact ---------
elif page == "Contact":
    with main:
        st.title("📞 Contact Book Haven")
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            message = st.text_area("Your Message")
            submitted = st.form_submit_button("Send")
            if submitted:
                st.success(f"Thank you {name}! We'll reply to {email} soon. 💌")

    with right_panel:
        st.subheader("📢 Reach Out Anytime!")
        st.write("We love hearing from fellow book lovers!")

# --------- About ---------
elif page == "About":
    with main:
        st.title("❤️ About Book Haven")
        st.write("""
        ✨ **Book Haven** isn't just a bookstore — it's a peaceful online space for every curious mind.  
        📚 We believe that books heal, inspire, and transform lives.  
        🌱 Our mission is to bring soul-nourishing reads to every reader.  
        💖 Thank you for being part of our journey. Keep reading. Keep growing.
        """)
        st.image("images/banner.jpg", caption="Keep Reading. Keep Growing. 🌿")

    with right_panel:
        st.subheader("💌 Stay Connected")
        email = st.text_input("Your Email for Updates")
        if st.button("Subscribe to News"):
            st.success("Subscribed!")

# --------- Footer ---------
st.markdown("---")
st.caption("💖 Made with love by Book Haven | Powered by Python & Streamlit")
