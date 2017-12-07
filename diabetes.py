import pandas

##### IMPORT CSV AND PREPROCESSING
df = pandas.read_csv("export-v10_3-201711-172812.csv")
df = df.fillna(0)

def make_entries(df, v_entry, value1, value2=None):
    for _, row in df.iterrows():
        
        timestamp_date_day = row['date'][0:2]
        timestamp_date_month = row['date'][3:5]
        timestamp_date_year = "20"+row['date'][6:8]
        
        timestamp_time = row['time']
        timestamp = "%s.%s.%s-%s" %(timestamp_date_year,timestamp_date_month, timestamp_date_day , timestamp_time)
        value = row[value1]
        if value2 == None:
            entry = "%svaultEntries.add(new VaultEntry(VaultEntryType.%s, TimestampUtils.createCleanTimestamp(\"%s\", \"yyyy.MM.dd-HH:mm\"), %s));" %(timestamp, v_entry, timestamp, value)
            data_entries.append(entry)
        else:
            value_2 = row[value2]
            entry = "%svaultEntries.add(new VaultEntry(VaultEntryType.%s, TimestampUtils.createCleanTimestamp(\"%s\", \"yyyy.MM.dd-HH:mm\"), %s, %s));" %(timestamp, v_entry, timestamp, value,value_2)
            data_entries.append(entry)



#### FILTER DATAFRAME BY DATE
df = df.loc[df['date'] == '05.06.17']

#### FILTER DATAFRAME BY ANNOTATION AND VAULT_ENTRY_TYPE
vet1 = 'SLEEP_LIGHT'
vet2 =  'SLEEP_DEEP'
df1 = df.loc[df['sleepAnnotation'] == vet1] 
df2 = df.loc[df['sleepAnnotation'] == vet2] 


##### SPECIFY COLUMNS
data_entries = []

##### ENTER VAULT ENTRY TYPE, VALUE1 AND OPTIONALLY VALUE2
make_entries(df1, vet1 ,"sleepValue", "cgmValue")
make_entries(df2, vet2,"sleepValue")


#### SORT ENTRIES AND CUT OFF PREPENDED TIMESTAMP
data_entries.sort()
for e in data_entries:
    print(e[16:])