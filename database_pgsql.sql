CREATE TABLE "users"(
    "user_id" BIGINT NOT NULL,
    "nom" VARCHAR(255) NOT NULL,
    "prenom" VARCHAR(255) NOT NULL,
    "email" VARCHAR(255) NOT NULL,
    "password" VARCHAR(255) NOT NULL,
    "created_at" DATE NOT NULL DEFAULT 'now()',
    "updated_at" DATE NULL
);
ALTER TABLE
    "users" ADD PRIMARY KEY("user_id");
ALTER TABLE
    "users" ADD CONSTRAINT "users_email_unique" UNIQUE("email");
CREATE TABLE "follows"(
    "follow_id" BIGINT NOT NULL,
    "user_id" BIGINT NOT NULL,
    "follower_id" BIGINT NOT NULL
);
ALTER TABLE
    "follows" ADD PRIMARY KEY("follow_id");
CREATE TABLE "posts"(
    "post_id" BIGINT NOT NULL,
    "user_id" BIGINT NOT NULL,
    "content" TEXT NOT NULL,
    "created_at" DATE NOT NULL DEFAULT 'now()',
    "updated_at" DATE NULL
);
ALTER TABLE
    "posts" ADD PRIMARY KEY("post_id");
CREATE TABLE "comments"(
    "comment_id" BIGINT NOT NULL,
    "user_id" BIGINT NOT NULL,
    "post_id" BIGINT NOT NULL,
    "content" TEXT NOT NULL,
    "cretated_at" DATE NOT NULL,
    "update_at" DATE NULL
);
ALTER TABLE
    "comments" ADD PRIMARY KEY("comment_id");
CREATE TABLE "post_tags"(
    "post_tag_id" BIGINT NOT NULL,
    "post_id" BIGINT NOT NULL,
    "label" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "post_tags" ADD PRIMARY KEY("post_tag_id");
CREATE TABLE "post_likes"(
    "post_like_id" BIGINT NOT NULL,
    "post_id" BIGINT NOT NULL,
    "user_id" BIGINT NOT NULL
);
ALTER TABLE
    "post_likes" ADD PRIMARY KEY("post_like_id");
CREATE TABLE "comments_likes"(
    "comment_like_id" BIGINT NOT NULL,
    "comment_id" BIGINT NOT NULL,
    "user_id" BIGINT NOT NULL
);
ALTER TABLE
    "comments_likes" ADD PRIMARY KEY("comment_like_id");
ALTER TABLE
    "follows" ADD CONSTRAINT "follows_follower_id_foreign" FOREIGN KEY("follower_id") REFERENCES "users"("user_id");
ALTER TABLE
    "post_tags" ADD CONSTRAINT "post_tags_post_id_foreign" FOREIGN KEY("post_id") REFERENCES "posts"("post_id");
ALTER TABLE
    "post_likes" ADD CONSTRAINT "post_likes_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "users"("user_id");
ALTER TABLE
    "comments" ADD CONSTRAINT "comments_post_id_foreign" FOREIGN KEY("post_id") REFERENCES "posts"("post_id");
ALTER TABLE
    "comments_likes" ADD CONSTRAINT "comments_likes_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "users"("user_id");
ALTER TABLE
    "posts" ADD CONSTRAINT "posts_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "users"("user_id");
ALTER TABLE
    "comments_likes" ADD CONSTRAINT "comments_likes_comment_id_foreign" FOREIGN KEY("comment_id") REFERENCES "comments"("comment_id");
ALTER TABLE
    "comments" ADD CONSTRAINT "comments_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "users"("user_id");
ALTER TABLE
    "follows" ADD CONSTRAINT "follows_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "users"("user_id");
ALTER TABLE
    "post_likes" ADD CONSTRAINT "post_likes_post_id_foreign" FOREIGN KEY("post_id") REFERENCES "posts"("post_id");