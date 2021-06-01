name := "read_info_empresa_hdfs"

version := "1.0"

scalaVersion := "2.12.2"

libraryDependencies ++= Seq(
  "org.apache.spark" % "spark-core_2.12" % "2.4.3",
  "org.apache.spark" % "spark-sql_2.12" % "2.4.4"
)

enablePlugins(JavaAppPackaging)

