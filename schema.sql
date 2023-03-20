create table vehicle (
    id SERIAL PRIMARY KEY,
    model_year CHAR(255) NOT NULL,
    make TEXT NOT NULL,
    model CHAR(255) NOT NULL,
    rejection_percentage CHAR(255) NOT NULL,
    reason_1 TEXT DEFAULT NULL,
    reason_2 TEXT DEFAULT NULL,
    reason_3 TEXT DEFAULT NULL
)