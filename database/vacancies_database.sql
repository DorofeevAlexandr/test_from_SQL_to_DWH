--area
CREATE TABLE IF NOT EXISTS area (
    id uuid PRIMARY KEY,
    hh_id TEXT NOT NULL,
    name TEXT NOT NULL,
    url TEXT
);


--employer
CREATE TABLE IF NOT EXISTS employer (
    id uuid PRIMARY KEY,
    hh_id TEXT NOT NULL,
    name TEXT NOT NULL,
    url TEXT
);

--vacancies
CREATE TABLE IF NOT EXISTS vacancies (
    id uuid PRIMARY KEY,
    hh_id TEXT NOT NULL,
    name TEXT NOT NULL,
    area_id uuid REFERENCES area ON DELETE CASCADE,
    employer_id uuid REFERENCES employer ON DELETE CASCADE,
    published_at TEXT,
    created_at TEXT,
    url TEXT
);

CREATE index IF NOT EXISTS vacancies_hh_id_idx ON vacancies(hh_id);

