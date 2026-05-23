import streamlit as st
from database import CATEGORIES, WASTE_DB

st.set_page_config(
    page_title="SortIt",
    page_icon="♻️",
    layout="wide"
)

# load css
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>",
                unsafe_allow_html=True)

# header
st.markdown(
    '<div class="main-title">♻ SortIt – Smart Waste Segregation</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Type waste item below</div>',
    unsafe_allow_html=True
)

# search
query = st.text_input(
    "Waste item",
    placeholder="banana peel, battery..."
)

if st.button("Check"):

    key = query.lower().strip()

    if key in WASTE_DB:

        cat_id, disposal = WASTE_DB[key]
        cat = CATEGORIES[cat_id]

        st.markdown(
            f"""
            <div class="result-card"
            style="background:{cat['bg']};
                   border-color:{cat['color']}">

            <h3 style="color:{cat['color']}">
            {cat['name']}
            </h3>

            <p>{disposal}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:
        st.error("Item not found")

# categories
st.divider()
st.subheader("Waste Categories")

cols = st.columns(2)

for i, (_, cat) in enumerate(CATEGORIES.items()):
    with cols[i % 2]:
        st.markdown(
            f"""
            <div class="category-card"
                 style="background:{cat['bg']}">

            <div class="category-name"
                 style="color:{cat['color']}">
                 {cat['name']}
            </div>

            <div class="category-desc">
                {cat['description']}
            </div>
            </div>
            """,
            unsafe_allow_html=True
        )
