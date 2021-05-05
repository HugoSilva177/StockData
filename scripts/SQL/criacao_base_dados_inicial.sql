CREATE TABLE stockdata_empresa.dados_empresa
(papel varchar(5) primary key,
 nome_empresa varchar(255),
 setor varchar(255)
);

CREATE TABLE stockdata_empresa.br_investing
(id serial primary key,
 papel varchar(5),
 brinvesting varchar(255),
 brinvesting_noticias varchar(255),
 FOREIGN KEY (papel) REFERENCES stockdata_empresa.dados_empresa(papel)
);

INSERT INTO stockdata_empresa.dados_empresa(papel, nome_empresa, setor)
VALUES('ABEV3', 'Ambev', 'Bebidas'),
('AZUL4', 'Azul', 'Transporte'),
('B3SA3', 'B3', 'Serviços Financeiros'),
('BBAS3', 'Banco do Brasil', 'Bancos'),
('BBDC4', 'Banco Bradesco', 'Bancos'),
('BRKM5', 'CVC Brasil', 'Químicos'),
('CVCB3', 'Cyrela Brazil', 'Viagens e Lazer'),
('CYRE3', 'Eneva', 'Construção Civil'),
('ENEV3', 'Gerdau SA', 'Energia Elétrica'),
('GGBR4', 'Grendene SA', 'Siderugica e Metalurgia'),
('GRND3', 'Itausa', 'Tecidos, Vestuário e Calçados'),
('ITSA4', 'Itausa', 'Bancos'),
('ITUB4', 'Itau Unibanco', 'Bancos'),
('JBSS3', 'JBS', 'Alimentos, Carnes e Derivados'),
('LAME4', 'Lojas Americanas', 'Comércio'),
('LWSA3', 'Locaweb', 'Programas e Serviços'),
('MGLU3', 'Magazine Luiza', 'Comércio'),
('NTCO3', 'Grupo Natura', 'Produtos Uso Pessoal e Limpeza'),
('PCAR3', 'Pão de Açucar', 'Comércio e Distribuição'),
('PETR4', 'Petrobras PN', 'Petróleo, Gás e Biocombustíveis'),
('PETZ3', 'Petz', 'Comércio'),
('RADL3', 'Raia Drogasil', 'Comércio e Distribuição'),
('SUZB3', 'Suzano Papel', 'Madeira e Papel'),
('USIM5', 'Usiminas', 'Siderurgica e Metalurgica'),
('VALE3', 'Vale', 'Mineração'),
('VVAR3', 'Viavarejo', 'Comércio'),
('WEGE3', 'WEG SA', 'Máquinas e Equipamentos')


INSERT INTO stockdata_empresa.br_investing(papel, brinvesting, brinvesting_noticias)
VALUES('ABEV3', 'ambev-pn', 'ambev-pn-news'),
('AZUL4', 'azul-sa-pref', 'azul-sa-pref-news'),
('B3SA3', 'bmfbovespa-on-nm', 'bmfbovespa-on-nm-news'),
('BBAS3', 'brasil-on', 'brasil-on-news'),
('BBDC4', 'bradesco-pn-n1', 'bradesco-pn-n1-news'),
('BRKM5', 'braskem-pna-n1', 'braskem-pna-n1-news'),
('CVCB3', 'cvc-brasil-on', 'cvc-brasil-on-news'),
('CYRE3', 'cyrela-realt-on-nm', 'cyrela-realt-on-nm-news'),
('ENEV3', 'eneva-sa', 'eneva-sa-news'),
('GGBR4', 'gerdau-pn-n1', 'gerdau-pn-n1-news'),
('GRND3', 'grendene-on-nm', 'grendene-on-nm-news'),
('ITSA4', 'itausa-pn-ej-n1', 'itausa-pn-ej-n1-news'),
('ITUB4', 'itauunibanco-pn-edj-n1', 'itauunibanco-pn-edj-n1-news'),
('JBSS3', 'jbs-on-nm', 'jbs-on-nm-news'),
('LAME4', 'lojas-americ-pn-int', 'lojas-americ-pn-int-news'),
('LWSA3', 'locaweb-servicos-de-internet-sa', 'locaweb-servicos-de-internet-sa-news'),
('MGLU3', 'magaz-luiza-on-nm', 'magaz-luiza-on-nm-news'),
('NTCO3', 'natura-on-nm', 'natura-on-nm-news'),
('PCAR3', 'companhia-brasileira-de-distribuica', 'companhia-brasileira-de-distribuica-news'),
('PETR4', 'petrobras-pn', 'petrobras-pn-news'),
('PETZ3', 'pet-center-comercio-e-partcipacoes', 'pet-center-comercio-e-partcipacoes-news'),
('RADL3', 'raiadrogasil-on-nm', 'raiadrogasil-on-nm-news'),
('SUZB3', 'suzano-papel-celulose', 'suzano-papel-celulose-news'),
('USIM5', 'usiminas-pna', 'usiminas-pna-news'),
('VALE3', 'vale-on-n1', 'vale-on-n1-news'),
('VVAR3', 'via-varejo-sa', 'via-varejo-sa-news'),
('WEGE3', 'weg-on-ej-nm', 'weg-on-ej-nm-news')
