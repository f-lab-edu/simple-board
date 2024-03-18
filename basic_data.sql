create table if not exists "post"
(
 "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
"title" VARCHAR(100) NOT NULL,
"content" TEXT,
"author" VARCHAR(50) NOT NULL,
"created_at" TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
"modified_at" TIMESTAMP
);

insert into post(title, content, author) values ('안녕하세요','운영을 담당하고 있습니다.', 'admin');