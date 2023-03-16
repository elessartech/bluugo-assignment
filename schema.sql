create table rejections (
    id SERIAL PRIMARY KEY,
    model_year INTEGER NOT NULL,
    make TEXT NOT NULL,
    model TEXT NOT NULL,
    rejection_procentage FLOAT NOT NULL,
    reason_1 TEXT DEFAULT NULL,
    reason_2 TEXT DEFAULT NULL,
    reason_3 TEXT DEFAULT NULL
)