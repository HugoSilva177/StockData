# StockData (projeto em desenvolvimento)

O projeto StockData tem como objetivo fazer a coleta de informações de uma empresa pelo seu código BVMF de diversas fontes diferentes.
Após a coleta o intuito é que os dados sejam pré formatados, organizados, fornecidos e utilizados para análise e aprendizagem de máquina.
Resumidamente, o projeto trata de um processo completo de ETL de dados relevantes de empresas com o capital aberto e papel 
negociado na Bolsa de Valores brasileira B3.

<b>Microservices:</b>
  * web_scraping: scraping feitos em páginas HTML.
  * extract_transform_load: processo de extract, transform e load dos dados resultantes do Web Scraping
e outras fontes.
  * kafka_docker e mongodb_docker: serviços essenciais como Kafka e MongoDB executando em containers.
  * hadoop_cluster_vm: Hadoop HDFS executando em máquinas virtuais Linux.

<b>Serviço de Web Scraping:</b>
  * Web Scraping está sendo feito em páginas HTML do site fundamentus e br.investing.
    * Buscando informações da empresa como dados financeiros, balanços, DRE, cotações, oscilações e notícias sobre a empresa.
  * Após o processo de Web Scraping os dados são enviados em forma de mensagem utilizando
o Kafka para o serviço de ETL.

<b>Serviço de ETL (Extract, Transform and Load):</b>
  * Extract: tendo diversas fontes como banco de dados, planilhas e principalmente Web Scraping.
  * Transform: todas informações serão pré processadas e formatadas antes do armazenamento.
  * Load: após o processo de 'Transform' as informações serão salvas no MongoDB para processamento em real-time ou near real-time e no Hadoop HDFS no formato parquet para processamento offline.

<b>Tecnologias utilizadas:</b>
  * Python: processo de ETL, Web Scraping, comunicação com base de dados e hadoop
  * MongoDB: armazenamento dos dados
  * Hadoop HDFS: armazenamento dos dados
  * Vagrant: criação de máquinas virtuais para o cluster Hadoop
  * Ansible: provisionamento da VMs criadas pelo Vagrant
  * Airflow: gerenciamento de fluxo de execução do processo de ETL
  * Kafka: sistema de mensageria entre os microservices
  * Docker: criação de containers para arquitetura de microservices
  * Git e Github: versionamento do projeto
  
