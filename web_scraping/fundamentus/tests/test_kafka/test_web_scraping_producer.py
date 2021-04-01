from web_scraping.fundamentus.src.kafka.WebScrapingProducer import WebScrapingProducer


class TestWebScrapingProducer:

    def instancia_web_scraping_producer(self):
        return WebScrapingProducer()

    def test_deve_criar_mensagem_em_um_topic_e_retornar_resultado(self):
        pass