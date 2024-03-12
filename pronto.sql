/*create database meu_projeto;*/
use meu_projeto;

create table if not exists funcionario(
	id int not null auto_increment,
    nome varchar(30) not null,
    senha varchar(20) not null,
    idade int(3) not null,
    cpf varchar(30) not null,
    primary key(id)
);

create table if not exists cliente(
	id int not null auto_increment,
    nome varchar(30) not null,
    idade int(3) not null,
    cpf varchar(11) not null,
    primary key(id)
);

create table if not exists cliente_veiculo(
	id int not null auto_increment,
    cliente_id integer,
    cpf varchar(11) not null,
    veiculo_id integer,
	tipo varchar(5) not null,
    marca varchar(30) not null,
    modelo varchar(30) not null,
    ano int(4) not null,
    cor varchar(15) not null,
    portas int(8),
    cilindragem int(10),
    primary key(id)
);

create table if not exists veiculo(
	id int not null auto_increment,
    tipo varchar(5) not null,
    marca varchar(30) not null,
    modelo varchar(30) not null,
    ano int(4) not null,
    cor varchar(15) not null,
    portas int(8),
    cilindragem int(10),
    primary key(id)
);
 
#alter table funcionario add column senha varchar(20) not null;
#alter table cliente_veiculo modify cpf varchar(11) not null;
#ALTER TABLE cliente MODIFY cpf VARCHAR(11);

insert into funcionario(nome, senha, idade, cpf)
values("Gustavo", 1313, 17, "10588626937"); 
SELECT * from funcionario;

