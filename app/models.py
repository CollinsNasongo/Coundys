from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class ContactType(db.Model):
    __tablename__ = 'contact_type'

    contact_type_id = db.Column(db.BigInteger, primary_key=True)
    contact_type_name = db.Column(db.String(255), nullable=False, unique=True)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)


class DemographicType(db.Model):
    __tablename__ = 'demographic_type'

    demographic_type_id = db.Column(db.BigInteger, primary_key=True)
    demographic_type_name = db.Column(db.String(255), nullable=False, unique=True)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)


class County(db.Model):
    __tablename__ = 'county'

    county_code = db.Column(db.String(20), primary_key=True)
    county_name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)


class ContactDetail(db.Model):
    __tablename__ = 'contact_detail'

    contact_id = db.Column(db.BigInteger, primary_key=True)
    county_code = db.Column(db.String(20), db.ForeignKey('county.county_code', ondelete='RESTRICT'), nullable=False)
    contact_type_id = db.Column(db.BigInteger, db.ForeignKey('contact_type.contact_type_id', ondelete='RESTRICT'), nullable=False)
    contact_information = db.Column(db.String(1000), nullable=False)
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)

    county = db.relationship('County', backref='contact_details')
    contact_type = db.relationship('ContactType', backref='contact_details')


class Governor(db.Model):
    __tablename__ = 'governor'

    governor_id = db.Column(db.BigInteger, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(1000))
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)


class CountyGovernor(db.Model):
    __tablename__ = 'county_governor'

    county_governor_id = db.Column(db.BigInteger, primary_key=True)
    county_code = db.Column(db.String(20), db.ForeignKey('county.county_code', ondelete='RESTRICT'), nullable=False)
    governor_id = db.Column(db.BigInteger, db.ForeignKey('governor.governor_id', ondelete='RESTRICT'), nullable=False)
    tenure_start_date = db.Column(db.Date, nullable=False)
    tenure_end_date = db.Column(db.Date)
    active = db.Column(db.Boolean, nullable=False, default=True)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)

    county = db.relationship('County', backref='governors')
    governor = db.relationship('Governor', backref='terms')


class CountyWebsite(db.Model):
    __tablename__ = 'county_website'

    website_id = db.Column(db.BigInteger, primary_key=True)
    county_code = db.Column(db.String(20), db.ForeignKey('county.county_code', ondelete='RESTRICT'), nullable=False)
    website_url = db.Column(db.String(1000), nullable=False)
    description = db.Column(db.String(255), default='main_website')
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)

    county = db.relationship('County', backref='websites')


class CountyDemographic(db.Model):
    __tablename__ = 'county_demographic'

    demographic_id = db.Column(db.BigInteger, primary_key=True)
    county_code = db.Column(db.String(20), db.ForeignKey('county.county_code', ondelete='RESTRICT'), nullable=False)
    demographic_type_id = db.Column(db.BigInteger, db.ForeignKey('demographic_type.demographic_type_id', ondelete='RESTRICT'), nullable=False)
    demographic_value = db.Column(db.String(1000), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)

    county = db.relationship('County', backref='demographics')
    demographic_type = db.relationship('DemographicType', backref='demographics')
