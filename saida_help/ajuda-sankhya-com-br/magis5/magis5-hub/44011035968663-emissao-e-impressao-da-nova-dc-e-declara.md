---
id: "44011035968663"
titulo: "Emissão e impressão da nova DC-e (Declaração de Conteúdo Eletrônica)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011035968663-Emiss%C3%A3o-e-impress%C3%A3o-da-nova-DC-e-Declara%C3%A7%C3%A3o-de-Conte%C3%BAdo-Eletr%C3%B4nica"
trilha: "Magis5 > Magis5 HUB"
atualizado_em: "2026-10-05T18:53:48Z"
rotulos: ["sync_hc", "magis5", "sync_hash_9c8a46ca84d5", "magis5_210627925922"]
---

# Emissão e impressão da nova DC-e (Declaração de Conteúdo Eletrônica)

## Neste guia, você encontrará orientações completas para emitir e imprimir a nova Declaração de Conteúdo Eletrônica (DC-e).

---

A **DC-e (Declaração de Conteúdo Eletrônica)** é um documento fiscal que passa a ser exigido pelo governo a partir de 06 de abril de 2026. Ela substitui a antiga Declaração de Conteúdo que não possuía valor fiscal.

A **DC-e (Declaração de Conteúdo Eletrônica)** foi criada para atender especificamente dois tipos de emissores:

1. **Pessoas físicas (PF);**
2. **Pessoas jurídicas não contribuintes do ICMS (PJ não contribuinte).**

Para esses perfis, a DC-e substitui a antiga Declaração de Conteúdo, passando a ter validade fiscal e exigindo emissão por meio da SEFAZ, com geração de chave de acesso para consulta e rastreabilidade.

Já para os demais casos, especialmente empresas contribuintes do ICMS a orientação do governo é a emissão da **NF-e (Nota Fiscal Eletrônica)**, que continua sendo o documento fiscal adequado para acobertar a circulação de mercadorias.

### O que essa nova mudança impacta?

Nos casos de vendas realizadas por meio dos canais de venda **que permitem cadastro como pessoa física (PF) ou pessoa jurídica não contribuinte do ICMS (PJ não contribuinte)**, a responsabilidade pela emissão da **DC-e** deve ser do próprio marketplace.

O mesmo se aplica às integrações logísticas, a responsabilidade pela geração da **DC-e** é das próprias plataformas.

### Emissão da DC-e por meio de Integrações Logísticas

Atualmente, no **Magis5 HUB**, já é possível realizar a impressão da DC-e em conjunto com a [integração dos Correios](https://ajuda.sankhya.com.br/como-integrar-o-correios?hsLang=pt-br). Quando há um contrato dos Correios devidamente integrado, a DC-e é gerada pelos próprios Correios e disponibilizada para impressão pelo Magis5 HUB.

Exemplo de **DC-e emitida via Correios**, apresentada no formato de **DACE Resumida (Documento Auxiliar da Declaração de Conteúdo Eletrônica)**

**![Captura de tela 2026-04-07 175421](https://ajuda.sankhya.com.br/hc/article_attachments/44011077272855)

💡 Caso a Declaração de Conteúdo ainda esteja sendo impressa no modelo antigo, sem valor fiscal, é necessário abrir um chamado junto ao [Suporte](https://ajuda.sankhya.com.br/como-abrir-um-suporte-por-bate-papo-na-magis5?hsLang=pt-br) para solicitar a ativação da impressão no modelo DC-e.**

⚠️ **Mandaê e Intelipost:

Até o momento, não há confirmação sobre a disponibilidade da emissão da DC-e nessas plataformas.**

### Emissão da DC-e por meio de Integrações com Canais de Venda.

**Mercado Livre e Amazon**

Essas plataformas já são responsáveis pela geração da **DC-e**; portanto, **deve ser utilizada a versão gerada pelo canal de venda**. Atualmente, essas plataformas **não disponibilizam a emissão da DC-e via API** (uma **API** é basicamente uma “ponte” que permite que dois sistemas **conversem e troquem informações automaticamente**).

Dessa forma, o seller precisará **acessar o Seller Central** (Mercado Livre ou Amazon) para **gerar e imprimir o documento corretamente**.

💡No Magis5 HUB, a declaração de conteúdo impressa seguirá o modelo antigo, sem valor fiscal, **exceto nos casos de integração com os Correios.**

⚠️ **Os demais canais de venda:

Até o momento, não há confirmação sobre a disponibilidade da emissão da DC-e nessas plataformas.**

### Impressão da DC-e pelo Magis5 HUB

Para que a **DC-e seja impressa corretamente pelo Magis5 HUB** em canais com **integração ativa dos Correios**, é necessário **ativar a opção** **“Imprimir nota fiscal/declaração de conteúdo”** na aba **“Notas Fiscais”** do canal de venda, localizada ao final da página.

![Imagem 2: Para que a DC-e seja impressa corretamente pelo Magis5 HUB em canais com integração ativa dos Correios , é necessário…](https://ajuda.sankhya.com.br/hc/article_attachments/44011047616535)
