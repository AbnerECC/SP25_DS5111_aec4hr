{{ config(materialized='table') }}

SELECT EN,FR
FROM DATA_SCIENCE.AEC4HR_RAW.NUMBERS
