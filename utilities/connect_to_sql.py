import pyodbc
import pickle
import numpy
from sklearn import metrics


def connect_sql_server():
    # https://datatofish.com/how-to-connect-python-to-sql-server-using-pyodbc/
    server_name = 'DESKTOP-3ED44OB\SQLEXPRESS'
    database_name = 'shppingDB'

    conn = pyodbc.connect('Driver={SQL Server};'
                          f'Server={server_name};'
                          f'Database={database_name};'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()
    # cursor.execute('[dbo].[UpdatePacketState] @packetId,@stateId,@shippingCompanyId,@shippingStateId')
    # cursor.execute('[dbo].[Top5BestShippingOffers]1')
    # cursor.execute('[dbo].[ShippingActiveCompanyByCompanyFilter]1')
    # cursor.execute('[dbo].[PacketsHistoryFilter] @startDate datetime, @endDate datetime, @maxFloor, @countryId')
    # cursor.execute('[dbo].[PacketLastStateFilter]3')
    cursor.execute('EXEC [dbo].[NewPacket] @sourceId =3 , @destinationId=1 ,@breakable =1, @express =1, @shippingCompanyId =2')
    # cursor.execute('[dbo].[GetCitiesWithPacketsCount]1')

    # cursor.execute('SELECT TOP (1000) [Id],[Name] FROM [shppingDB].[dbo].[PacketState]')

    for row in cursor:
        print(row)
    # conn.commit()


connect_sql_server()
