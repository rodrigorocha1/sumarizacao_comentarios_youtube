CREATE  table canais (
	id_canal string PRIMARY KEY,
	nome_canal string
	
);


CREATE table videos (
	id_video string PRIMARY KEY,
	id_canal string,
	titulo_video string,
	comentario_sumarizado string,
	FOREIGN KEY(id_canal) REFERENCES canais (id_canal)
);



CREATE table comentarios (
	id_comentario string PRIMARY KEY,
	id_video string,
	usuario string,
	comentario string,
	comentario_atualizado,
	data_publicacao string,
	data_atualizacao string,
	FOREIGN KEY(id_video) REFERENCES videos (id_video)
);


CREATE table resposta_comentarios (
	id_resposta_comentario string PRIMARY KEY,
	id_comentario string,
	usuario string,
	resposta_comentario string,
	resposta_comentario_atualizado string,
	data_publicacao string,
	data_atualizacao string,
	FOREIGN KEY(id_comentario) REFERENCES comentarios (id_comentario)
);


SELECT *
from comentarios 
WHERE  id_comentario= 'UgzLwUQoo7fSUQNdQKp4AaABAg';

SELECT *
FROM canais c ;

SELECT *
from videos v 
where v.id_video = 'bnB7pyDfOaY';

SELECT *
from resposta_comentarios rc 
INNER JOIN comentarios c on c.id_comentario  = rc.id_comentario 
where id_video  = 'LCnsyNfaAk4'
order by resposta_comentario;


SELECT *
from canais c 
INNER JOIN videos v on v.id_canal = 



SELECT canais.*, videos.*
FROM canais
JOIN videos ON canais.id_canal = videos.id_video
WHERE videos.id_video = 'bnB7pyDfOaY'
LIMIT 1;

DELETE FROM canais ;
DELETE FROM comentarios;
DELETE FROM videos;
DELETE FROM resposta_comentarios;

