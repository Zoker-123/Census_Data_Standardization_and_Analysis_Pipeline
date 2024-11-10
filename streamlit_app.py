#!/usr/bin/env python
# coding: utf-8

# In[27]:


import mysql.connector
import pandas as pd
import streamlit as st

# Function to create a connection to the MySQL database
def create_connection():
    connection = mysql.connector.connect(
        host='localhost',  # Replace with your database host
        user='root',  # Replace with your database username
        password='root123',  # Replace with your database password
        database='census_data'  # Replace with your database name
    )
    return connection


# In[28]:


def total_population_per_district():
    conn = create_connection()
    query = "SELECT District, Population FROM census_data GROUP BY District LIMIT 5"
    df = pd.read_sql(query, conn)
    conn.close()
    return df


# In[29]:


def literate_males_females_per_district():
    conn = create_connection()
    query = "SELECT District_Code, State_UT, District, Literate_Male, Literate_Female FROM census_data GROUP BY District"
    df = pd.read_sql(query, conn)
    conn.close()
    return df


# In[30]:


def percentage_of_workers_per_district():
    conn = create_connection()
    query = "SELECT District_Code, State_UT, District, ROUND((Workers/Population)*100, 2) \
                            AS Percentage_of_Workers FROM census_data"
    df = pd.read_sql(query, conn)
    conn.close()
    return df


# In[31]:


def households_with_lpg_png_per_district():
    conn = create_connection()
    query = "SELECT District_Code, State_UT, District, LPG_or_PNG_Households FROM census_data"
    df = pd.read_sql(query, conn)
    conn.close()
    return df


# In[6]:


def religious_composition_per_district():
    conn = create_connection()
    query = """
    SELECT district, 
           SUM(CASE WHEN religion = 'Hindu' THEN 1 ELSE 0 END) AS hindus,
           SUM(CASE WHEN religion = 'Muslim' THEN 1 ELSE 0 END) AS muslims,
           SUM(CASE WHEN religion = 'Christian' THEN 1 ELSE 0 END) AS christians
    FROM census_data
    GROUP BY district
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df


# In[7]:


def households_with_internet_access_per_district():
    conn = create_connection()
    query = """
    SELECT district, 
           SUM(CASE WHEN internet_access = 'Yes' THEN 1 ELSE 0 END) AS households_with_internet
    FROM census_data
    GROUP BY district
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df


# In[8]:


def educational_attainment_distribution_per_district():
    conn = create_connection()
    query = """
    SELECT district, 
           SUM(CASE WHEN education_level = 'Below Primary' THEN 1 ELSE 0 END) AS below_primary,
           SUM(CASE WHEN education_level = 'Primary' THEN 1 ELSE 0 END) AS primary,
           SUM(CASE WHEN education_level = 'Middle' THEN 1 ELSE 0 END) AS middle,
           SUM(CASE WHEN education_level = 'Secondary' THEN 1 ELSE 0 END) AS secondary
    FROM census_data
    GROUP BY district
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df


# In[9]:


def transportation_access_per_district():
    conn = create_connection()
    query = """
    SELECT district, 
           SUM(CASE WHEN transportation_mode = 'Bicycle' THEN 1 ELSE 0 END) AS households_with_bicycle,
           SUM(CASE WHEN transportation_mode = 'Car' THEN 1 ELSE 0 END) AS households_with_car,
           SUM(CASE WHEN transportation_mode = 'Radio' THEN 1 ELSE 0 END) AS households_with_radio,
           SUM(CASE WHEN transportation_mode = 'Television' THEN 1 ELSE 0 END) AS households_with_tv
    FROM census_data
    GROUP BY district
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df


# In[10]:


