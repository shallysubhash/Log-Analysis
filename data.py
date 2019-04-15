import psycopg2
dbName = "news"

query1 = """SELECT count(*) AS num ,articles.title FROM ARTICLES 
INNER JOIN log ON LOG.PATH LIKE 
concat('%', articles.slug, '%') 
GROUP BY articles.title 
order by num desc limit 3"""

query2 = """SELECT count(*) AS Num ,authors.name FROM ARTICLES 
INNER JOIN log ON LOG.PATH 
LIKE concat('%', articles.slug, '%') 
JOIN authors on articles.author = authors.id 
  GROUP BY authors.name order by Num desc"""

query3 = """select
sum(case log.status when '200 OK' then 0 else 1 end) 
/count(*)::float * 100 as Per, 
date(time)  from log group by date(time) 
having sum(case log.status when '200 OK' 
then 0 else 1 end) /count(*)::float * 100 >1"""


def QueryResult(query):
    db = psycopg2.connect(database=dbName)
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result


def PrintResult(rows, title):
    print ("\t",title)
    for row in rows:
        print ( "\t", row[1],'\t --- ', row[0], "views")


def PrintAuthorResult(rows, title):
    print ("\t",title)
    for row in rows:
        print ( "\t", row[1],'\t --- ', round(row[0],2), "% errors")
        

PrintResult(QueryResult(query1), 'Most popular three articles of all time?')
print("===============================================================")
PrintResult(QueryResult(query2), 'Most popular authors of all time?')
print("===============================================================")
PrintAuthorResult(QueryResult(query3), 'Days did more than 1% of requests lead to errors')