import streamlit as st

musicas = {
    "Michael Jackson": {
        "Billie Jean": "https://www.youtube.com/watch?v=Zi_XLOBDo_Y&list=RDZi_XLOBDo_Y",
        "Thriller": "https://www.youtube.com/watch?v=4V90AmXnguw&list=RD4V90AmXnguw",
    },
    "50 Cent": {
        "In Da Club": "https://www.youtube.com/watch?v=5qm8PH4xAss&list=RD5qm8PH4xAss",
        "Many Men": "https://www.youtube.com/watch?v=5D3crqpClPY&list=RD5D3crqpClPY",
    },
    "Billie Eilish": {
        "Birds of a Feather": "https://www.youtube.com/watch?v=V9PVRfjEBTI&list=RDV9PVRfjEBTI"
    },
}
st.sidebar.image("logo.png")
artista = st.sidebar.selectbox("Selecione o artista:", musicas.keys())
musicas_artista = musicas[artista]
st.title(artista)
video,sobre= st.tabs(['video','sobre'])
with video:
    for musica in musicas_artista.items():
        titulo, link = musica
        st.subheader(titulo)
        st.video(link)

withsobre'














