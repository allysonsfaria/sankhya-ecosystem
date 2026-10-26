---
id: "30769824971031"
titulo: "Crédito do Trabalhador (eConsignado): o que é e como funciona"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30769824971031-Cr%C3%A9dito-do-Trabalhador-eConsignado-o-que-%C3%A9-e-como-funciona"
trilha: "Manual do Produto > Pessoas+ > Crédito do Trabalhador"
atualizado_em: "2026-09-27T18:44:32Z"
rotulos: ["eSocial", "Folha de Pagamento", "Lançamento de Movimento", "empréstimo consignado", "cédito eConsignado", "eConsignado", "Crédito do trabalhador", "crédito do trabalhador MGE", "Domicílio Eletrônico Trabalhista", "FGTS Digital", "Pessoal+", "Crédito Consignado", "Empréstimo"]
---

# Crédito do Trabalhador (eConsignado): o que é e como funciona

```
 Versão disponível: a partir da 5.31.0 (Pessoal+) / sanEsocial 3.11
```

O crédito do trabalhador eConsignado foi criado pelo governo para tornar mais acessível o empréstimo ao trabalhador com taxas reduzidas, oferecendo maior segurança tanto para os trabalhadores quanto para os bancos, pois, como as parcelas são descontadas diretamente da folha de pagamento, o risco de inadimplência diminui e, com a digitalização do processo por meio da Carteira de Trabalho Digital (CTPS Digital), a solicitação e aprovação do empréstimo se tornaram mais rápidas e seguras.

Além disso, essa modalidade de empréstimo foi integrada ao eSocial para garantir que as empresas registrem e informem corretamente os valores descontados, seguindo as regras oficiais.

O fluxo para **a solicitação do crédito eConsignado** ocorrerá da seguinte maneira:

| ![Imagem 1: O fluxo para a solicitação do crédito eConsignado ocorrerá da seguinte maneira:](https://ajuda.sankhya.com.br/hc/article_attachments/42310420831511) | 1. **Colaborador**: |
| --- | --- |
| - acessa a CTPS Digital; - simula o empréstimo; - envia a proposta ao banco. |

| ![Imagem 2: envia a proposta ao banco.](https://ajuda.sankhya.com.br/hc/article_attachments/42310436783895) | 2. **Banco**: |
| --- | --- |
| - analisa a proposta considerando a margem de consignação no eSocial; - aprova e faz o contrato do empréstimo. |

| ![Imagem 3: aprova e faz o contrato do empréstimo.](https://ajuda.sankhya.com.br/hc/article_attachments/42310420833047) | 3. **Empresa**: |
| --- | --- |
| - recebe a notificação do DET (Domicílio Eletrônico Trabalhista) para acessar o Portal Emprega Brasil; - no portal, consulta o extrato consolidado dos empréstimos consignados; - pode baixar o arquivo com os dados para realizar o lançamento do empréstimo na folha de pagamento do colaborador; - importa o arquivo no sistema; - realiza o cálculo da folha mensal ou rescisão com o desconto; - envia o evento correspondente ao desconto ao eSocial. |

| ![Imagem 4: envia o evento correspondente ao desconto ao eSocial.](https://ajuda.sankhya.com.br/hc/article_attachments/42310436785047) | 4. **eSocial**: |
| --- | --- |
| - envio da rubrica com natureza 9253 e o código de FGTS 31 pelo evento S-1010; - envio do desconto da parcela do empréstimo através dos eventos S-1200/S-2299 ou S-2399.   **Nota:** o eSocial Simplificado (MEI, Segurado Especial e Doméstico), o desconto ocorre automaticamente. |

| ![Imagem 5: Nota: o eSocial Simplificado (MEI, Segurado Especial e Doméstico), o desconto ocorre automaticamente.](https://ajuda.sankhya.com.br/hc/article_attachments/42310420834839) | 5. **Portal FGTS Digital**: |
| --- | --- |
| - emite a GFD (Guia de Recolhimento Digital) mensal com os valores das parcelas dos empréstimos informadas ao eSocial;   ![Imagem 6: A empresa deve pagar a GFD via PIX.](https://ajuda.sankhya.com.br/hc/article_attachments/42310436791831) A empresa deve pagar a GFD via PIX. |

| ![Imagem 7: A empresa deve pagar a GFD via PIX.](https://ajuda.sankhya.com.br/hc/article_attachments/42310420836247) | 6. **Caixa Econômica Federal**: |
| --- | --- |
| - recebe o pagamento da GFD e repassa as parcelas aos bancos contratados. |

No Pessoal+, a funcionalidade do crédito do Trabalhador (**eConsignado**) permite que o departamento pessoal registre esses empréstimos de forma estruturada, garantindo que os descontos sejam aplicados corretamente na folha de pagamento e enviados ao eSocial conforme as exigências legais.

Acesse os links abaixo para conhecer as funcionalidades desta rotina.

| [Lançamento do Crédito do Trabalhador no Pessoal+](https://ajuda.sankhya.com.br/hc/pt-br/articles/35831517422871) |
| --- |
| [Como consultar a Tabela 37 – Instituições Financeiras para Empréstimo Consignado do eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/35647758894231) |
| [Como emitir guia FGTS apenas com Crédito do Trabalhador](https://ajuda.sankhya.com.br/hc/pt-br/articles/35317056373911) |
| [Como consultar empréstimo Crédito do Trabalhador](https://ajuda.sankhya.com.br/hc/pt-br/articles/34382673779735) |
| [Reprocessamento do Crédito do Trabalhador](https://ajuda.sankhya.com.br/hc/pt-br/articles/36386300103063) |
| [FAQ - Dúvidas Frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/35835468147735) |
| [Mensagens de erros e advertências do Crédito do Trabalhador](https://ajuda.sankhya.com.br/hc/pt-br/articles/35679033606551) |

![Imagem 8: Para saber mais, acesse a Documentação oficial sobre o Crédito do trabalhador e o Manual Operacional do Empregador .](https://ajuda.sankhya.com.br/hc/article_attachments/35835877312535) Para saber mais, acesse a [Documentação oficial sobre o Crédito do trabalhador](https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/credito-do-trabalhador) e o [Manual Operacional do Empregador](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica/manual-operacional-do-empregador-programa-credito-do-trabalhador-v2-16-05-25.pdf).
