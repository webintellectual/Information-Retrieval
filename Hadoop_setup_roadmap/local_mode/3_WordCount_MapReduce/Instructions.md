## Writing a WordCount MapReduce application, bundling it, and running it using the Hadoop local mode

- Use snake case only to name the files and folder.
- Specify path of python in .py files <br/>
  #!{python path}

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
