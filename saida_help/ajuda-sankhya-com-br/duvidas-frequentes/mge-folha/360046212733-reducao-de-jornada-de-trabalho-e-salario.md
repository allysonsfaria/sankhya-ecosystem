---
id: "360046212733"
titulo: "Redução de jornada de trabalho e salário - MP936. Saiba Mais!"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360046212733-Redu%C3%A7%C3%A3o-de-jornada-de-trabalho-e-sal%C3%A1rio-MP936-Saiba-Mais"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:34:40Z"
rotulos: ["Contrato", "Folha", "eSocial", "Configuração Funcionários", "Redução de Jornada e Salário - MP936", "MP936"]
---

# Redução de jornada de trabalho e salário - MP936. Saiba Mais!

**[MEDIDA PROVISÓRIA Nº 936, DE](http://legislacao.planalto.gov.br/legisla/legislacao.nsf/Viw_Identificacao/mpv%20936-2020?OpenDocument)**   [1º](http://legislacao.planalto.gov.br/legisla/legislacao.nsf/Viw_Identificacao/mpv%20936-2020?OpenDocument)   **[DE ABRIL DE 2020](http://legislacao.planalto.gov.br/legisla/legislacao.nsf/Viw_Identificacao/mpv%20936-2020?OpenDocument)**

São medidas do Programa Emergencial de Manutenção do Emprego e da Renda:

I - o **pagamento de Benefício** Emergencial de Preservação do Emprego e da Renda;

II - a **redução proporcional de jornada** de trabalho **e de salários**; e

III - a **suspensão temporária** do contrato de trabalho.

Fonte: <http://www.planalto.gov.br/ccivil_03/_Ato2019-2022/2020/Mpv/mpv936.htm>

**Pré-Requisitos:**

- Versão 4.32.0.34 ou superior
- Versão 4.33.0.16 ou superior

**Parametrizações necessárias para a redução proporcional de jornada de trabalho e de salários:**

![Imagem 1: Tela de cadastro “Força Maior”, acessada através do Menu Arquivos > Cadastros > Força Maior:](https://ajuda.sankhya.com.br/hc/article_attachments/19150656283543) Tela de cadastro “Força Maior”, acessada através do Menu **Arquivos > Cadastros > Força Maior:**

Atenção!!
Todos os cadastros de redução deverão ser realizados pela rotina de Força Maior:

![Imagem 2: Atenção!! Todos os cadastros de redução deverão ser realizados pela rotina de Força Maior:](https://ajuda.sankhya.com.br/hc/article_attachments/19150656284823)

O usuário deverá preencher os seguintes campos:

- **Empresa:** para qual empresa valerá a regra
- **Sindicato:** para qual sindicato valerá a regra

Após escolher empresa e sindicato, as regras de redução valerá para todos os funcionários pertencentes a empresa e ao sindicato escolhidos;

- **Data início:** data do acordo de redução
- **Data fim:** data fim do acordo de redução
- **Redução %**: percentual de redução do salário e da jornada de trabalho
- **Justificativa:** justificativa da redução
- **Ajuda compensatória:** se a empresa irá adotar a Ajuda Compensatória proposta na MP nº 936/2020 art. 9º.

**Opções de funcionários:**

- **Todos os funcionários da Empresa e /ou sindicato:** se o usuário escolher essa opção a redução se aplicará a todos os funcionários da empresa e sindicato assim que o usuário clicar no botton “Gera Redução Salarial”;
- **Filtrar colaboradores:** nessa opção o usuário poderá escolher quais funcionários terão as regras de redução aplicada; O filtro aparecerá quando o usuário preencher todos os dados acima, clicar no botão “Gera Redução Salarial” podendo escolher por departamento ou por funcionário e posteriormente clicar em OK para que a redução seja gerada.

![Imagem 3: Filtrar colaboradores: nessa opção o usuário poderá escolher quais funcionários terão as regras de redução aplicada; O…](https://ajuda.sankhya.com.br/hc/article_attachments/360080588673)

**Observação:** As regras cadastradas passarão a vigorar a partir da data início até a data fim. Lembrando que os dias anteriores à data início e os dias posteriores à data fim serão pagos sem a redução salarial, ou seja, o pagamento nessas referências será proporcional.

![Imagem 4: Tela 'Funcionários': (Aba Contrato - Sub-Aba "Força Maior ")](https://ajuda.sankhya.com.br/hc/article_attachments/19150611091607) Tela 'Funcionários': [Aba Contrato - Sub-Aba "Força Maior "]

![Imagem 5: Tela 'Funcionários': (Aba Contrato - Sub-Aba "Força Maior ")](https://ajuda.sankhya.com.br/hc/article_attachments/19150656295319)

Após realizar o cadastro da redução na rotina de Força Maior, o cadastro do funcionário será alimentado com os dados da redução. Através do cadastro do funcionário a redução poderá ser finalizada ou a data término da redução poderá ser prorrogada, conforme explicação no próximo item.

**2.1. Prorrogação da data término da redução salarial e jornada de trabalho:**

- **Prorrogação na rotina de “Força Maior”:** Na hipótese da prorrogação da redução salarial e jornada de trabalho serem para todos os funcionários do cadastro realizado anteriormente na rotina de Força Maior a alteração da data fim deverá ser realizada na rotina com o preenchimento da nova data de término da redução salarial, confirmação na tela de cadastro e do aviso mostrado em tela, conforme imagem abaixo.

![Imagem 6: Prorrogação na rotina de “Força Maior”: Na hipótese da prorrogação da redução salarial e jornada de trabalho serem para…](https://ajuda.sankhya.com.br/hc/article_attachments/19150611099159)

![Imagem 7: Prorrogação na rotina de “Força Maior”: Na hipótese da prorrogação da redução salarial e jornada de trabalho serem para…](https://ajuda.sankhya.com.br/hc/article_attachments/360079499214)

Após, a data término da redução será atualizada no cadastro do funcionário automaticamente, assim como na tabela histórica da redução.

- **Prorrogação pelo cadastro do funcionário:** Para a hipótese da prorrogação ser apenas para funcionários específicos e não abranger a todos os funcionários cadastrados na rotina de ‘Força Maior’, o primeiro passo é desvincular o funcionário da Rotina “Força Maior” para que a data fim possa ser alterada.

![Imagem 8: Prorrogação pelo cadastro do funcionário: Para a hipótese da prorrogação ser apenas para funcionários específicos e não…](https://ajuda.sankhya.com.br/hc/article_attachments/19150656306455)

Após clicar em ‘Desvincular Força Maior’, o sistema apresentará o aviso abaixo para confirmar se o usuário deseja desvincular o cadastro do funcionário da rotina de ‘Força Maior’.

![Imagem 9: Após clicar em ‘Desvincular Força Maior’, o sistema apresentará o aviso abaixo para confirmar se o usuário deseja…](https://ajuda.sankhya.com.br/hc/article_attachments/360079499434)

Escolhendo ‘Sim’, o cadastro do funcionário será desvinculado da rotina Força Maior e a data término da redução poderá ser alterada e após a alteração a nova data será salva no cadastro do funcionário e na tabela histórica da redução, conforme imagem abaixo.

![Imagem 10: Escolhendo ‘Sim’, o cadastro do funcionário será desvinculado da rotina Força Maior e a data término da redução poderá…](https://ajuda.sankhya.com.br/hc/article_attachments/19150656308503)

**Atenção:**

Na referência de término da Redução é necessário Finalizar a Suspensão/Redução no botão específico:

**Pelo cadastro do funcionário:** 

![Imagem 11: Pelo cadastro do funcionário:](https://ajuda.sankhya.com.br/hc/article_attachments/19150656315415)

**Pela rotina 'Força Maior':**

Se necessário finalizar vários funcionários de uma vez, que foram lançados por uma força maior especifica, finalizar por esse mesmo botão "Finalizar Redução/Suspensão" na tela 'Força Maior'.

**Importante:**

![Imagem 12: Para orientações sobre a Importação do leiaute para envio da redução ao Governo ,acesse: Importação do leiaute para…](https://ajuda.sankhya.com.br/hc/article_attachments/19150656283543) Para orientações sobre a **Importação do leiaute para envio da redução ao Governo**,acesse:  [Importação do leiaute para envio da redução ao Governo - MP936](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046291194)

![Imagem 13: Para orientações sobre " suspensão temporária do contrato de trabalho", acesse: Suspensão temporária do contrato de…](https://ajuda.sankhya.com.br/hc/article_attachments/19150611091607) Para orientações sobre "**suspensão temporária** do contrato de trabalho", acesse: [Suspensão temporária do contrato de trabalho - MP936. Saiba Mais!](https://ajuda.sankhya.com.br/hc/pt-br/articles/360046293694)

[![Imagem 14: Calculadora MP 936 simula acordos de redução de jornada e salário](https://ajuda.sankhya.com.br/hc/article_attachments/19150611112727) Calculadora MP 936 simula acordos de redução de jornada e salário](https://www.portaldaindustria.com.br/canais/industria-contra-covid-19/impacto-economico/#anchor-simulador)

![Imagem 15: Saiba Mais: http://www.normaslegais.com.br/legislacao/portaria-seprt-10486-2020.htm](https://ajuda.sankhya.com.br/hc/article_attachments/19150656321047) Saiba Mais: <http://www.normaslegais.com.br/legislacao/portaria-seprt-10486-2020.htm>
