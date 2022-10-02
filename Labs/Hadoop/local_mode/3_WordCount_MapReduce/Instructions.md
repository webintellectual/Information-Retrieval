## Writing a WordCount MapReduce application, bundling it, and running it using the Hadoop local mode

- Use snake case only to name the files and folder.
- Specify path of python in .py files <br/>
  #!{python path}
- Perform this task in your own separate directory if you are a collabrator of this Git and GitHub repo <br/>

Command to run mapReduce job:

```
$ $HADOOP_HOME/bin/hadoop jar \
$HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.10.2.jar \
-file {mapper.py file path} -mapper Mapper.py \
-file {reducer.py file path} -reducer reducer.py \
-input {input.txt file path} \
-output {new directory path for output}
```

Note: folder of output should not be existing already.

The output directory will have a file named part-r-XXXXX, which will have the count of each word in the document. Congratulations! You have successfully run your first MapReduce program.

```
$ cat {output folder path}/part*
```
