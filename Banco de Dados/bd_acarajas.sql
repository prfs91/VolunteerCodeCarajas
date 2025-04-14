CREATE DOMAIN dm_descricao VARCHAR(100);

CREATE TABLE cidade (
	id_cidade INTEGER NOT NULL,
	nome_cidade dm_descricao,
	uf_cidade CHAR(2),
	PRIMARY KEY (id_cidade)
);

CREATE TABLE bairro (
	id_bairro INTEGER NOT NULL,
	nome_bairro dm_descricao,
	cidade dm_descricao,
	PRIMARY KEY (id_bairro)
);

CREATE TABLE aux_escolaridade (
	id_escolaridade INTEGER NOT NULL,
	nome_escolaridade VARCHAR(20),
	PRIMARY KEY (id_escolaridade)
);

CREATE TABLE associado (
	id_associado INTEGER NOT NULL,
	nome_associado dm_descricao,
	nome_mae dm_descricao,
	nome_pai dm_descricao,
	data_nascimento dm_descricao,
	cidade_nascimento dm_descricao,
	uf_nascimento CHAR(2),
	rg_associado dm_descricao,
	orgao_expedidor_rg dm_descricao,
	cpf_associado dm_descricao,
	tipo_certidao dm_descricao,
	num_certidao dm_descricao,
	livro_certidao dm_descricao,
	folha_certidao dm_descricao,
	estado_civil dm_descricao,
	endereco dm_descricao,
	num_endereco dm_descricao,
	bairro_endereco dm_descricao,
	id_cidade_endereco INTEGER,
	uf_endereco dm_descricao,
	cep_endereco dm_descricao,
	contato_associado dm_descricao,
	whatsapp_associado dm_descricao,
	contato_recado dm_descricao,
	nome contato_recado dm_descricao,
	email_associado dm_descricao,
	tipo_deficiencia dm_descricao,
	causa_deficiencia dm_descricao,
	cid10 dm_descricao,
	usa_aparelho dm_descricao,
	estudante dm_descricao,
	escolaridade dm_descricao,
	profissao dm_descricao,
	foto dm_descricao,
	habilitado dm_descricao,
	
	
	PRIMARY KEY (id_associado)
	FOREIGN KEY (id_cidade_endereco) REFERENCES cidade (id_cidade)
);