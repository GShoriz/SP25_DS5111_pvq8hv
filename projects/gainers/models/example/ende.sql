{{ config(materialized='table') }}

SELECT EN,DE
FROM DATA_SCIENCE.PVQ8HV_RAW.NUMBERS
