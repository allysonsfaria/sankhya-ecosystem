---
id: "42427218983959"
titulo: "Como funciona a integração de dados entre Pontotel e Sankhya"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427218983959-Como-funciona-a-integra%C3%A7%C3%A3o-de-dados-entre-Pontotel-e-Sankhya"
trilha: "PONTOTEL: Sistema de marcação de ponto > Integração entre sistemas"
atualizado_em: "2026-08-03T13:29:58Z"
rotulos: ["sync_hc", "pontotel_6a3328db515a79b2c9b8c24d", "sync_hash_91fc38cd3234", "pontotel"]
---

# Como funciona a integração de dados entre Pontotel e Sankhya

![Imagem 1](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/2_1u3icba.png)

A Pontotel faz parte do Grupo Sankhya, e nossas plataformas possuem uma integração nativa. O objetivo é automatizar seus processos e garantir que os dados de pessoas e da estrutura da empresa sejam consistentes nos dois sistemas, eliminando a necessidade de cadastros duplicados.
A integração principal funciona com o ERP Sankhya sendo a "fonte da verdade" para os cadastros, enviando os dados para a Pontotel.

---

## O que é integrado

Quando você inclui ou edita as informações a seguir no ERP Sankhya, elas são automaticamente criadas ou atualizadas na plataforma Pontotel:

- Admissão de empregados
- Atualização de cadastro de empregados
- Dados pessoais (CPF, RG, e-mail, etc.)
- Demissão de empregados
- Criação de usuários vinculados aos empregados
- Inclusão de férias e afastamentos
- Edição de férias e afastamentos

Além disso, a integração **correlaciona** outros dados. Veja quais:

| Dado no Sankhya | Dado na Pontotel |
| --- | --- |
| Empresas | Empregadores |
| Departamento | Local de Trabalho |
| Carga horária histórica | Escala |
| Sindicato | Regra de cálculo e banco de horas |

---

## O que não é integrado automaticamente

A integração foca em replicar os dados dos colaboradores e os eventos de ausência. As criações das estruturas de regras e a exclusão de eventos ainda são feitas manualmente na Pontotel.
Não são atualizadas automaticamente do Sankhya para a Pontotel:

- **Exclusão** de férias e afastamentos (Se excluir no Sankhya, é preciso excluir manualmente na Pontotel).
- **Criação** de Carga histórica (Sankhya) / Escala (Pontotel).
- **Criação e configuração** de Sindicato (Sankhya) / Regra de cálculo e banco de horas (Pontotel).

> ⚠️ Atenção: Os cadastros de escala, regras de cálculo e banco de horas serão realizados no processo de implantação junto ao time de Sucesso do Cliente. Os códigos das cargas horárias históricas e sindicatos existentes no Sankhya precisam existir no PontoTel para que estas informações sejam atualizadas.

---

## O que a Pontotel envia para o Sankhya (Fechamento da Folha)

A integração também funciona no sentido inverso para fechar o ciclo da folha: a Pontotel envia os dados apurados do ponto (Verbas e Faltas) de volta para o ERP Sankhya de forma automatizada.
Isso é feito através do **Arquivo de Exportação E02**.
A plataforma Pontotel consolida todos os apontamentos (horas extras, atrasos, faltas, adicionais) em um arquivo formatado (TXT ou CSV) que pode ser integrado e importado diretamente para o ERP Sankhya para o fechamento da folha de pagamento.

> ⚠️ **Atenção:** Para que esta exportação funcione, é necessário um serviço de pré-configuração (parametrização) do arquivo E02. Essa parametrização não tem custo para clientes Sankhya.

Para saber mais sobre como funciona o E02, acesse nosso artigo: [Entenda sobre o arquivo E02 (Arquivo para importação de apontamentos)](https://sankhya.zendesk.com/hc/pt-br/articles/42427233340567)

---

## Como funciona o fluxo de ativação da integração

A ativação da integração entre Pontotel e Sankhya segue um processo estruturado, conduzido em conjunto com as equipes das duas plataformas. No geral, o processo tem previsão de conclusão em até **30 a 40 dias**, e começa de forma simples: basta uma solicitação.

1. O cliente solicita a ativação da integração pelo suporte da Pontotel ou da Sankhya.
2. Um analista entra em contato, apresenta o cronograma do projeto e solicita o preenchimento de um formulário com as informações necessárias para iniciar:
   🔗 [Preencher formulário de ativação](https://docs.google.com/forms/d/e/1FAIpQLScB6tA6zUzy_-onhI27Cguiy_HrrdK81XxBDFmWDio_hdTl3w/viewform?usp=dialog)
3. Com as bases conectadas, é gerada uma planilha de análise de dados para que o cliente identifique e corrija eventuais inconsistências nas informações cadastradas na Sankhya.
4. Após as correções, o cliente confirma e a integração é validada em ambiente de homologação pela equipe técnica.
5. O cliente realiza sua própria validação em uma ambiente de testes e, estando tudo certo, aprova o avanço.
6. A integração é ativada. Nessa etapa, os códigos e verbas são confirmados junto ao cliente.
7. O cliente valida as verbas e o funcionamento da integração de faltas. Com tudo aprovado, o processo é encerrado.

> 💡 Dica: Para começar, basta entrar em contato com o suporte da Pontotel ou da Sankhya e preencher o [formulário](https://docs.google.com/forms/d/e/1FAIpQLScB6tA6zUzy_-onhI27Cguiy_HrrdK81XxBDFmWDio_hdTl3w/viewform) acima. Nossa equipe assume o restante do processo.

---

Essa integração bidirecional é a forma mais **fácil** de garantir a **evolução** dos seus processos. O Sankhya centraliza os cadastros de **pessoas**, e a Pontotel devolve os dados de ponto prontos para o fechamento da folha, garantindo uma **gestão** unificada e **simples**.

Caso ainda tenha dúvidas ou precise de auxílio, entre em contato com o nosso time de Suporte pelo chat integrado ao [site Pontotel Gestão](https://gestao.pontotel.com.br/#/cognito/login) ou pelo [WhatsApp](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0)!
