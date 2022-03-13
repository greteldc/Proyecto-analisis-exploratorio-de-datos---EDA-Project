#definición para 
def reorder_columns(dataframe, col_name, position):
    """Reorder a dataframe's column.
    Args:
        dataframe (pd.DataFrame): dataframe to use
        col_name (string): column name to move
        position (0-indexed position): where to relocate column to
    Returns:
        pd.DataFrame: re-assigned dataframe
    """
    temp_col = dataframe[col_name]
    dataframe = dataframe.drop(columns=[col_name])
    dataframe.insert(loc=position, column=col_name, value=temp_col)
    return dataframe
#df = reorder_columns(dataframe=df, col_name='Age', position=0)
#print(df)


#definición para quitarles a los títulos de las columnas el contenido irrelevante y hacerles así más cortos
#es un proceso reiterativo con el mismo patrón => creación definición más adecuada
def shorten_column_titles(list_of_column_headers):
    lista = []
    for i in list_of_column_headers:
        if "_DESCR_NL" in i:
            i = i.replace("_DESCR_NL","")
        if "TX_" in i:
            i = i.replace("TX_", "")
        else:
            i = i
        lista.append(i)
    return lista

def shorten_name_values(column):
    lista = []
    for i in column:
        if "Arrondissement" in i:
            i = i.replace("Arr.")
    else:
        i = i
    lista.append(i)
    return lista

def clarify_name_acc(list_of_column_headers):
    lista = []
    for i in list_of_column_headers:
        if "MS_ACCT_WITH" in i:
            i = i.replace("MS_ACCT", "Nº ACC")
        elif "MS_ACCT" in i:
            i = i.replace("MS_ACCT", "Nº ACC")
        else: 
            i = i
        lista.append(i)
    return lista

#function to extract total number of accidents per year from year-datasheets
def sumar_total_acc_por_ano(lista_acc_por_ano):
    lista = []
    for i in lista_acc_por_ano:
        lista.append(i["Nº ACC"].sum())
    return lista

#function to find duplicate columns (return via list):   - def from https://thispointer.com/how-to-find-drop-duplicate-columns-in-a-dataframe-python-pandas/
def getDuplicateColumns(df):
    duplicateColumnNames = set()
    for x in range(df.shape[1]):
        col = df.iloc[:, x]
        for y in range(x + 1, df.shape[1]):
            otherCol = df.iloc[:, y]
            if col.equals(otherCol):
                duplicateColumnNames.add(df.columns.values[y])
    return list(duplicateColumnNames)