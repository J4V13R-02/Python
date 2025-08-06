import pandas as pd

personTable = pd.DataFrame({'personId': [1, 2],
                            'lastName': ['Wang', 'Alice'],
                            'firstName': ['Allen', 'Bob']})
addressTable = pd.DataFrame({'addressId': [1, 2],
                            'personId': [2, 3],
                            'city': ['New York City', 'Leetcode'],
                            'state': ['New York', 'California']})
resultado = pd.merge(personTable, addressTable, on='personId', how='left')
resultado = resultado.drop(columns=['personId'])

print(personTable)
print(addressTable)
print(resultado)

