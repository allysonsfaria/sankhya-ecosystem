---
id: "360044510613"
titulo: "Como configurar um evento para compor a base de calculo da GRRF?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044510613-Como-configurar-um-evento-para-compor-a-base-de-calculo-da-GRRF"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:33:24Z"
rotulos: ["#criadoRoger", "#revisadohugnei", "Configuração", "Eventos", "Financeiro", "Folha de Pagamento", "GRRF", "Compor Bases de Cálculo", "Base de cálculo GRRF", "Configurar evento", "FGTS"]
---

# Como configurar um evento para compor a base de calculo da GRRF?

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18856741160599) SOLUÇÃO:**

![Imagem 2: Acesse: MGEPessoal >Arquivos > Bases de cálculo, verifique a existência das bases informadas abaixo e se todas elas…](https://ajuda.sankhya.com.br/hc/article_attachments/18856798467351) Acesse: MGEPessoal >Arquivos > Bases de cálculo, verifique a existência das bases informadas abaixo e se todas elas estão devidamente identificadas:

- **1810 - BASE CAMPO 25 GRRF** - Identificação: 5 - Base GRRF Mês Anterior à Rescisão
  **1825 - BASE CAMPO 25 MÊS ANTERIOR** - Identificação: 1 - Bases Auxiliares
- **1811 - BASE CAMPO 26 GRRF** - Identificação: 6 - Base GRRF Mês da Rescisão
  **1826 - BASE FGTS MÊS RESCISÃO** - Identificação: 1 - Bases Auxiliares
- **1812 - BASE CAMPO 27 GRRF** - Identificação: 5 - Base GRRF Indenizações
  **1827 - BASE FGTS VERBAS INDENIZ** - Identificação: 1 - Bases Auxiliares

As bases acima são pares, portanto o evento deve compor, de acordo com sua configuração, as duas bases.

![Imagem 3: Acesse: Arquivos > Eventos, escolha o evento desejado. Acesse a aba: Incidência Bases GRRF.](https://ajuda.sankhya.com.br/hc/article_attachments/18856798469015) Acesse: Arquivos > Eventos, escolha o evento desejado.  Acesse a aba: Incidência Bases GRRF.

- **Mês Anterior à Rescisão [Marcado]:**Com esta marcação, o valor do evento irá compor o campo **25 da GRRF**, destinado à informação da remuneração + 13ª salário paga, devida ou creditada ao trabalhador no mês anterior ao da competência da rescisão.
- **Mês da Rescisão [Marcado]:**Com esta marcação, o valor do evento irá compor o campo **26 da GRRF**, destinado à informação da remuneração + 13ª salário paga, devida ou creditada ao trabalhador no mês da rescisão.
- **Indenizações [Marcado]:**Com esta marcação, o valor do evento irá compor o campo **27 da GRRF**, destinado à informação da remuneração + 13ª Salário devido ao trabalhador, a título de aviso prévio indenizado exclusivamente

![Imagem 4: Indenizações (Marcado) : Com esta marcação, o valor do evento irá compor o campo 27 da GRRF , destinado à informação da…](https://ajuda.sankhya.com.br/hc/article_attachments/18856798478231)

![Imagem 5: Acesse a aba: Bases de cálculo, a configuração de composição de base, pode ser conferida nesta aba.](https://ajuda.sankhya.com.br/hc/article_attachments/18856741182999) Acesse a aba: Bases de cálculo, a configuração de composição de base, pode ser conferida nesta aba.

![Imagem 6: Acesse a aba: Bases de cálculo, a configuração de composição de base, pode ser conferida nesta aba.](https://ajuda.sankhya.com.br/hc/article_attachments/360062083814)

As bases 1810 - BASE CAMPO 25 GRRF, 1811 - BASE CAMPO 26 GRRF e 1812 - BASE CAMPO 27 GRRF, por possuírem identificação, serão incluídas automaticamente nessa aba e serão utilizadas para a geração da guia da GRRF que será integrada com o financeiro.

As bases 1825 - BASE CAMPO 25 MÊS ANTERIOR, 1826 - BASE FGTS MÊS RESCISÃO e 1827 - BASE FGTS VERBAS INDENIZ, por serem 'Bases Auxiliares', devem ser incluídas manualmente, no botão + conforme os pares informados no início, e serão utilizadas pelo evento 990 - MULTA FGTS.
