from sqlalchemy import Column, Integer, String, Text, JSON, Date, ForeignKey, Boolean, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship



Base = declarative_base()


# Base Tables
class County(Base):
    __tablename__ = "county"

    county_code = Column(String(20), primary_key=True)
    county_name = Column(String(255), nullable=False)

    def __repr__(self):
        return f"County(county_code={self.county_code}, county_name={self.county_name})"
    
    def as_dict(self):
        return {
            "county_code": self.county_code,
            "county_name": self.county_name,
        }

# Domain Tables
class ContactType(Base):
    __tablename__ = "contact_type"

    contact_type_id = Column(Integer, primary_key=True, autoincrement=True)
    contact_type_name = Column(String(255), nullable=False, unique=True)

    def __repr__(self):
        return f"ContactType(contact_type_id={self.contact_type_id}, contact_type_name={self.contact_type_name})"

class DemographicType(Base):
    __tablename__ = "demographic_type"

    demographic_type_id = Column(Integer, primary_key=True, autoincrement=True)
    demographic_type_name = Column(String(255), nullable=False, unique=True)

    def __repr__(self):
        return f"Demographic(contact_type_id={self.demographic_type_id}, demographic_type_name={self.demographic_type_name})"


# Link/Bridge Tables
class CountyContact(Base):
    __tablename__ = "county_contact"

    county_contact_id = Column(Integer, primary_key=True, autoincrement=True)
    county_code = Column(String(20), ForeignKey("county.county_code"), nullable=False)
    contact_type_id = Column(
        String(20), ForeignKey("contact_types.contact_type_code"), nullable=False
    )
    contact_information = Column(Text, nullable=False)
    description = Column(String(255))  # Added description field
    def __repr__(self):
        return (
            f"CountyContact(county_contact_id={self.county_contact_id}, "
            f"county_code={self.county_code}, contact_type_id={self.contact_type_code}, "
            f"description={self.description})"
        )


class Governor(Base):
    __tablename__ = "governor"

    governor_id = Column(Integer, primary_key=True, autoincrement=True)
    governor_name = Column(JSON, nullable=False, default={"first_name": "", "last_name": ""})
    image_url = Column(Text)

    @property
    def full_name(self):
        return f"{self.governor_name.get('first_name', '')} {self.governor_name.get('last_name', '')}"

    def __repr__(self):
        return f"Governor(governor_id={self.governor_id}, full_name={self.full_name})"


class CountyGovernor(Base):
    __tablename__ = "county_governor"

    county_governor_id = Column(Integer, primary_key=True, autoincrement=True)
    county_code = Column(String(20), ForeignKey("county.county_code"), nullable=False)
    governor_id = Column(Integer, ForeignKey("governor.governor_id"), nullable=False)
    tenure_start_date = Column(Date, nullable=False)
    tenure_end_date = Column(Date)
    active = Column(Boolean, nullable=False, default=True)  # Added active flag with default True

    def __repr__(self):
        return (
            f"CountyGovernor(county_governor_id={self.county_governor_id}, "
            f"county_code={self.county_code}, governor_id={self.governor_id}, "
            f"active={self.active})"
        )
    
class CountyWebsite(Base):
    __tablename__ = "county_website"

    county_website_id = Column(Integer, primary_key=True, autoincrement=True)
    county_code = Column(String(20), ForeignKey("county.county_code"), nullable=False)
    description = Column(String(255), default="main_website")
    website_url = Column(Text, nullable=False)

    def __repr__(self):
        return (
            f"CountyWebsite(county_website_id={self.county_website_id}, "
            f"county_code={self.county_code}, description={self.description}, "
            f"website_url={self.website_url})"
        )
    
class CountyDemographic(Base):
    __tablename__ = "county_demographics"

    county_demographics_id = Column(Integer, primary_key=True)
    county_code = Column(String(20), ForeignKey("county.county_code"), nullable=False)
    demographic_id = Column(Integer, ForeignKey("demographic_type.demographic_id"), nullable=False)
    demographic_value = Column(Text, nullable=False)
    def __repr__(self):
        return (
            f"CountyDemographic(county_demographics_id={self.county_demographics_id}, "
            f"county_code={self.county_code}, demographic_id={self.demographic_id}, "
            f"demographic_value={self.demographic_value})"
        )

