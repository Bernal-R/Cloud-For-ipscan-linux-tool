from typing import List, Dict
from pydantic import Field, BaseModel
import uuid

# -----------------------------------------------------------------------------
# CATEGORIES FIELD
# -----------------------------------------------------------------------------
class CategoriesField(BaseModel):
    bots: bool = Field(False, title='Botnet member activity')
    crypto_mining: bool = Field(False, title='Used for cryptocurrency mining')
    ip_scan: bool = Field(False, title='Illegally scan networks looking for vulnerabilities')
    ip_dynamic: bool = Field(False, title='Includes ip addresses of dial-up servers and DSL lines')
    malware: bool = Field(False, title='Includes IPs from malicious sites or websites with malware')
    anonymization: bool = Field(False, title='Includes the IP addresses of the Web proxies that can be used for anonymous browsing')
    command_center_botnets: bool = Field(False, title='Includes IP addresses, botnet hosting command and server control')
    spam: bool = Field(False, title='Includes the IP addresses that send spam')

# -----------------------------------------------------------------------------
# IP TAGS
# -----------------------------------------------------------------------------
class IpAnalysisTagsField(BaseModel):
    host_name: str = Field(None, title='Name of the computer that sent the ip to analyze')
    time: str = Field(None, title="The timestamp when ip to analyze was send")

# -----------------------------------------------------------------------------
# BASE CREATE ANALYSIS
# -----------------------------------------------------------------------------
class BaseCreateAnalysisSchema(BaseModel):
    ip: str = Field(None, title='Ip to be analize')
    score: int = Field(None, title='CVSS score')
    country: str = Field(None, title='Country where server is alocated')
    tags: IpAnalysisTagsField = Field(None, title="Tags for ip analysis")
    categories: CategoriesField = Field(None, title='Contains the categories of risks presented')

# -----------------------------------------------------------------------------
# IP ANALYSIS METRIC
# -----------------------------------------------------------------------------
class CreateAnalysisMetric(BaseCreateAnalysisSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


