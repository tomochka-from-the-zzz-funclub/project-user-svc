create table users (
	id SERIAL primary key,
	email VARCHAR(255) unique not null,
    password VARCHAR(64) not null,
	name VARCHAR(255) not null,
	surname VARCHAR(255) not null,
	birth DATE not null,
	subscription BOOL not null default(false)
);

create table favorite_films (
	id SERIAL primary key,
	user_id INT not null references users(id),
	film_id INT not null references films(id),
    UNIQUE(user_id, film_id)
);
create table favorite_genres (
	user_id INT not null references users(id),
	genre_id INT not null references genres(id),
    UNIQUE(user_id, genre_id)
);

create table viewed (
	id SERIAL primary key,
	user_id INT not null references users(id),
	film_id INT not null references films(id),
	timecode TIME,
    UNIQUE(user_id, film_id)
);