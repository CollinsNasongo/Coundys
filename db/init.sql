-- ==========================
-- Domain Tables
-- ==========================
CREATE TABLE contact_type (
    contact_type_id BIGSERIAL PRIMARY KEY,
    contact_type_name VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE demographic_type (
    demographic_type_id BIGSERIAL PRIMARY KEY,
    demographic_type_name VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- ==========================
-- Base Table: County
-- ==========================
CREATE TABLE county (
    county_code VARCHAR(20) PRIMARY KEY,
    county_name VARCHAR(255) NOT NULL,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- ==========================
-- Contact Details
-- ==========================
CREATE TABLE contact_detail (
    contact_id BIGSERIAL PRIMARY KEY,
    county_code VARCHAR(20) NOT NULL,
    contact_type_id BIGINT NOT NULL,
    contact_information VARCHAR(1000) NOT NULL,
    description VARCHAR(255),
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (county_code) REFERENCES county(county_code) ON DELETE RESTRICT,
    FOREIGN KEY (contact_type_id) REFERENCES contact_type(contact_type_id) ON DELETE RESTRICT
);

-- ==========================
-- Governor
-- ==========================
CREATE TABLE governor (
    governor_id BIGSERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    image_url VARCHAR(1000),
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- ==========================
-- County–Governor Relationship
-- ==========================
CREATE TABLE county_governor (
    county_governor_id BIGSERIAL PRIMARY KEY,
    county_code VARCHAR(20) NOT NULL,
    governor_id BIGINT NOT NULL,
    tenure_start_date DATE NOT NULL,
    tenure_end_date DATE,
    active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (county_code) REFERENCES county(county_code) ON DELETE RESTRICT,
    FOREIGN KEY (governor_id) REFERENCES governor(governor_id) ON DELETE RESTRICT
);

-- ==========================
-- County Website
-- ==========================
CREATE TABLE county_website (
    website_id BIGSERIAL PRIMARY KEY,
    county_code VARCHAR(20) NOT NULL,
    website_url VARCHAR(1000) NOT NULL,
    description VARCHAR(255) DEFAULT 'main_website',
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (county_code) REFERENCES county(county_code) ON DELETE RESTRICT
);

-- ==========================
-- County Demographics
-- ==========================
CREATE TABLE county_demographic (
    demographic_id BIGSERIAL PRIMARY KEY,
    county_code VARCHAR(20) NOT NULL,
    demographic_type_id BIGINT NOT NULL,
    demographic_value VARCHAR(1000) NOT NULL,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (county_code) REFERENCES county(county_code) ON DELETE RESTRICT,
    FOREIGN KEY (demographic_type_id) REFERENCES demographic_type(demographic_type_id) ON DELETE RESTRICT
);

-- ==========================
-- Indexes (optional but recommended)
-- ==========================
CREATE INDEX idx_contact_detail_county_code ON contact_detail(county_code);
CREATE INDEX idx_county_governor_county_code ON county_governor(county_code);
CREATE INDEX idx_county_governor_governor_id ON county_governor(governor_id);
CREATE INDEX idx_county_demographic_type_id ON county_demographic(demographic_type_id);
