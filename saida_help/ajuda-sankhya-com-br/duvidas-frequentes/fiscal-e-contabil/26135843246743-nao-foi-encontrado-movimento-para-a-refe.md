---
id: "26135843246743"
titulo: "Não foi encontrado movimento para a referência"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26135843246743-N%C3%A3o-foi-encontrado-movimento-para-a-refer%C3%AAncia"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:43:09Z"
rotulos: ["Relatórios", "Imobilizado", "Contabilização", "Depreciação", "IMOB_E00037", "Não foi encontrado movimento para a referência", "Erro"]
---

# Não foi encontrado movimento para a referência

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/26135843238551) MENSAGEM**: 

IMOB\_E00037 - Não foi encontrado movimento para a referência

**![Imagem 2: SOLUÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/26135843241751) SOLUÇÃO**:

É preciso ter certeza, que a depreciação do mês para a qual está sendo gerado o lote, já foi de fato executada na rotina  [Calculo da Depreciação Mensal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360053497654-C%C3%A1lculo-da-Deprecia%C3%A7%C3%A3o-Mensal). Para fazer essa verificação, use o [Relatório Contábil do Patrimonial](https://ajuda.sankhya.com.br/hc/pt-br/articles/4447889227415-Relat%C3%B3rios-Cont%C3%A1beis-do-Patrimonial) (Caminho: Imobilizado » Arquivos » Relatórios Contábeis do Patrimonial), que demonstra o valor depreciado no mês em questão[.](https://ajuda.sankhya.com.br/hc/pt-br/articles/4447889227415-Relat%C3%B3rios-Cont%C3%A1beis-do-Patrimonial) Se nessa consulta, no relatório Depreciação mensal analítica, for apresentado os dados e valores da depreciação, de fato há valores a serem contabilizados. Porém, se não houver valores, significa que algo falhou na execução da depreciação mensal e deve ser verificado.

**![Imagem 3: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/26135843240343) CAUSA**:

Ao executarmos a rotina de [Geração de Lote de Depreciação,](https://ajuda.sankhya.com.br/hc/pt-br/articles/1500001593622-Gera%C3%A7%C3%A3o-de-Lote-de-Deprecia%C3%A7%C3%A3o) o sistema realiza uma consulta dos movimentos de depreciação que ainda **não** foram contabilizados para montar o lote contábil e integrar à Contabilidade. Porém, quando o sistema **não** encontra nenhum dado ainda pendente para contabilização, a mensagem é apresentada.
