data base: community

create table clase / tabla Persona:
dni pk not null
name
lastname
email
phone_number
location unique


class / table User:
fk: dni
password
df: id_rol

class / table Role:
id
description

class / table predio:
id
location