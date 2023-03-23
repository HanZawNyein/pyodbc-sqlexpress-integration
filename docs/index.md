# Microsoft ODBC driver for SQL Server (Linux)


For full documentation visit [Install the Microsoft ODBC driver for SQL Server (Linux)](https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver16&tabs=ubuntu18-install%2Calpine17-install%2Cdebian8-install%2Credhat7-13-install%2Crhel7-offline).

[Configure development environment for pyodbc Python development](https://learn.microsoft.com/en-us/sql/connect/python/pyodbc/step-1-configure-development-environment-for-pyodbc-python-development?view=sql-server-ver16)
## Microsoft ODBC 17

=== "Ubuntu"

    ```bash
    if ! [[ "16.04 18.04 20.04 22.04" == *"$(lsb_release -rs)"* ]];
    then
        echo "Ubuntu $(lsb_release -rs) is not currently supported.";
        exit;
    fi

    sudo su
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

    curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list > /etc/apt/sources.list.d/mssql-release.list

    exit
    sudo apt-get update
    sudo ACCEPT_EULA=Y apt-get install -y msodbcsql17
    # optional: for bcp and sqlcmd
    sudo ACCEPT_EULA=Y apt-get install -y mssql-tools
    echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
    source ~/.bashrc
    # optional: for unixODBC development headers
    sudo apt-get install -y unixodbc-dev
    ```

## Project Configuration

=== "Ubuntu"
```zsh
python3 -m venv venv
source venv/bin/activate
```

Install Requirements
```zsh
pip3 install pyodbc
```

## Connection

=== "Ubuntu"
```zsh
DRIVER={ODBC Driver 17 for SQL Server};SERVER=host_name,port;DATABASE=db_name;UID=username;PWD=password
```

```py
import pyodbc
__connection_str = f'DRIVER={{{self.DRIVER}}};SERVER={self.SERVER},{self.PORT};DATABASE={self.DATABASE};UID={self.UID};PWD={self.PWD}'
cnxn = pyodbc.connect(__connection_str)
cursor = cnxn.cursor()
cursor.execute(query)
```