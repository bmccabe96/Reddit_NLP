use Reddit;


create table Posts
(
	id_num MEDIUMINT NOT NULL AUTO_INCREMENT,
    title VARCHAR(10000) UNIQUE,
    author VARCHAR(150),
    upvote_ratio FLOAT,
    id VARCHAR(20) UNIQUE,
    class VARCHAR(20),
    PRIMARY KEY (id_num)
)
;

create table Comments
(
	id_num MEDIUMINT NOT NULL AUTO_INCREMENT,
    body VARCHAR(10000) UNIQUE,
    comment_id VARCHAR(20),
    parent_id VARCHAR(20),
    link_id VARCHAR(20),
    author VARCHAR(150),
    score MEDIUMINT,
    class VARCHAR(20),
    PRIMARY KEY (id_num)
)
;