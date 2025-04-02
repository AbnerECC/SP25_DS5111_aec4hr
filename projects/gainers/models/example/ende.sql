{{ config(materialized='table') }}

SELECT EN,DE
FROM DATA_SCIENCE.AEC4HR_RAW.NUMBERS
