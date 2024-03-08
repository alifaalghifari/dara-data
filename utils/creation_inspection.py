import pandas as pd
import io

class CreationInspection:
    def __init__(self, data):
        self.data = data
        # self.filename = filename

    # DATAFRAME TO STRING
    def df_to_str(self, data):
        buffer = io.StringIO(initial_value=' tes',newline='\n')  
        data.info(buf=buffer)
        data_str = buffer.getvalue()
        return data_str
    
    # DATAFRAME TO HTML
    def df_to_html(self, data):
        data_html = data.to_html(classes='data')
        return data_html
    
    # READ CSV
    def read_csv(self):
        return pd.read_csv(self.data)
    
    # DATA CREATE
    def data_create(self):
        data = pd.read_csv(self.data).head(5)
        data_create = self.df_to_html(data)
        return data_create, "df = pd.read_csv('" + self.data.filename + "')"
    
    # DATA INFO
    def data_info(self):
        data = self.read_csv()
        data_info = self.df_to_str(data)
        return data_info, "df.info()"
    
    # DATA HEAD
    def data_head(self, n):
        data = self.read_csv()
        head_data = data.head(n)
        data_html = self.df_to_html(head_data)
        return data_html, "df.head(" + str(n) + ")"
    
    # DATA TAIL
    def data_tail(self, n):
        data = self.read_csv()
        tail_data = data.tail(n)
        data_html = self.df_to_html(tail_data)
        return data_html, "df.tail(" + str(n) + ")"
        
def read_csv(data, num = 5):
    data = pd.read_csv(data)

    # select data
    data = data.head()

    # tables = [data.to_html(classes='data')]

    return data