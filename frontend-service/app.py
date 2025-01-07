import streamlit as st
import requests
import json

# Sayfa konfigürasyonu
st.set_page_config(
    page_title="E-Ticaret Mikroservis",
    page_icon="🛍️",
    layout="wide"
)

# CSS stil tanımlamaları
st.markdown(
    """
    <style>
        .main-container {
            background-color: #ffebcd; /* Blanchedd Almond yakını */
            padding: 30px;
        }

        h1 {
            color: #1a5276;
            padding: 10px 0;
            border-bottom: 2px solid #1abc9c;
        }

        h3 {
            color: #2e4053;
            margin: 15px 0;
        }

        .stButton>button {
            background: linear-gradient(to right, #1abc9c, #16a085);
            color: #fff;
            padding: 10px 20px;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            transition: 0.3s ease;
        }

        .stButton>button:hover {
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.15);
            transform: translateY(-3px);
        }

        .stTextInput>div>div>input {
            border-radius: 8px;
            border: 1px solid #95a5a6;
            padding: 8px 12px;
        }

        .message-box {
            background-color: #e8f8f5;
            color: #0e6655;
            padding: 12px;
            border-radius: 5px;
            margin: 15px 0;
        }

        .json-view {
            background-color: #fdfefe;
            padding: 16px;
            border-radius: 6px;
            border: 1px solid #d5dbdb;
        }

        .expander-header {
            background-color: #f9f9f9;
            padding: 12px;
            border-radius: 5px;
            margin: 8px 0;
        }

        .error-message {
            background-color: #f6ddcc;
            color: #943126;
            padding: 10px;
            border-radius: 5px;
            margin: 10px 0;
        }
        .stApp {
            background-color: blanchedalmond    ;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Ana başlık
st.title("🛍️ E-Ticaret Yönetim Paneli")
st.markdown("---")

# Sol ve sağ kolonları oluştur
left_col, right_col = st.columns([2, 3])

with left_col:
    with st.expander("👤 Yeni Kullanıcı Ekle", expanded=True):
        name = st.text_input("İsim", placeholder="Örn: Ahmet Yılmaz")
        email = st.text_input("Email", placeholder="ornek@email.com")
        if st.button("➕ Kullanıcı Oluştur"):
            try:
                response = requests.post("http://user-service:8001/api/users", 
                                      json={"name": name, "email": email})
                if response.status_code == 200:
                    st.success("✅ Kullanıcı başarıyla oluşturuldu!")
            except Exception as e:
                st.error(f"❌ Hata: {str(e)}")

    with st.expander("📦 Yeni Ürün Ekle", expanded=True):
        product_name = st.text_input("Ürün Adı", placeholder="Örn: Gaming Laptop")
        price = st.number_input("Fiyat (TL)", min_value=0.0, step=0.01)
        if st.button("➕ Ürün Oluştur"):
            try:
                response = requests.post("http://product-service:8002/api/products", 
                                      json={"name": product_name, "price": price})
                if response.status_code == 200:
                    st.success("✅ Ürün başarıyla oluşturuldu!")
            except Exception as e:
                st.error(f"❌ Hata: {str(e)}")

    with st.expander("🛒 Yeni Sipariş Oluştur", expanded=True):
        try:
            users_response = requests.get("http://user-service:8001/api/users")
            users = users_response.json()
            usernames = [user["name"] for user in users.values()]
            username = st.selectbox("Kullanıcı Seçin", usernames)
        except:
            st.error("Kullanıcı listesi yüklenemedi!")
            username = st.text_input("Kullanıcı Adı")

        try:
            products_response = requests.get("http://product-service:8002/api/products")
            products = products_response.json()
            product_names = [product["name"] for product in products.values()]
            selected_products = st.multiselect("Ürünleri Seçin", product_names)
        except:
            st.error("Ürün listesi yüklenemedi!")
            selected_products = st.text_input("Ürün Adları (virgülle ayırın)").split(",")

        total = st.number_input("Toplam Tutar (TL)", min_value=0.0, step=0.01)

        if st.button("➕ Sipariş Oluştur"):
            try:
                response = requests.post("http://order-service:8003/api/orders", 
                                      json={
                                          "username": username,
                                          "product_names": selected_products,
                                          "total": total
                                      })
                if response.status_code == 200:
                    st.success("✅ Sipariş başarıyla oluşturuldu!")
                else:
                    st.error(f"❌ Hata: {response.json().get('detail', 'Bilinmeyen hata')}")
            except Exception as e:
                st.error(f"❌ Hata: {str(e)}")

with right_col:
    st.subheader("📊 Sistem Verileri")
    if st.button("🔄 Verileri Yenile", key="refresh"):
        try:
            st.markdown("### 👥 Kullanıcılar")
            users = requests.get("http://user-service:8001/api/users").json()
            st.json(users)

            st.markdown("### 📦 Ürünler")
            products = requests.get("http://product-service:8002/api/products").json()
            st.json(products)

            st.markdown("### 🛒 Siparişler")
            orders = requests.get("http://order-service:8003/api/orders").json()
            st.json(orders)
        except Exception as e:
            st.error(f"❌ Veri yüklenirken hata oluştu: {str(e)}")

st.markdown("---")
st.markdown("### 📌 Sistem Durumu")
col1, col2, col3 = st.columns(3)

try:
    with col1:
        try:
            response = requests.get("http://user-service:8001/api/users", timeout=5)
            if response.status_code == 200:
                st.success("✅ Kullanıcı Servisi Aktif")
            else:
                st.error("❌ Kullanıcı Servisi Kapalı")
        except requests.exceptions.RequestException:
            st.error("❌ Kullanıcı Servisi Kapalı")

    with col2:
        try:
            response = requests.get("http://product-service:8002/api/products", timeout=5)
            if response.status_code == 200:
                st.success("✅ Ürün Servisi Aktif")
            else:
                st.error("❌ Ürün Servisi Kapalı")
        except requests.exceptions.RequestException:
            st.error("❌ Ürün Servisi Kapalı")

    with col3:
        try:
            response = requests.get("http://order-service:8003/api/orders", timeout=5)
            if response.status_code == 200:
                st.success("✅ Sipariş Servisi Aktif")
            else:
                st.error("❌ Sipariş Servisi Kapalı")
        except requests.exceptions.RequestException:
            st.error("❌ Sipariş Servisi Kapalı")
except:
    st.error("❌ Servis durumları kontrol edilemiyor")
