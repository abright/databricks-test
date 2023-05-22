# Databricks notebook source
    dbutils.widgets.text('myinput','')

    myinput = dbutils.widgets.get('myinput')

    print(myinput)
    output = 'cell 1 received input: ' + myinput
    print(output)

# COMMAND ----------

    print(output)
    output2 = 'cell 2 received input: ' + output
    print(output2)
    dbutils.notebook.exit({"final_output": output2})
