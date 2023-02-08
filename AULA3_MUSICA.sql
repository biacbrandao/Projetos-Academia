create schema exemplo_musica;

create table cantor_banda(
	id integer primary key auto_increment,
    nome varchar(15),
    genero_musical varchar(15)
);

create table album(
	id integer primary key auto_increment,
    nome varchar(20),
    id_cantor_banda integer,
    foreign key (id_cantor_banda) references cantor_banda(id)
);

create table musicas(
	nome varchar(30),
    id integer primary key auto_increment,
    ano integer
);

create table album_musicas(
	id_album integer,
    id_musica integer,
    foreign key (id_album) references album(id),
    foreign key (id_musica) references musicas(id)
);