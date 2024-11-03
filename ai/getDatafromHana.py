from hdbcli import dbapi

try :
    conn = dbapi.connect(
        address='1dea6918-8439-4491-9903-b3b234cd01f2.hna2.prod-eu10.hanacloud.ondemand.com',
        port=443,
        user='DBADMIN',
        password='Welcome1',
)
except dbapi.Error as er:
    print('Connect failed, exiting')
    print(er)
    exit()

cursor = conn.cursor()

#выгрузка заявок из таб. HR_USB_2QMODEL_JOBDESCRIPTIONS
sqlCommandJob= "SELECT * FROM 5E9E1FB36AF148F39F2AA9F64D1529B9.HR_USB_2QMODEL_JOBDESCRIPTIONS;"
cursor.execute(sqlCommandJob, ())
dbJobDescription = cursor.fetchall()
listOfJobDescription = []

for row in dbJobDescription:
    listOfJobDescription.append(str(row[1:])) #без id

#пример ключевых слов
keywordList = [
    "Специалист MES",
    "Разработчик",
    "сектор поддержки MES",
    "бизнес-процессы",
    "прием заказов",
    "планирование производства",
    "оперативное планирование",
    "учет производства",
    "качество продукции",
    "складские операции",
    "нормирование операций",
    "PHP разработка",
    "OOП",
    "SQL",
    "Git",
    "Laravel",
    "CSS",
    "SASS",
    "LESS",
    "JavaScript",
    "Vue",
    "web socket",
    "Bootstrap",
    "Ajax",
    "UI/UX",
    "паттерны",
    "серверы",
    "сети",
    "информационная безопасность",
    "анализ бизнес-процессов",
    "оптимизация процессов",
    "разработка документации",
    "сбор данных",
    "визуализация данных",
    "металлургия",
    "технические задания",
    "SDLC",
    "тестирование",
    "интеграция систем",
    "презентации",
    "обучение пользователей",
    "техническая документация",
    "Microsoft Office 365",
    "Agile",
    "Intermediate English",
    "АСУТП",
    "консалтинг",
    "внедрение систем"
]

#вставка ключивых слов в таб. HR_USB_2QMODEL_KEYWORDS
valueKeywords = ",".join(f"'{keyword}'" for keyword in keywordList)
jobID = dbJobDescription[0][1]
jobTitle = dbJobDescription[0][1]
sqlCommandKey = "INSERT INTO 5E9E1FB36AF148F39F2AA9F64D1529B9.HR_USB_2QMODEL_KEYWORDS (JOB_ID,KEYWORDS,JOB_TITLE_JOB_ID) VALUES (?,?,?);"
cursor.execute(sqlCommandKey, (jobID,valueKeywords,jobTitle))

cursor.close()
conn.close()