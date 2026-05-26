# Topic :: PySpark::

"""
1 : What is pyspark ?
PySpark is Python API for apache spark ,
used to process and analyze large amount of data very fast across multiple computers

or


"PySpark is the Python API for Apache Spark. It allows you to 
write Python code to process massive amounts of 
data across a cluster of computers simultaneously."

If you try to process a 100 GB or 1 TB file on your laptop using standard Python 
(like basic loops or standard Pandas), your computer will likely freeze 
or run out of memory. PySpark solves this by splitting the 
data into smaller chunks and distributing the
work across multiple machines (or multiple cores on your laptop)


2 : Why Pyspark introduced?

before spark ,hadoop was used, it was very slow because 
it wrote data to disk after every step ..

spark keeps data in memory (ram) making 100 % faster.
pyspark was introduced for python developers could use spark without learning java/scala


3: where to use 

big companies like : netflix ,uber,amazon used in data engineering pipelines ,ml on big data 
ETL jobs,and log processing 


4: when to use?

use pyspark when ur data is too big for pandas 
when we need to process data fast across multiple machines

when working on cloud GCP with databricks ,aws,azure   

5 Syntax: for session



from pyspark.sql import SparkSession
spark = SparkSession.builder \
        .appName("myapp") \
        .getOrCreate()
        
6 spark divides work into 3 ?
Job → Stages → Tasks



Feature,Pandas,PySpark
Data Size,Small to Medium (fits in a single computer's RAM),Massive Big Data (Terabytes/Petabytes)
Execution,Single machine (Single-core by default),Distributed across a cluster (Multi-machine)
Speed,Fast for small datasets; slow/crashes on large data,Optimized for scale; handles massive data efficiently

    
"""


# example code 

from pyspark.sql import SparkSession


# creating entry point (before this there is concept of sparkContext)
spark = SparkSession.builder \
        .appName("Demo") \
                .getOrCreate()


print("Session Created \n")


# we need to create dataframe using spark 



data = [        
        (1,"Prasad","ASD",0),
        (2,"narsimha","architect",250000),
        (3,"Sai Pallavi","Non-It",19999),
        (4,"Adhi","QA",35000),
        (5,"Sharmila","ASD",34000)]



columns = ["id","name","dept","salary"]


# now create df using above data and columns


df = spark.createDataFrame(data, columns)



print("=========data about employee information==========\n")

df.show() # it will print data about df

# print schema 
print(df.printSchema) # it will print about column name respective data types



# names of columns we can use this df.columns 
print(df.columns) 


# suppose we need to select name and dept 


df.select("name","dept").show()



# suppose we need to filter salary 


df.filter("salary >19000").show()



# order by sal


df.orderBy("salary").show()

# group by dept









# reading different data source 


df_employees_csv = spark.read.csv("src/employees.csv")
df_product_csv = spark.read.csv("src/products.csv")
df_sales_csv = spark.read.csv("src/sales.csv")
df_students_json = spark.read \
        .option("multiLine","true")\
        .json("src/students.json")
df_application_logs_txt = spark.read.text("src/application_logs.txt")


print("\n")


print("\ninformation about employee table\n")

df_employees_csv.show()

print("\n information about products\n")
df_product_csv.show()


print("\n information about sales\n")
df_sales_csv.show()


print("\n information about the application logs\n")
df_application_logs_txt.show()


print("\n information about the student json file\n")

df_students_json.show()


# checking who get high marks 

top_students_marks = df_students_json.filter("marks")

print("\n printing top student marks in table\n")
top_students_marks.show()