How to submit Spark applications:https://spark.apache.org/docs/latest/submitting-applications.html
1.Launching Applications with spark-submit with spark-submit:
./bin/spark-submit \
  --class <main-class> \
  --master <master-url> \
  --deploy-mode <deploy-mode> \
  --conf <key>=<value> \
  ... # other options
  <application-jar> \
  [application-arguments]

Some of the commonly used options are:

--class: The entry point for your application (e.g. org.apache.spark.examples.SparkPi)
--master: The master URL for the cluster (e.g. spark://23.195.26.187:7077)
--deploy-mode: Whether to deploy your driver on the worker nodes (cluster) or locally as an external client (client) (default: client) †
--conf: Arbitrary Spark configuration property in key=value format. For values that contain spaces wrap “key=value” in quotes (as shown).
application-jar: Path to a bundled jar including your application and all dependencies. The URL must be globally visible inside of your cluster, for instance, an hdfs:// path or a file:// path that is present on all nodes.
application-arguments: Arguments passed to the main method of your main class, if any

# Run on a YARN cluster
export HADOOP_CONF_DIR=XXX
./bin/spark-submit \
  --class org.apache.spark.examples.SparkPi \
  --master yarn \
  --deploy-mode cluster \  # can be client for client mode
  --executor-memory 20G \
  --num-executors 50 \
  /path/to/examples.jar \
  1000

# Run a Python application on a Spark standalone cluster
# $SPARK_HOME defined in ~/.profile
$SPARK_HOME/bin/spark-submit \
  --master spark://<HOSTNAME>(e.g,207.184.161.138):7077 \
  examples/src/main/python/pi.py \
  1000


