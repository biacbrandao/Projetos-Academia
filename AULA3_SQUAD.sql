create table squads(
	id integer primary key auto_increment,
    nome varchar(15)
);

create table projetos(
	id integer primary key auto_increment,
    nome varchar(20),
    id_squad integer,
    foreign key (id_squad) references squads(id)
);

create table pessoas(
	nome varchar(30),
    cpf varchar(20) primary key,
    cargo varchar(20)
);

create table projeto_pessoa(
	id_projeto integer,
    id_pessoa varchar(20),
    foreign key (id_projeto) references projetos(id),
    foreign key (id_pessoa) references pessoas(cpf)
);