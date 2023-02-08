create table departamentos(
	id integer,
    nome varchar(20),
    diretora varchar(30)
);

alter table departamentos add constraint pk_id primary key(id);

create table disciplinas(
	id integer,
    nome varchar(20),
    carga_horaria tinyint
);

alter table disciplinas add constraint pk_id primary key(id);
alter table disciplinas add column id_departamento integer;
alter table disciplinas add constraint fk_id foreign key(id_departamento)
 references departamentos (id);