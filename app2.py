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

with sobre:
    if artista == "Michael Jackson":
        st.markdown("""
# Michael Jackson

![Michael Jackson](https://upload.wikimedia.org/wikipedia/commons/5/55/Michael_Jackson_1988.jpg)

## Quem foi Michael Jackson?

Michael Joseph Jackson (1958–2009), conhecido como **Rei do Pop**, foi um cantor, compositor, dançarino e empresário norte-americano. É considerado um dos artistas mais influentes da história da música.

## Informações Básicas

| Informação | Detalhes |
|------------|-----------|
| Nome completo | Michael Joseph Jackson |
| Nascimento | 29 de agosto de 1958 |
| Local de nascimento | Gary, Indiana, Estados Unidos |
| Falecimento | 25 de junho de 2009 |
| Nacionalidade | Americana |
| Profissão | Cantor, compositor, dançarino e produtor |

## Principais Álbuns

### Thriller (1982)

![Thriller](https://upload.wikimedia.org/wikipedia/en/5/55/Michael_Jackson_-_Thriller.png)

O álbum mais vendido da história da música.

### Bad (1987)

![Bad](https://upload.wikimedia.org/wikipedia/en/5/51/Michael_Jackson_-_Bad.png)

Um dos álbuns mais populares de Michael Jackson.

## Músicas Mais Famosas

- Billie Jean
- Thriller
- Beat It
- Smooth Criminal
- Black or White

## Curiosidades

- Popularizou o famoso passo de dança chamado **Moonwalk**.
- Seu álbum **Thriller** bateu recordes de vendas.
- Ganhou diversos prêmios ao longo da carreira.
- Influenciou artistas de várias gerações.

## Michael Jackson em Show

![Michael Jackson em apresentação](https://upload.wikimedia.org/wikipedia/commons/0/02/Michael_Jackson_in_1984.jpg)

## Legado

Michael Jackson revolucionou a música pop, a dança e os videoclipes, deixando um legado que continua inspirando artistas e fãs em todo o mundo.
""")
    if artista ==  "50 Cent":
       st.markdown("""
# 50 Cent

![50 Cent](https://cdn-images.dzcdn.net/images/artist/58da3cca2d598e43c7a7823cf75277e5/1900x1900-000000-81-0-0.jpg)

## Quem é 50 Cent?

Curtis James Jackson III, mais conhecido como **50 Cent**, é um rapper, ator, produtor e empresário norte-americano. Ele ficou famoso no início dos anos 2000 e se tornou um dos maiores nomes do hip-hop mundial.

## Informações Básicas

| Informação | Detalhes |
|------------|-----------|
| Nome completo | Curtis James Jackson III |
| Nome artístico | 50 Cent |
| Nascimento | 6 de julho de 1975 |
| Local de nascimento | Queens, Nova York, Estados Unidos |
| Nacionalidade | Americana |
| Profissão | Rapper, ator, produtor e empresário |

## Principais Álbuns

### Get Rich or Die Tryin' (2003)

![Get Rich or Die Tryin'](https://upload.wikimedia.org/wikipedia/pt/7/73/Get_Rich_or_Die_Tryin%27.jpg)

Álbum de estreia que o tornou famoso mundialmente.

### The Massacre (2005)

![The Massacre](https://upload.wikimedia.org/wikipedia/pt/5/59/The_Massacre.jpg)

Um dos álbuns de rap mais vendidos dos anos 2000.

## Músicas Mais Famosas

- In Da Club
- Candy Shop
- P.I.M.P.
- Many Men (Wish Death)
- Just a Lil Bit
- 21 Questions

## Curiosidades

- Foi descoberto pelos rappers Eminem e Dr. Dre.
- É fundador da gravadora G-Unit Records.
- Além da música, teve sucesso como ator e produtor de séries.
- Tornou-se um empresário de sucesso com investimentos em diversas empresas.

## 50 Cent em Show

![50 Cent em apresentação](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQ9ZejOtcHTDniR0CwF6u0fw-uJbjkAF4-6BXm3eZWtDXhiup6R_6W4NU&s=10)

## Legado

50 Cent ajudou a definir o rap dos anos 2000 com seu estilo marcante, suas letras e seu sucesso comercial. Sua influência continua presente na música e no entretenimento.
""")
    if artista == "Billie Eilish": 
        st.markdown("""
                    
                   https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRToWH_06e5bGQn0EfeRfmB5fx5mIELDtygj3J6ma5XfqlYBhZRDkemWe-j&s=10,00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# Billie Eilish

![Billie Eilish](https://static.wikia.nocookie.net/gracieabrams/images/3/39/Billie_Eilish.jpeg/revision/latest?cb=20250318232144)

## Quem é Billie Eilish?

Billie Eilish Pirate Baird O'Connell, conhecida profissionalmente como **Billie Eilish**, é uma cantora e compositora norte-americana. Ela ganhou fama mundial com seu estilo musical único, misturando pop alternativo, eletrônica e indie.

## Informações Básicas

| Informação | Detalhes |
|------------|-----------|
| Nome completo | Billie Eilish Pirate Baird O'Connell |
| Nome artístico | Billie Eilish |
| Nascimento | 18 de dezembro de 2001 |
| Local de nascimento | Los Angeles, Califórnia, Estados Unidos |
| Nacionalidade | Americana |
| Profissão | Cantora e compositora |

## Principais Álbuns

### WHEN WE ALL FALL ASLEEP, WHERE DO WE GO? (2019)

![WHEN WE ALL FALL ASLEEP, WHERE DO WE GO?](https://upload.wikimedia.org/wikipedia/pt/8/8f/When_We_Fall_Asleep%2C_Where_Do_We_Go.png)

Álbum de estreia que a tornou um fenômeno mundial.

### Happier Than Ever (2021)

![Happier Than Ever](https://s2.glbimg.com/BhvoS48eOJDtKnxOGCIMHMcdKuM=/smart/e.glbimg.com/og/ed/f/original/2021/05/21/billie-eilish-happier-than-ever.jpeg)

Um dos álbuns mais aclamados de sua carreira.

## Músicas Mais Famosas

- bad guy
- lovely
- ocean eyes
- when the party's over
- everything i wanted
- Happier Than Ever
- Birds of a Feather

## Curiosidades

- Começou sua carreira ainda adolescente.
- Trabalha frequentemente com seu irmão, Finneas.
- Ganhou vários prêmios Grammy.
- É conhecida por seu estilo visual marcante e inovador.

## Billie Eilish em Show

![Billie Eilish em apresentação](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRToWH_06e5bGQn0EfeRfmB5fx5mIELDtygj3J6ma5XfqlYBhZRDkemWe-j&s=10)

## Legado

Billie Eilish revolucionou o pop moderno com sua voz suave, letras profundas e produção inovadora, tornando-se uma das artistas mais influentes de sua geração.
""")











