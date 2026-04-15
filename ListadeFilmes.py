import pandas as pd

nomesDefilmes = [ "Senhor dos Anéis", 
                 "Harry Potter", 
                 "Star Wars", 
                 "Matrix",
                 "Bastardos Inglórios",
                 "O Poderoso Chefão",           
                    "Pulp Fiction",
                    "Clube da Luta",
                    "O Senhor dos Anéis: O Retorno do Rei",     
                    "O Senhor dos Anéis: A Sociedade do Anel",
                    "O Senhor dos Anéis: As Duas Torres",
                    "O Hobbit: Uma Jornada Inesperada",
                    "O Hobbit: A Desolação de Smaug",
                    "O Hobbit: A Batalha dos Cinco Exércitos",
                    "Harry Potter e a Pedra Filosofal",
                    "Harry Potter e a Câmara Secreta",
                    "Harry Potter e o Prisioneiro de Azkaban",              
                    "Harry Potter e o Cálice de Fogo",
                    "Harry Potter e a Ordem da Fênix",
                    "Harry Potter e o Enigma do Príncipe",
                    "Harry Potter e as Relíquias da Morte - Parte 2",
                    "Star Wars: Episódio IV - Uma Nova Esperança",
                    "Star Wars: Episódio V - O Império Contra-Ataca",
                    "Star Wars: Episódio VI - O Retorno de Jedi",
                    "Star Wars: Episódio I - A Ameaça Fantasma",
                    "Star Wars: Episódio II - Ataque dos Clones",   
                    "Star Wars: Episódio III - A Vingança dos Sith",
                    "Jonh Wick",
                    "Jonh Wick 2",
                    "Jonh Wick 3",
                    "Jonh Wick 4",
                    "Vingadores: Ultimato",
                    "Vingadores: Guerra Infinita",  
                    "Vingadores: Era de Ultron",
                    "Vingadores: O Início da Guerra Infinita",      
                    "Vingadores: O Início da Era de Ultron",
                    "Vingadores: O Início do Ultimato",
                    "Um dia depois do amanhã",
                    "Blade o caçador de vampiros",
                    "Blade II",
                    "Blade Trinity"            

]

df = pd.DataFrame(nomesDefilmes,columns=["Nomes de Filmes"])

df["Categoria"] = "Filme"

print(df)   

