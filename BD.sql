CREATE DATABASE pw2-ingresso;

use pw2_ingresso;

CREATE TABLE TBL_FILME (
    ID_FILME BIGINT PRIMARY KEY IDENTITY,
    TX_NOME VARCHAR(50) NOT NULL,
    NR_DURACAO INT NOT NULL,
    TP_CATEGORIA VARCHAR(17) NOT NULL,
    TP_CLASSIFICACAO VARCHAR(5),
    CHK_EM_CARTAZ VARCHAR(1),
    NR_ANO INT,
    TX_CAPA VARCHAR(300),
    TX_DIRETOR VARCHAR(300),
    TX_ELENCO VARCHAR(300),
    TX_DESCRICAO VARCHAR(500),
    NR_AVALIACAO FLOAT
);


INSERT INTO TBL_FILME (
    TX_NOME,
    NR_DURACAO,
    TP_CATEGORIA,
    TP_CLASSIFICACAO,
    CHK_EM_CARTAZ,
    NR_ANO,
    TX_CAPA,
    TX_DIRETOR,
    TX_ELENCO,
    TX_DESCRICAO,
    NR_AVALIACAO
) VALUES (
    'Interestelar',
    169,
    'FICCAO_CIENTIFICA',
    'A10',
    'S',
    2014,
    'https://exemplo.com/capas/interestelar.jpg',
    'Christopher Nolan',
    'Matthew McConaughey, Anne Hathaway, Jessica Chastain',
    'Uma equipe de exploradores viaja através de um buraco de minhoca em busca de um novo lar para a humanidade.',
    8.7
);

INSERT INTO TBL_FILME (
    TX_NOME,
    NR_DURACAO,
    TP_CATEGORIA,
    TP_CLASSIFICACAO,
    CHK_EM_CARTAZ,
    NR_ANO,
    TX_CAPA,
    TX_DIRETOR,
    TX_ELENCO,
    TX_DESCRICAO,
    NR_AVALIACAO
) VALUES (
    'O Poderoso Chefão',
    175,
    'DRAMA',
    'A16',
    'N',
    1972,
    'https://exemplo.com/capas/poderoso-chefao.jpg',
    'Francis Ford Coppola',
    'Marlon Brando, Al Pacino, James Caan',
    'A história da família Corleone e sua influência no mundo do crime organizado.',
    9.2
);

INSERT INTO TBL_FILME (
    TX_NOME,
    NR_DURACAO,
    TP_CATEGORIA,
    TP_CLASSIFICACAO,
    CHK_EM_CARTAZ,
    NR_ANO,
    TX_CAPA,
    TX_DIRETOR,
    TX_ELENCO,
    TX_DESCRICAO,
    NR_AVALIACAO
) VALUES (
    'Toy Story',
    81,
    'ANIMACAO',
    'LIVRE',
    'N',
    1995,
    'https://exemplo.com/capas/toy-story.jpg',
    'John Lasseter',
    'Tom Hanks, Tim Allen, Don Rickles',
    'Um grupo de brinquedos ganha vida quando os humanos não estão por perto.',
    8.3
);

INSERT INTO TBL_FILME (
    TX_NOME,
    NR_DURACAO,
    TP_CATEGORIA,
    TP_CLASSIFICACAO,
    CHK_EM_CARTAZ,
    NR_ANO,
    TX_CAPA,
    TX_DIRETOR,
    TX_ELENCO,
    TX_DESCRICAO,
    NR_AVALIACAO
) VALUES (
    'Matrix',
    136,
    'ACAO',
    'A14',
    'S',
    1999,
    'https://exemplo.com/capas/matrix.jpg',
    'Lana Wachowski, Lilly Wachowski',
    'Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss',
    'Um hacker descobre que a realidade como ele conhece é uma elaborada simulação.',
    8.7
);

INSERT INTO TBL_FILME (
    TX_NOME,
    NR_DURACAO,
    TP_CATEGORIA,
    TP_CLASSIFICACAO,
    CHK_EM_CARTAZ,
    NR_ANO,
    TX_CAPA,
    TX_DIRETOR,
    TX_ELENCO,
    TX_DESCRICAO,
    NR_AVALIACAO
) VALUES (
    'O Rei Leão',
    118,
    'AVENTURA',
    'LIVRE',
    'N',
    1994,
    'https://exemplo.com/capas/o-rei-leao.jpg',
    'Roger Allers, Rob Minkoff',
    'Matthew Broderick, Jeremy Irons, James Earl Jones',
    'Um jovem leão precisa enfrentar desafios para assumir seu lugar como rei das Terras do Reino.',
    8.5
);
