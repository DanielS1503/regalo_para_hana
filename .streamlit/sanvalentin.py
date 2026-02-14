import streamlit as st
import time

st.set_page_config(page_title="Para el amor de mi vida 💚", page_icon="💘")
# --- NUEVO TRUCO: FONDO MY MELODY + TARJETA BLANCA ---
st.markdown(
    """
    <style>
    /* 1. Ponemos tu imagen de My Melody de fondo en TODA la pantalla */
    .stApp {
        background-image: url("https://wallpapers.com/images/hd/my-melody-cute-pattern-oly3aszw5e2937kg.jpg");
        background-size: cover; /* Hace que llene la pantalla */
        background-attachment: fixed; /* Hace que el fondo no se mueva al bajar */
    }
    
    /* 2. Creamos la "tarjeta" blanca semitransparente para que se lea todo perfecto */
    .block-container, [data-testid="stAppViewBlockContainer"] {
        background-color: rgba(255, 255, 255, 0.9) !important; /* Blanco al 90% */
        border-radius: 20px; /* Bordes redondeados */
        padding: 3rem 2rem !important; /* Espacio para que respire el texto */
        margin-top: 3rem; /* Lo separa un poco del borde superior */
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2); /* Sombra elegante */
        max-width: 800px; /* Hace que la tarjeta no sea exageradamente ancha */
    }
    
    /* 3. Ajuste para esconder el fondo gris por defecto de Streamlit en la parte superior */
    header {
        background-color: transparent !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# ----------------------------------------

# ----------------------------------------
# ----------------------------------------

st.title("Feliz dia del amor y la amistad mi pulguita 💚")
st.write("---")

st.write("### Este es un detalle para ti Hanna, uno que podras tener guardado para siempre")
st.write("""Como estoy aprendiendo a programar te queria hacer este regalo, para que sepas que te tengo presente en todo de alguna u otra forma. 
""")

st.write("""Feliz primer 14 de febrero juntos, eres la unica persona con la que me encantaria compartir este dia la veces que sean posibles, te quiero hoy y siempre pequeña, disfrutemos el dia tanto como el resto
         \n No soy muy creyente del destino, pero le agradezco que me permitiera conocer y tener a alguien tan unica como lo eres tu, eres una gran persona, cosa que me hace sentir orgulloso de que tu seas mi pareja""")

st.image(r".streamlit/nuestra_foto.jpg", caption="Un pequeño recuerdo nuestro ❤️", use_container_width=True)

st.write("---")

st.subheader("Tengo una pregunta muy importante:")
respuesta = st.radio(
    "¿Qué opinas de este super regalo 🤓", 
    ["Elige una opción...", "Me encanta ", "Está muy lindo", "Te voy a robar la pc (Lo voy a guardar por siempre 💚)"]
)

if respuesta != "Elige una opción...":
    st.write("Te amo Hanna")
    
    if st.button("Toca aquí para tu sorpresa final 🎁"):
        with st.spinner('Cargando sorpresa...'):
            time.sleep(2)
        st.balloons() 

        st.success("Feliz 14 de febrero mi San Valentin, y espero que pronto el año, gracias por ser tu, princesa.")





