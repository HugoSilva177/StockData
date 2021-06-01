package com.hdfs.stockdata

import org.apache.spark.{SparkConf, SparkContext}
import org.apache.spark.sql.{DataFrame, SQLContext}

object ReadInfoEmpresaHDFS extends App {
  
    val conf: SparkConf = new SparkConf().setMaster("local").setAppName("fundamentus-info-empresa")
    val sc: SparkContext = new SparkContext(conf)
    val sqlContext: SQLContext = new SQLContext(sc)
    readParquet(sqlContext)
  
    def readParquet(sqlContext: SQLContext) = {
      val newDataDF = sqlContext.read.parquet("hdfs://172.17.177.40:9000/user/hadoopuser/fundamentus/detalhes/info_empresa") 
      newDataDF.show()
  }
  
}
