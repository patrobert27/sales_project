def total_income(df_sales, df_products):
    # Utlilizo el merge para unir dos datos, basicamente un join de SQL
    df = df_sales.merge(df_products, on="id_product")
    df["Income"] = df["amount"] * df["price"]
    return df["Income"].sum()

def sales_by_city(df_sales, df_clientes, df_products):
    df = df_sales.merge(df_clientes, on="id_client").merge(df_products, on="id_product")
    df["Income"] = df["amount"] * df["price"]
    return df.groupby("city")["Income"].sum().reset_index()
