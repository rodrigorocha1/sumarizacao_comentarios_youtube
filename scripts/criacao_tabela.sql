CREATE  table canais (
	id_canal string PRIMARY KEY,
	nome_canal string
	
)


CREATE table videos (
	id_video string PRIMARY KEY,
	id_canal string,
	comentario_sumarizado string,
	FOREIGN KEY(id_canal) REFERENCES canais (id_canal)
)



CREATE table comentarios (
	id_comentario string PRIMARY KEY,
	id_video string,
	usuario string,
	comentario string,
	comentario_atualizado,
	data_publicacao string,
	data_atualizacao string,
	FOREIGN KEY(id_video) REFERENCES videos (id_video)
)


CREATE table resposta_comentarios (
	id_resposta_comentario string PRIMARY KEY,
	id_comentario string,
	usuario string,
	resposta_comentario string,
	data_publicacao string,
	data_atualizacao string,
	FOREIGN KEY(id_comentario) REFERENCES comentarios (id_comentario)
)
