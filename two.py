import pandas as pd


def process_data():
    # Do not alter this line.
    biopics = pd.read_csv("biopics.csv", encoding='latin-1')
    # Write your code here.
    # Remember to return the right object.

    # remove duplicates
    biopics = biopics.drop_duplicates()

    # rename 'box_office' to 'earnings'
    biopics=  biopics.rename(columns={'box_office': 'earnings'})

    # Filter out rows with missing earnings
    biopics = biopics[biopics['earnings'].notna()]

    # Keep only movies released in the year 1990
    biopics = biopics[biopics['year_release'] >= 1990]

    # Convert the type of subject and country to category
    biopics['type_of_subject'] = biopics['type_of_subject'].astype('category')
    biopics['country'] = biopics['country'].astype('category')

    # Create a new variable called lead_actor_actress_known
    biopics['lead_actor_actress_known'] = biopics['lead_actor_actress'].notna()

    # Update earnings so they are expressed in millions instead of dollars.
    biopics['earnings'] = biopics['earnings'] / 1_000_000

    # Reorder the columns in the data frame
    biopics = biopics[['title', 'year_release', 'earnings', 'country', 'type_of_subject', 'lead_actor_actress', 'lead_actor_actress_known']]

    # Sort in descending order by earnings
    biopics = biopics.sort_values(by='earnings', ascending=False)

    return biopics.reset_index(drop=True)
