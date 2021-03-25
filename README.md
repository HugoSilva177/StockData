# StockData

O projeto StockData tem como objetivo fazer a coleta de informações de uma empresa pelo seu código BVMF (papel de ações negociada na Bovespa) de diversas fontes diferentes.
Após a coleta o intuito é que os dados sejam pré formatados, organizados, fornecidos e utilizados para análise e aprendizagem de máquina.


<b>Processo de ETL (Extract, Transform and Load):</b>
  *  Extract: tendo diversas fontes como banco de dados, planilhas e principalmente Web Scraping.
      * Web Scraping será feito em sites especificos: em busca de informações da empresa como dados financeiros, balanços, DRE, cotações, oscilações e notícias sobre a empresa.
  * Transform: todas informações serão pré processadas e formatadas antes do armazenamento.
  * Load: após o processo de 'Transform' as informações serão salvas no MongoDB para processamento em real-time ou near real-time e no Hadoop HDFS no formato parquet para processamento offline.


<b>Tecnologias utilizadas:</b>
  * Python: processo de ETL, Web Scraping, interação com base de dados e hadoop
  * MongoDB: armazenamento dos dados
  * Hadoop HDFS: armazenamento dos dados
  * Vagrant: criação de máquinas virtuais para o cluster Hadoop
  * Ansible: provisionamento da VMs criadas pelo Vagrant
  * Airflow: gerenciamento de fluxo de execução do processo de ETL
  * Kafka: mensageria entre os microsserviços
  * Docker: arquitetura de microsserviços do projeto
  * Git: versionamento do projeto
  
