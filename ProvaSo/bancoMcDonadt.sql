create database mcDonadt;

use mcDonadt;

create table pedido(
idPedido int primary key auto_increment,
numeroPedido char(3),
nome varchar(40),
cpf varchar(15),
lanche varchar(20)
)auto_increment = 1;

select*from pedido;