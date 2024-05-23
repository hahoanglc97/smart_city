import pandas as pd

key = pd.read_csv("/Users/ha/Project/AWS_key/smart_city_project_user_accessKeys.csv")

configuration = {
    "AWS_ACCESS_KEY": key["Access key ID"][0],
    "AWS_SECRET_KEY": key["Secret access key"][0],
}
