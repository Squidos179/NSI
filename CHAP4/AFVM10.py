import pandas
client=pandas.read_csv("fiches_client.csv")
commande=pandas.read_csv("fiches_com.csv")
cl_com=pandas.merge(client, commande)
df = pandas.DataFrame({"A":[12, 4, 5, 44, 1],
                "B":[5, 2, 54, 3, 2],
                "C":[20, 16, 7, 3, 8],
                "D":[14, 3, 17, 2, 6]})

print(df.mean(axis = 1))

