{{ config(materialized='table') }}

SELECT EN,FR
FROM DATA_SCIENCE.PVQ8HV_RAW.NUMBERS
