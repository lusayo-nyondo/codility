SELECT 
    event_type, 
    (latest_value - second_latest_value) AS value_diff
FROM (
    SELECT 
        event_type,
        -- Get the value of rank 1
        MAX(CASE WHEN rank_desc = 1 THEN value END) as latest_value,
        -- Get the value of rank 2
        MAX(CASE WHEN rank_desc = 2 THEN value END) as second_latest_value
    FROM (
        SELECT 
            event_type, 
            value, 
            ROW_NUMBER() OVER (PARTITION BY event_type ORDER BY time DESC) as rank_desc
        FROM events
    ) as ranked_events
    WHERE rank_desc <= 2
    GROUP BY event_type
) as final_values
-- Only include types that actually had a second latest value
WHERE second_latest_value IS NOT NULL
ORDER BY event_type ASC;