def condition_of_census_houses_per_district():
    conn = create_connection()
    query = """
    SELECT district, 
           SUM(CASE WHEN condition = 'Dilapidated' THEN 1 ELSE 0 END) AS dilapidated,
           SUM(CASE WHEN condition = 'With Separate Kitchen' THEN 1 ELSE 0 END) AS with_kitchen,
           SUM(CASE WHEN condition = 'With Bathing Facility' THEN 1 ELSE 0 END) AS with_bathing,
           SUM(CASE WHEN condition = 'With Latrine Facility' THEN 1 ELSE 0 END) AS with_latrine
    FROM census_data
    GROUP BY district
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df


# In[11]:


def household_size_distribution_per_district():
    conn = create_connection()
    query = """
    SELECT district, 
           SUM(CASE WHEN household_size = 1 THEN 1 ELSE 0 END) AS one_person,
           SUM(CASE WHEN household_size = 2 THEN 1 ELSE 0 END) AS two_persons,
           SUM(CASE WHEN household_size BETWEEN 3 AND 5 THEN 1 ELSE 0 END) AS three_to_five_persons
    FROM census_data
    GROUP BY district
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df


# In[12]:


def total_households_per_state():
    conn = create_connection()
    query = "SELECT state, COUNT(*) AS total_households FROM census_data GROUP BY state"
    df = pd.read_sql(query, conn)
    conn.close()
    return df


# In[13]:


def latrine_facility_per_state():
    conn = create_connection()
    query = """
    SELECT state, 
           SUM(CASE WHEN latrine_facility = 'Yes' THEN 1 ELSE 0 END) AS households_with_latrine
    FROM census_data
    GROUP BY state
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df


# In[14]:


def average_household_size_per_state():
    conn = create_connection()
    query = """
    SELECT state, 
           AVG(household_size) AS average_household_size
    FROM census_data
    GROUP BY state
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df


# In[15]:


def owned_vs_rented_households_per_state():
    conn = create_connection()
    query = """
    SELECT state, 
           SUM(CASE WHEN ownership = 'Owned' THEN 1 ELSE 0 END) AS owned,
           SUM(CASE WHEN ownership = 'Rented' THEN 1 ELSE 0 END) AS rented
    FROM census_data
    GROUP BY state
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df


# In[16]:


def latrine_facility_distribution_per_state():
    conn = create_connection()
    query = """
    SELECT state, 
           SUM(CASE WHEN latrine_type = 'Pit Latrine' THEN 1 ELSE 0 END) AS pit_latrine,
           SUM(CASE WHEN latrine_type = 'Flush Latrine' THEN 1 ELSE 0 END) AS flush_latrine
    FROM census_data
    GROUP BY state
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df


# In[17]:


def drinking_water_access_per_state():
    conn = create_connection()
    query = """
    SELECT state, 
           SUM(CASE WHEN drinking_water_access = 'Yes' THEN 1 ELSE 0 END) AS households_with_drinking_water
    FROM census_data
    GROUP BY state
    """
    df


# In[18]:


def average_household_income_distribution_per_state():
    conn = create_connection()
    query = """
    SELECT state, 
           AVG(household_income) AS average_household_income
    FROM census_data
    GROUP BY state
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df


# In[19]:


def married_couples_percentage_per_state():
    conn = create_connection()
    query = """
    SELECT state, 
           (SUM(CASE WHEN marital_status = 'Married' THEN 1 ELSE 0 END) / COUNT(*)) * 100 AS percentage_married
    FROM census_data
    GROUP BY state
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df


# In[20]:


def households_below_poverty_line_per_state():
    conn = create_connection()
    query = """
    SELECT state, 
           SUM(CASE WHEN poverty_status = 'Below Poverty Line' THEN 1 ELSE 0 END) AS households_below_poverty
    FROM census_data
    GROUP BY state
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df


# In[21]:


def overall_literacy_rate_per_state():
    conn = create_connection()
    query = """
    SELECT state, 
           (SUM(CASE WHEN literate = 'Yes' THEN 1 ELSE 0 END) / COUNT(*)) * 100 AS literacy_rate
    FROM census_data
    GROUP BY state
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df


# In[ ]:




