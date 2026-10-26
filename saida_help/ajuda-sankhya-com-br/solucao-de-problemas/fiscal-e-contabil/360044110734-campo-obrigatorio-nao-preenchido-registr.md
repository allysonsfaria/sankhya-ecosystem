---
id: "360044110734"
titulo: "Campo obrigatório não preenchido - Registro I050 - Campo COD NAT"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110734-Campo-obrigat%C3%B3rio-n%C3%A3o-preenchido-Registro-I050-Campo-COD-NAT"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:53:13Z"
rotulos: ["#criadoRoger", "#revisadojunior", "Configuração", "ECD", "Contabilidade", "Natureza", "Plano de Contas", "Campo obrigatório não preenchido - COD NAT", "Erro ao validar ECD", "Preencher tipo de conta no Plano de Contas", "Erro"]
---

# Campo obrigatório não preenchido - Registro I050 - Campo COD NAT

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16979737733271) MENSAGEM:**

Campo obrigatório não preenchido - Registro I050 - Campo COD NAT.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16979767503127) SITUAÇÃO:**

Ao validar o arquivo ECD o seguinte erro é apresentado do validador.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16979767506071)SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 4: Acesse: Contabilidade » Cadastros » Plano de Contas](https://ajuda.sankhya.com.br/hc/article_attachments/16979737739543) Acesse: Contabilidade » Cadastros » Plano de Contas

Selecione as contas analíticas, conforme foi criticado na descrição do erro:

Exemplo: |**I050**|01012015| |A|7|**1.1.02.04.03.02.00001**|1.1.02.04.03.02|**(-) Amort Acum Licença Softwares/Sistema**

- Aba: **"Geral"**
- Campo **"Grupo de Conta"**: selecione conforme orientação do seu Contador
- Faça o ajuste para todas as contas, que apresentaram erro no relatório do PVA.

![Imagem 5: Acesse: Contabilidade » Conexão » ECD » Geração de Arquivo - ECD:](https://ajuda.sankhya.com.br/hc/article_attachments/16979737740695) Acesse: Contabilidade » Conexão » ECD » Geração de Arquivo - ECD:

- Gere o arquivo novamente e faça uma nova validação.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16979767511575)CAUSA:**

Ocorre quando as contas declaradas no arquivo ECD estão sem a informação do tipo de Conta, no cadastro de Plano de Contas.
