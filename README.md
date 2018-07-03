# Coding Task
Reading data from an API, saving to a database, and compiling the results into a spreadsheet, email the spreadsheet to a specified email address.

Data Source:
Event Data: https://eonet.sci.gsfc.nasa.gov/api/v2.1/events

Running Configuration

1. Run data_processing.py, make sure you have changed "save_path" to your local path.
2. Run event_database.py, make sure you set "work_path" correctly.
3. Run email_send.py, please set csv file path correctly.
4. In email_send.py, I used SendCoud email API to send target emails. You need to have your name and email address in this function. 
    
    
         save_path = '/Users/dangchong/Desktop/coding_task'
         work_path = '/Users/dangchong/Desktop/coding_task'
         file_path = "/Users/dangchong/Desktop/coding_task/event.csv"
         send_email('your_name', 'email_address')
		 
You can use SQLite to open the event.db file, also you can write SQL queries in it.

If comes error like  "table event already exists", delete that file and run again.

